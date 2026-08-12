"""Issues and pull requests from the forge monorepo."""

import os
from dataclasses import dataclass
from datetime import datetime

import httpx
from django.conf import settings
from django.core.management.base import CommandError
from django.db import transaction
from django.utils.dateparse import parse_datetime
from pydantic import BaseModel, ConfigDict, ValidationError

from pages.models import Issue, Member, System
from pages.sources.common import SyncResult, abort_if
from pages.sources.members import forgejo_login_map

SYSTEM_LABEL_PREFIX = "system/"


class ForgejoUser(BaseModel):
    model_config = ConfigDict(extra="ignore")

    username: str


class ForgejoLabel(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str
    color: str


class ForgejoPullRequestMeta(BaseModel):
    model_config = ConfigDict(extra="ignore")

    merged: bool = False
    merged_at: str | None = None


class ForgejoIssuePayload(BaseModel):
    model_config = ConfigDict(extra="ignore")

    number: int
    title: str
    state: str
    html_url: str
    labels: list[ForgejoLabel] = []
    user: ForgejoUser
    created_at: str
    updated_at: str
    closed_at: str | None = None
    pull_request: ForgejoPullRequestMeta | None = None


@dataclass(frozen=True)
class IssueRecord:
    number: int
    title: str
    state: str
    url: str
    system_slug: str | None
    labels: list[dict[str, str]]
    author: str
    is_pull: bool
    merged_at: datetime | None
    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    return parse_datetime(value)


def _resolve_labels(
    labels: list[ForgejoLabel], number: int, errors: list[str]
) -> tuple[str | None, list[dict[str, str]]]:
    system_slugs = sorted(
        label.name[len(SYSTEM_LABEL_PREFIX) :]
        for label in labels
        if label.name.startswith(SYSTEM_LABEL_PREFIX)
    )
    presentation_labels = [
        {"name": label.name, "color": label.color}
        for label in labels
        if not label.name.startswith(SYSTEM_LABEL_PREFIX)
    ]

    if not system_slugs:
        return None, presentation_labels

    return system_slugs[0], presentation_labels


def fetch_issues(errors: list[str]) -> list[ForgejoIssuePayload]:
    owner, repo = settings.FORGEJO_REPO.split("/", 1)
    base = settings.FORGEJO_BASE_URL.rstrip("/")
    url = f"{base}/api/v1/repos/{owner}/{repo}/issues"

    headers = {"accept": "application/json"}
    token = os.environ.get("FORGEJO_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    payloads: list[ForgejoIssuePayload] = []
    page = 1
    limit = 50

    try:
        with httpx.Client(timeout=30.0) as client:
            while True:
                response = client.get(
                    url,
                    params={"state": "all", "page": page, "limit": limit},
                    headers=headers,
                )
                response.raise_for_status()
                total = int(response.headers.get("x-total-count", 0))
                for item in response.json():
                    try:
                        payloads.append(ForgejoIssuePayload.model_validate(item))
                    except ValidationError as exc:
                        number = item.get("number", "?")
                        errors.append(f"issue #{number}: invalid payload: {exc}")
                if page * limit >= total:
                    break
                page += 1
    except httpx.HTTPError as exc:
        errors.append(f"forge API request failed: {exc}")

    return payloads


def load_issues(systems: dict[str, System], errors: list[str]) -> list[IssueRecord]:
    records: list[IssueRecord] = []
    for payload in fetch_issues(errors):
        system_slug, presentation_labels = _resolve_labels(payload.labels, payload.number, errors)
        if system_slug and system_slug not in systems:
            errors.append(f"issue #{payload.number}: unknown system label system/{system_slug}")
            continue

        is_pull = payload.pull_request is not None
        merged_at = None
        if is_pull and payload.pull_request and payload.pull_request.merged_at:
            merged_at = _parse_dt(payload.pull_request.merged_at)

        created_at = _parse_dt(payload.created_at)
        updated_at = _parse_dt(payload.updated_at)
        if created_at is None or updated_at is None:
            errors.append(f"issue #{payload.number}: missing created_at or updated_at")
            continue

        records.append(
            IssueRecord(
                number=payload.number,
                title=payload.title,
                state=payload.state,
                url=payload.html_url,
                system_slug=system_slug,
                labels=presentation_labels,
                author=payload.user.username,
                is_pull=is_pull,
                merged_at=merged_at,
                created_at=created_at,
                updated_at=updated_at,
                closed_at=_parse_dt(payload.closed_at),
            )
        )

    return records


def sync_issues(
    records: list[IssueRecord],
    systems: dict[str, System],
    members_by_forgejo: dict[str, Member],
) -> SyncResult:
    with transaction.atomic():
        for record in records:
            system = systems.get(record.system_slug) if record.system_slug else None
            Issue.objects.update_or_create(
                number=record.number,
                defaults={
                    "title": record.title,
                    "state": record.state,
                    "url": record.url,
                    "system": system,
                    "member": members_by_forgejo.get(record.author),
                    "labels": record.labels,
                    "author": record.author,
                    "is_pull": record.is_pull,
                    "merged_at": record.merged_at,
                    "created_at": record.created_at,
                    "updated_at": record.updated_at,
                    "closed_at": record.closed_at,
                },
            )

        removed, _ = Issue.objects.exclude(
            number__in=[record.number for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_issues(*, flush: bool = False) -> SyncResult:
    if not System.objects.exists():
        raise CommandError("no systems in the database — run sync_systems first")

    systems = {system.slug: system for system in System.objects.all()}
    errors: list[str] = []
    records = load_issues(systems, errors)
    abort_if(errors, "sync_issues")

    if flush:
        Issue.objects.all().delete()

    members_by_forgejo = forgejo_login_map(list(Member.objects.all()))
    return sync_issues(records, systems, members_by_forgejo)

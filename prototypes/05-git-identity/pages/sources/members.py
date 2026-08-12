"""Members: one markdown file per member under ``content/members/<slug>.md``."""

from dataclasses import dataclass
from pathlib import Path

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from pages.models import Member
from pages.sources.common import (
    SyncResult,
    abort_if,
    format_validation_error,
    render_markdown,
)


class MemberFrontmatter(BaseModel):
    """What authors write at the top of a member profile file."""

    model_config = ConfigDict(extra="forbid")

    name: str
    identities: dict[str, str | list[str]] = Field(default_factory=dict)
    active: bool = True


@dataclass(frozen=True)
class MemberRecord:
    username: str
    meta: MemberFrontmatter
    body_html: str


def forgejo_login_map(members: list[Member]) -> dict[str, Member]:
    """Map forge login strings to members from stored identity assertions."""
    mapping: dict[str, Member] = {}
    for member in members:
        forgejo = member.identities.get("forgejo")
        if isinstance(forgejo, str):
            logins = [forgejo]
        elif isinstance(forgejo, list):
            logins = forgejo
        else:
            continue
        for login in logins:
            mapping[login] = member
    return mapping


def load_members(members_dir: Path, errors: list[str]) -> list[MemberRecord]:
    records: list[MemberRecord] = []
    if not members_dir.is_dir():
        errors.append(f"{members_dir}: directory not found")
        return records

    for path in sorted(members_dir.glob("*.md")):
        record = _load_member(path, errors)
        if record is not None:
            records.append(record)

    return records


def _load_member(path: Path, errors: list[str]) -> MemberRecord | None:
    username = path.stem
    label = f"members/{path.name}"

    parsed = frontmatter.load(path)
    try:
        meta = MemberFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    return MemberRecord(
        username=username,
        meta=meta,
        body_html=render_markdown(parsed.content),
    )


def sync_members(records: list[MemberRecord]) -> SyncResult:
    with transaction.atomic():
        for record in records:
            Member.objects.update_or_create(
                username=record.username,
                defaults={
                    "name": record.meta.name,
                    "body_html": record.body_html,
                    "identities": record.meta.identities,
                    "active": record.meta.active,
                },
            )
        removed, _ = Member.objects.exclude(
            username__in=[record.username for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_members(*, flush: bool = False) -> SyncResult:
    errors: list[str] = []
    records = load_members(settings.CONTENT_DIR / "members", errors)
    abort_if(errors, "sync_members")

    if flush:
        Member.objects.all().delete()

    return sync_members(records)

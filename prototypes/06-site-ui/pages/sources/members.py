"""Members: one markdown file per member under ``content/members/<slug>.md``."""

from dataclasses import dataclass
from pathlib import Path

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from pages.models import Group, Member
from pages.sources.common import (
    SyncResult,
    abort_if,
    format_validation_error,
    group_cache,
    render_markdown,
)


class MemberFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    role: str = ""
    groups: list[str] = Field(default_factory=list)
    active: bool = True


@dataclass(frozen=True)
class MemberRecord:
    username: str
    meta: MemberFrontmatter
    body_html: str


def load_members(members_dir: Path, groups: dict[str, Group], errors: list[str]) -> list[MemberRecord]:
    records: list[MemberRecord] = []
    if not members_dir.is_dir():
        errors.append(f"{members_dir}: directory not found")
        return records

    for path in sorted(members_dir.glob("*.md")):
        record = _load_member(path, groups, errors)
        if record is not None:
            records.append(record)

    return records


def _load_member(path: Path, groups: dict[str, Group], errors: list[str]) -> MemberRecord | None:
    username = path.stem
    label = f"members/{path.name}"

    parsed = frontmatter.load(path)
    try:
        meta = MemberFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    unknown = sorted({slug for slug in meta.groups if slug not in groups})
    if unknown:
        errors.append(f"{label}: unknown groups: {', '.join(unknown)}")
        return None

    return MemberRecord(
        username=username,
        meta=meta,
        body_html=render_markdown(parsed.content),
    )


def sync_members(records: list[MemberRecord], groups: dict[str, Group]) -> SyncResult:
    with transaction.atomic():
        for record in records:
            member, _ = Member.objects.update_or_create(
                username=record.username,
                defaults={
                    "name": record.meta.name,
                    "body_html": record.body_html,
                    "role": record.meta.role,
                    "active": record.meta.active,
                },
            )
            member.groups.set([groups[slug] for slug in record.meta.groups])

        removed, _ = Member.objects.exclude(
            username__in=[record.username for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_members(*, flush: bool = False) -> SyncResult:
    groups = group_cache()
    errors: list[str] = []
    records = load_members(settings.CONTENT_DIR / "members", groups, errors)
    abort_if(errors, "sync_members")

    if flush:
        Member.objects.all().delete()

    return sync_members(records, groups)

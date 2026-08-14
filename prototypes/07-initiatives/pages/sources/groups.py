"""Groups defined in ``content/members/groups.yaml``."""

from dataclasses import dataclass
from pathlib import Path

import yaml
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, ValidationError

from pages.models import Group
from pages.sources.common import SyncResult, abort_if, format_validation_error


class GroupFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    summary: str = ""
    matrix: str = ""


@dataclass(frozen=True)
class GroupRecord:
    slug: str
    meta: GroupFrontmatter


def load_groups(path: Path, errors: list[str]) -> list[GroupRecord]:
    if not path.is_file():
        return []

    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records: list[GroupRecord] = []
    for slug, meta in raw.items():
        label = f"members/groups.yaml ({slug})"
        if not isinstance(meta, dict):
            errors.append(f"{label}: expected mapping")
            continue
        try:
            records.append(
                GroupRecord(slug=slug, meta=GroupFrontmatter.model_validate(meta))
            )
        except ValidationError as exc:
            errors.append(f"{label}: {format_validation_error(exc)}")

    return records


def sync_groups(records: list[GroupRecord]) -> SyncResult:
    with transaction.atomic():
        for record in records:
            Group.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.meta.title,
                    "summary": record.meta.summary,
                    "matrix_room": record.meta.matrix,
                },
            )
        removed, _ = Group.objects.exclude(
            slug__in=[record.slug for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_groups(*, flush: bool = False) -> SyncResult:
    errors: list[str] = []
    records = load_groups(settings.CONTENT_DIR / "members" / "groups.yaml", errors)
    abort_if(errors, "sync_groups")

    if flush:
        Group.objects.all().delete()

    return sync_groups(records)

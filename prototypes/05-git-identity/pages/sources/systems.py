"""Systems: one directory per system under ``content/systems/<slug>/``.

``system.md`` carries the marketing page and team references. Updates live in
``updates.json`` beside it — loaded by ``updates.py``, stored on the row as JSON.
"""

from dataclasses import dataclass
from pathlib import Path

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from pages.models import Member, System
from pages.sources import updates
from pages.sources.common import (
    SyncResult,
    abort_if,
    format_validation_error,
    member_cache,
    render_markdown,
    require_members,
)


class SystemFrontmatter(BaseModel):
    """What authors write at the top of ``system.md``."""

    model_config = ConfigDict(extra="forbid")

    title: str
    summary: str = ""
    teamlead: str
    admins: list[str] = Field(default_factory=list)


@dataclass(frozen=True)
class SystemRecord:
    """A validated system, ready to sync: frontmatter plus everything derived."""

    slug: str
    meta: SystemFrontmatter
    body_html: str
    updates: list[dict[str, str]]


def load_systems(
    systems_dir: Path, members: dict[str, Member], errors: list[str]
) -> list[SystemRecord]:
    records = []
    if not systems_dir.is_dir():
        return records

    for system_dir in sorted(systems_dir.iterdir()):
        if system_dir.is_dir():
            record = _load_system(system_dir, members, errors)
            if record is not None:
                records.append(record)

    return records


def _load_system(
    system_dir: Path, members: dict[str, Member], errors: list[str]
) -> SystemRecord | None:
    slug = system_dir.name
    label = f"systems/{slug}/system.md"

    path = system_dir / "system.md"
    if not path.is_file():
        errors.append(f"systems/{slug}/: missing system.md")
        return None

    parsed = frontmatter.load(path)
    try:
        meta = SystemFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    unknown = sorted({u for u in [meta.teamlead, *meta.admins] if u not in members})
    if unknown:
        errors.append(f"{label}: unknown members: {', '.join(unknown)}")
        return None

    loaded_updates = updates.load_updates(system_dir / "updates.json", slug, errors)
    if loaded_updates is None:
        return None

    return SystemRecord(
        slug=slug,
        meta=meta,
        body_html=render_markdown(parsed.content),
        updates=loaded_updates,
    )


def sync_systems(records: list[SystemRecord], members: dict[str, Member]) -> SyncResult:
    with transaction.atomic():
        for record in records:
            system, _ = System.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.meta.title,
                    "summary": record.meta.summary,
                    "body_html": record.body_html,
                    "teamlead": members[record.meta.teamlead],
                    "updates": record.updates,
                },
            )
            system.admins.set([members[username] for username in record.meta.admins])

        removed, _ = System.objects.exclude(
            slug__in=[record.slug for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_systems(*, flush: bool = False) -> SyncResult:
    require_members()

    members = member_cache()
    errors: list[str] = []
    records = load_systems(settings.CONTENT_DIR / "systems", members, errors)
    abort_if(errors, "sync_systems")

    if flush:
        System.objects.all().delete()

    return sync_systems(records, members)

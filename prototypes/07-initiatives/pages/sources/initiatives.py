"""Initiatives: one directory per initiative under ``content/initiatives/<slug>/``."""

import datetime as dt
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator

from pages.models import Initiative, Member, System
from pages.sources import updates
from pages.sources.common import (
    SyncResult,
    abort_if,
    format_validation_error,
    member_cache,
    render_markdown,
    require_members,
)


InitiativeStatus = Literal[
    "proposal", "seeking-contributors", "active", "paused", "completed"
]


class InitiativeFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    summary: str = ""
    status: InitiativeStatus = "active"
    start_date: dt.date
    end_date: dt.date | None = None
    takers: list[str] = Field(default_factory=list)
    systems: list[str] = Field(default_factory=list)
    loomio: str = ""
    matrix: str = ""

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def _accept_yaml_datetime(cls, value: object) -> object:
        if isinstance(value, dt.datetime):
            return value.date()
        return value

    @model_validator(mode="after")
    def _end_on_or_after_start(self) -> "InitiativeFrontmatter":
        if self.end_date is not None and self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date")
        return self


@dataclass(frozen=True)
class InitiativeRecord:
    slug: str
    meta: InitiativeFrontmatter
    body_html: str
    updates: list[dict[str, str]]


def load_initiatives(
    initiatives_dir: Path,
    members: dict[str, Member],
    system_slugs: set[str],
    errors: list[str],
) -> list[InitiativeRecord]:
    records = []
    if not initiatives_dir.is_dir():
        return records

    for initiative_dir in sorted(initiatives_dir.iterdir()):
        if initiative_dir.is_dir():
            record = _load_initiative(initiative_dir, members, system_slugs, errors)
            if record is not None:
                records.append(record)

    return records


def _load_initiative(
    initiative_dir: Path,
    members: dict[str, Member],
    system_slugs: set[str],
    errors: list[str],
) -> InitiativeRecord | None:
    slug = initiative_dir.name
    label = f"initiatives/{slug}/initiative.md"

    path = initiative_dir / "initiative.md"
    if not path.is_file():
        errors.append(f"initiatives/{slug}/: missing initiative.md")
        return None

    parsed = frontmatter.load(path)
    try:
        meta = InitiativeFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    unknown_takers = sorted({u for u in meta.takers if u not in members})
    if unknown_takers:
        errors.append(f"{label}: unknown takers: {', '.join(unknown_takers)}")
        return None

    unknown_systems = sorted({u for u in meta.systems if u not in system_slugs})
    if unknown_systems:
        errors.append(f"{label}: unknown systems: {', '.join(unknown_systems)}")
        return None

    loaded_updates = updates.load_updates(
        initiative_dir / "updates.json", slug, errors, collection="initiatives"
    )
    if loaded_updates is None:
        return None

    return InitiativeRecord(
        slug=slug,
        meta=meta,
        body_html=render_markdown(parsed.content),
        updates=loaded_updates,
    )


def sync_initiatives(
    records: list[InitiativeRecord], members: dict[str, Member]
) -> SyncResult:
    with transaction.atomic():
        for record in records:
            initiative, _ = Initiative.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.meta.title,
                    "summary": record.meta.summary,
                    "status": record.meta.status,
                    "start_date": record.meta.start_date,
                    "end_date": record.meta.end_date,
                    "body_html": record.body_html,
                    "loomio_url": record.meta.loomio,
                    "matrix_room": record.meta.matrix,
                    "updates": record.updates,
                },
            )
            initiative.takers.set([members[username] for username in record.meta.takers])
            initiative.systems.set(
                [System.objects.get(slug=slug) for slug in record.meta.systems]
            )

        removed, _ = Initiative.objects.exclude(
            slug__in=[record.slug for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_initiatives(*, flush: bool = False) -> SyncResult:
    require_members()

    members = member_cache()
    system_slugs = set(System.objects.values_list("slug", flat=True))
    errors: list[str] = []
    records = load_initiatives(
        settings.CONTENT_DIR / "initiatives",
        members,
        system_slugs,
        errors,
    )
    abort_if(errors, "sync_initiatives")

    if flush:
        Initiative.objects.all().delete()

    return sync_initiatives(records, members)

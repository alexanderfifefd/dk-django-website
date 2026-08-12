"""Groups defined in ``content/members/groups.yaml``."""

from pathlib import Path

import yaml
from django.conf import settings
from django.db import transaction

from pages.models import Group
from pages.sources.common import SyncResult


def load_groups(path: Path) -> list[tuple[str, str]]:
    if not path.is_file():
        return []

    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records: list[tuple[str, str]] = []
    for slug, meta in raw.items():
        if isinstance(meta, dict):
            title = meta.get("title", slug.replace("-", " ").title())
            records.append((slug, title))
    return records


def sync_groups(records: list[tuple[str, str]]) -> SyncResult:
    with transaction.atomic():
        for slug, title in records:
            Group.objects.update_or_create(slug=slug, defaults={"title": title})
        removed, _ = Group.objects.exclude(slug__in=[slug for slug, _ in records]).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_groups(*, flush: bool = False) -> SyncResult:
    records = load_groups(settings.CONTENT_DIR / "members" / "groups.yaml")

    if flush:
        Group.objects.all().delete()

    return sync_groups(records)

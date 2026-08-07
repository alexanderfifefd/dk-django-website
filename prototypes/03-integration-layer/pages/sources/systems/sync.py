from django.db import transaction

from pages.models import Member, System
from pages.sources.errors import SyncResult
from pages.sources.systems.load import SystemRecord


def sync_systems(records: list[SystemRecord], members: dict[str, Member]) -> SyncResult:
    with transaction.atomic():
        slugs = [record.slug for record in records]
        for record in records:
            system, _ = System.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.title,
                    "summary": record.summary,
                    "body_html": record.body_html,
                    "teamlead": members[record.teamlead_username],
                    "updates": record.updates,
                },
            )
            system.admins.set([members[username] for username in record.admin_usernames])

        removed, _ = System.objects.exclude(slug__in=slugs).delete()

    return SyncResult(upserted=len(slugs), removed=removed)

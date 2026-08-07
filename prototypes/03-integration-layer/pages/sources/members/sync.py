from django.db import transaction

from pages.models import Member
from pages.sources.errors import SyncResult
from pages.sources.members.schema import MemberSource


def sync_members(records: list[MemberSource]) -> SyncResult:
    with transaction.atomic():
        usernames = [record.username for record in records]
        for record in records:
            Member.objects.update_or_create(
                username=record.username,
                defaults={"name": record.name},
            )
        removed, _ = Member.objects.exclude(username__in=usernames).delete()

    return SyncResult(upserted=len(usernames), removed=removed)

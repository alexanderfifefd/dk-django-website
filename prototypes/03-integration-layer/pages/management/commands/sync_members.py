from django.core.management.base import BaseCommand

from pages.sources import members


class Command(BaseCommand):
    help = "Sync external/members.json into the Member table."

    def handle(self, *args, **options):
        outcome = members.run_sync_members()
        self.stdout.write(
            self.style.SUCCESS(
                f"Synced {outcome.upserted} members, removed {outcome.removed}."
            )
        )

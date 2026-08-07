from django.core.management.base import BaseCommand

from pages.sources.pipeline import run_sync_members


class Command(BaseCommand):
    help = "Sync fixtures/members.json into the Member table."

    def handle(self, *args, **options):
        outcome = run_sync_members()
        self.stdout.write(
            self.style.SUCCESS(
                f"Synced {outcome.upserted} members, removed {outcome.removed}."
            )
        )

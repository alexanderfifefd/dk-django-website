from django.core.management.base import BaseCommand

from pages.sources import systems


class Command(BaseCommand):
    help = "Sync content/systems/ into the System table."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete every system first and rebuild from scratch.",
        )

    def handle(self, *args, flush, **options):
        outcome = systems.run_sync_systems(flush=flush)
        self.stdout.write(
            self.style.SUCCESS(
                f"Synced {outcome.upserted} systems, removed {outcome.removed}."
            )
        )

from django.core.management.base import BaseCommand

from pages.sources import issues


class Command(BaseCommand):
    help = "Sync issues and pull requests from the configured Forgejo repo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete every cached issue first and rebuild from scratch.",
        )

    def handle(self, *args, flush, **options):
        outcome = issues.run_sync_issues(flush=flush)
        self.stdout.write(
            self.style.SUCCESS(
                f"Synced {outcome.upserted} issues, removed {outcome.removed}."
            )
        )

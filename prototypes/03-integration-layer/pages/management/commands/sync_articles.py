from django.core.management.base import BaseCommand

from pages.sources import articles


class Command(BaseCommand):
    help = "Sync content/blog/ into the Article table."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete every article first and rebuild from scratch.",
        )

    def handle(self, *args, flush, **options):
        outcome = articles.run_sync_articles(flush=flush)
        self.stdout.write(
            self.style.SUCCESS(
                f"Synced {outcome.upserted} articles, removed {outcome.removed}."
            )
        )

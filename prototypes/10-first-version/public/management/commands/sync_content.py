from django.core.management.base import BaseCommand

from public.loaders.articles import run_sync_articles


class Command(BaseCommand):
    help = "Sync articles from content/articles/ into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete derived content first and rebuild from scratch.",
        )

    def handle(self, *args, **options):
        result = run_sync_articles(flush=options["flush"])
        self.stdout.write(
            self.style.SUCCESS(
                f"Synced {result.upserted} article(s), removed {result.removed}."
            )
        )

from django.core.management.base import BaseCommand

from public.loaders.articles import run_load_articles


class Command(BaseCommand):
    help = "Load articles from content/articles/ into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete derived articles first and rebuild from scratch.",
        )

    def handle(self, *args, **options):
        result = run_load_articles(flush=options["flush"])
        self.stdout.write(
            self.style.SUCCESS(
                f"Loaded {result.upserted} article(s), removed {result.removed}."
            )
        )

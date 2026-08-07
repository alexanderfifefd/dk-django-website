from django.core.management.base import BaseCommand

from pages.sources.pipeline import run_ingest


class Command(BaseCommand):
    help = "Sync content/systems/ and content/blog/ into derived tables."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete every system and article first and rebuild from scratch.",
        )

    def handle(self, *args, flush, **options):
        outcome = run_ingest(flush=flush)
        self.stdout.write(
            self.style.SUCCESS(
                f"Ingested {outcome.systems.upserted} systems "
                f"(removed {outcome.systems.removed}), "
                f"{outcome.articles.upserted} articles "
                f"(removed {outcome.articles.removed})."
            )
        )

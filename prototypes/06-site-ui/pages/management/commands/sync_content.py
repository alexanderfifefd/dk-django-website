from django.core.management.base import BaseCommand

from pages.sources.sync import run_sync_content


class Command(BaseCommand):
    help = "Sync all content from content/ into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete derived content first and rebuild from scratch.",
        )

    def handle(self, *args, **options):
        run_sync_content(flush=options["flush"])
        self.stdout.write(self.style.SUCCESS("Synced content from disk."))

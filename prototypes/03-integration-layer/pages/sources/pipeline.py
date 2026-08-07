from dataclasses import dataclass

from django.conf import settings
from django.core.management.base import CommandError
from django.db import transaction

from pages.models import Article, Member, System
from pages.sources.articles.load import load_all_articles
from pages.sources.articles.sync import sync_articles
from pages.sources.errors import IngestReport, SyncResult
from pages.sources.members.load import load_members
from pages.sources.members.sync import sync_members
from pages.sources.systems.load import load_all_systems
from pages.sources.systems.sync import sync_systems


@dataclass(frozen=True)
class IngestOutcome:
    systems: SyncResult
    articles: SyncResult


def run_sync_members() -> SyncResult:
    report = IngestReport()
    records = load_members(settings.MEMBERS_FIXTURE, report)
    _raise_if_errors(report, "sync_members aborted, nothing written")

    return sync_members(records)


def run_ingest(*, flush: bool = False) -> IngestOutcome:
    if not Member.objects.exists():
        raise CommandError("no members in the database — run sync_members first")

    members = {member.username: member for member in Member.objects.all()}
    report = IngestReport()

    system_records = load_all_systems(settings.CONTENT_DIR / "systems", members, report)
    system_slugs = {record.slug for record in system_records}

    article_records = load_all_articles(
        settings.CONTENT_DIR / "blog",
        members,
        system_slugs,
        report,
    )
    _raise_if_errors(report, "ingest aborted, nothing written")

    with transaction.atomic():
        if flush:
            Article.objects.all().delete()
            System.objects.all().delete()

        systems = sync_systems(system_records, members)
        articles = sync_articles(article_records, members)

    return IngestOutcome(systems=systems, articles=articles)


def _raise_if_errors(report: IngestReport, message: str) -> None:
    if report.errors:
        raise CommandError(f"{message}:\n  " + "\n  ".join(report.errors))

from django.db import transaction

from pages.models import Article, Member, System
from pages.sources.articles.load import ArticleRecord
from pages.sources.errors import SyncResult


def sync_articles(records: list[ArticleRecord], members: dict[str, Member]) -> SyncResult:
    with transaction.atomic():
        slugs = [record.slug for record in records]
        for record in records:
            system = (
                System.objects.get(slug=record.system_slug) if record.system_slug else None
            )
            Article.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.title,
                    "date": record.date,
                    "author": members[record.author_username],
                    "system": system,
                    "summary": record.summary,
                    "body_html": record.body_html,
                },
            )

        removed, _ = Article.objects.exclude(slug__in=slugs).delete()

    return SyncResult(upserted=len(slugs), removed=removed)

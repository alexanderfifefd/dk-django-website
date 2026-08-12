"""Run every file-backed sync in dependency order."""

from pages.models import Article, Group, Member, System
from pages.sources import articles, groups, members, systems


def run_sync_content(*, flush: bool = False) -> None:
    if flush:
        Article.objects.all().delete()
        System.objects.all().delete()
        Member.objects.all().delete()
        Group.objects.all().delete()

    groups.run_sync_groups()
    members.run_sync_members()
    systems.run_sync_systems()
    articles.run_sync_articles()

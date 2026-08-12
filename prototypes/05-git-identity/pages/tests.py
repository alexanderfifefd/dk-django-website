from datetime import datetime, timezone

from django.test import TestCase

from pages.models import Issue, Member
from pages.sources import issues
from pages.sources.issues import IssueRecord
from pages.sources.members import forgejo_login_map


class ForgejoLoginMapTests(TestCase):
    def test_maps_string_and_list_identities(self):
        alice = Member.objects.create(
            username="alice",
            name="Alice Chen",
            identities={"forgejo": "alice"},
        )
        alex = Member.objects.create(
            username="alex",
            name="Alexander",
            identities={"forgejo": ["alexanrf", "alex-old"]},
        )

        mapping = forgejo_login_map(list(Member.objects.all()))

        self.assertEqual(mapping["alice"], alice)
        self.assertEqual(mapping["alexanrf"], alex)
        self.assertEqual(mapping["alex-old"], alex)


class IssueMemberLinkTests(TestCase):
    def test_sync_issues_links_member_by_forgejo_login(self):
        member = Member.objects.create(
            username="alex",
            name="Alexander",
            identities={"forgejo": "alexanrf"},
        )
        record = IssueRecord(
            number=4,
            title="Test PR",
            state="open",
            url="https://forge.example/pulls/4",
            system_slug=None,
            labels=[],
            author="alexanrf",
            is_pull=True,
            merged_at=None,
            created_at=datetime(2026, 8, 8, 11, 56, 32, tzinfo=timezone.utc),
            updated_at=datetime(2026, 8, 8, 12, 19, 38, tzinfo=timezone.utc),
            closed_at=None,
        )

        issues.sync_issues([record], {}, forgejo_login_map([member]))

        issue = Issue.objects.get(number=4)
        self.assertEqual(issue.member, member)
        self.assertEqual(issue.author, "alexanrf")

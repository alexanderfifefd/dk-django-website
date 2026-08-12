from django.db import models


class Member(models.Model):
    """A collective member, derived from ``content/members/<slug>.md``."""

    username = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    body_html = models.TextField(blank=True)
    identities = models.JSONField(default=dict, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class System(models.Model):
    """A piece of software the collective maintains, derived from ``system.md``."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body_html = models.TextField()
    teamlead = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="systems_led")
    admins = models.ManyToManyField(Member, related_name="systems_administered", blank=True)
    updates = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug


class Issue(models.Model):
    """A forge issue or pull request, cached from the monorepo API."""

    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=500)
    state = models.CharField(max_length=10)
    url = models.URLField(max_length=500)
    system = models.ForeignKey(
        System, on_delete=models.SET_NULL, related_name="issues", null=True, blank=True
    )
    member = models.ForeignKey(
        Member, on_delete=models.SET_NULL, related_name="issues", null=True, blank=True
    )
    labels = models.JSONField(default=list, blank=True)
    author = models.CharField(max_length=200)
    is_pull = models.BooleanField(default=False)
    merged_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        kind = "PR" if self.is_pull else "issue"
        return f"#{self.number} ({kind})"

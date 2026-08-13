from django.db import models


class Group(models.Model):
    """Org group defined in ``content/members/groups.yaml``."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug


class Member(models.Model):
    """Collective member, derived from ``content/members/<slug>.md``."""

    username = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    body_html = models.TextField(blank=True)
    role = models.CharField(max_length=200, blank=True)
    groups = models.ManyToManyField(Group, related_name="members", blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class System(models.Model):
    """Software the collective maintains, derived from ``system.md``."""

    class Stage(models.TextChoices):
        SUGGESTION = "suggestion", "Suggestion"
        DEVELOPMENT = "development", "Development"
        PRODUCTION = "production", "Production"

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body_html = models.TextField()
    stage = models.CharField(max_length=20, choices=Stage.choices, default=Stage.PRODUCTION)
    url = models.URLField(blank=True)
    teamlead = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="systems_led")
    admins = models.ManyToManyField(Member, related_name="systems_administered", blank=True)
    updates = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug


class Article(models.Model):
    """Blog post derived from ``content/articles/<slug>.md``."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    author = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="articles")
    system = models.ForeignKey(
        System, on_delete=models.PROTECT, related_name="articles", null=True, blank=True
    )
    summary = models.TextField(blank=True)
    body_html = models.TextField()

    class Meta:
        ordering = ["-date", "slug"]

    def __str__(self):
        return self.slug

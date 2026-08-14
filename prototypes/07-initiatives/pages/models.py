from django.db import models


class Group(models.Model):
    """Org group defined in ``content/members/groups.yaml``."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    matrix_room = models.CharField(max_length=200, blank=True)

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


class Recruiting(models.TextChoices):
    OPEN = "open", "Open"


class Initiative(models.Model):
    """Goal-oriented effort, derived from ``content/initiatives/<slug>/initiative.md``."""

    class Status(models.TextChoices):
        PROPOSED = "proposed", "Proposed"
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        COMPLETED = "completed", "Completed"

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body_html = models.TextField()
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.ACTIVE)
    recruiting = models.CharField(
        max_length=20, choices=Recruiting.choices, blank=True, default=""
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    loomio_url = models.URLField(blank=True)
    matrix_room = models.CharField(max_length=200, blank=True)
    updates = models.JSONField(default=list, blank=True)
    takers = models.ManyToManyField(Member, related_name="initiatives_led", blank=True)
    systems = models.ManyToManyField("System", related_name="initiatives", blank=True)

    class Meta:
        ordering = ["slug"]

    def __str__(self):
        return self.slug


class System(models.Model):
    """Software the collective maintains, derived from ``system.md``."""

    class Stage(models.TextChoices):
        IDEA = "idea", "Idea"
        DEVELOPMENT = "development", "Development"
        PRODUCTION = "production", "Production"

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body_html = models.TextField()
    stage = models.CharField(max_length=20, choices=Stage.choices, default=Stage.PRODUCTION)
    recruiting = models.CharField(
        max_length=20, choices=Recruiting.choices, blank=True, default=""
    )
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
    author = models.ForeignKey(
        Member, on_delete=models.PROTECT, related_name="articles", null=True, blank=True
    )
    author_group = models.ForeignKey(
        Group, on_delete=models.PROTECT, related_name="articles", null=True, blank=True
    )
    system = models.ForeignKey(
        System, on_delete=models.PROTECT, related_name="articles", null=True, blank=True
    )
    initiative = models.ForeignKey(
        Initiative, on_delete=models.PROTECT, related_name="articles", null=True, blank=True
    )
    summary = models.TextField(blank=True)
    body_html = models.TextField()

    class Meta:
        ordering = ["-date", "slug"]

    def __str__(self):
        return self.slug

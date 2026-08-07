from django.db import models


class Member(models.Model):
    """Cached profile from the identity provider. Nothing in git creates one."""

    username = models.SlugField(unique=True)
    name = models.CharField(max_length=200)

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


class Article(models.Model):
    """A blog post derived from ``content/blog/*.md``."""

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

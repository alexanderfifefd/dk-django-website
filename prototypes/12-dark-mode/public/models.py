from django.db import models


class Article(models.Model):
    """Blog post derived from ``content/articles/<slug>.md``."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    author = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body_html = models.TextField()

    class Meta:
        ordering = ["-date", "slug"]

    def __str__(self):
        return self.slug

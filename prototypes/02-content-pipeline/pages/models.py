from django.db import models


class Post(models.Model):
    """A blog post row derived from a markdown file by ``manage.py ingest``.

    Never edited by hand: files in ``content/blog/`` are the source of
    truth, and this table can be flushed and rebuilt from them at any time.
    """

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    tags = models.JSONField(default=list, blank=True)
    summary = models.TextField(blank=True)
    body_html = models.TextField()

    class Meta:
        ordering = ["-date", "slug"]

    def __str__(self):
        return self.slug

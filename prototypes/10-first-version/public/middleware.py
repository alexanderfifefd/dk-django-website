from django.core.management.base import CommandError
from django.http import HttpResponse
from django.template import engines

from public.loaders.articles import run_load_articles


class ContentLoadMiddleware:
    """Re-load git-owned articles from disk on every request in DEBUG."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            run_load_articles()
        except CommandError as exc:
            return self._load_error_response(exc)
        return self.get_response(request)

    def _load_error_response(self, exc: CommandError) -> HttpResponse:
        template = engines["django"].from_string(
            """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Article load failed</title></head>
<body>
  <h1>Article load failed</h1>
  <pre>{{ message }}</pre>
</body>
</html>"""
        )
        return HttpResponse(
            template.render({"message": str(exc)}),
            status=500,
            content_type="text/html; charset=utf-8",
        )

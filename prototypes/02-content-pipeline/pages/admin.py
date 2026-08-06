from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Read-only: rows are derived from content/blog/ by `manage.py ingest`,
    so any hand edit here would be erased by the next run."""

    list_display = ("slug", "title", "date", "tags", "summary")
    ordering = ("-date",)
    search_fields = ("slug", "title", "summary", "body_html")
    list_filter = ("date",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

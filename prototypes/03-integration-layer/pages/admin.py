from django.contrib import admin

from .models import Article, Member, System


class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Member)
class MemberAdmin(ReadOnlyAdmin):
    list_display = ("username", "name")
    search_fields = ("username", "name")


@admin.register(System)
class SystemAdmin(ReadOnlyAdmin):
    list_display = ("slug", "title", "teamlead", "summary")
    search_fields = ("slug", "title", "summary")
    filter_horizontal = ("admins",)


@admin.register(Article)
class ArticleAdmin(ReadOnlyAdmin):
    list_display = ("slug", "title", "date", "author", "system", "summary")
    list_filter = ("date", "system")
    search_fields = ("slug", "title", "summary", "body_html")

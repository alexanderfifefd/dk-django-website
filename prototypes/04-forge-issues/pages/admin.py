from django.contrib import admin

from .models import Issue, Member, System


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


@admin.register(Issue)
class IssueAdmin(ReadOnlyAdmin):
    list_display = ("number", "title", "state", "is_pull", "system", "author", "merged_at")
    list_filter = ("state", "is_pull", "system")
    search_fields = ("title", "author")

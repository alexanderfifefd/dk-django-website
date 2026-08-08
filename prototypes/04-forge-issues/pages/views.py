from django.shortcuts import get_object_or_404, render

from .models import Issue, Member, System


def _recent_updates(limit=5):
    updates = []
    for system in System.objects.all():
        for item in system.updates:
            updates.append(
                {
                    "date": item["date"],
                    "kind": item["kind"],
                    "message": item["message"],
                    "system": system,
                }
            )
    updates.sort(key=lambda u: u["date"], reverse=True)
    return updates[:limit]


def _visible_prs(queryset):
    """Pull requests worth showing — excludes declined (closed without merge)."""
    return (
        queryset.filter(is_pull=True)
        .exclude(state="closed", merged_at__isnull=True)
        .order_by("-updated_at")
    )


def home(request):
    return render(
        request,
        "pages/home.html",
        {
            "recent_updates": _recent_updates(),
            "recent_issues": Issue.objects.filter(
                is_pull=False, state="open", system__isnull=False
            )
            .select_related("system")
            .order_by("-created_at")[:5],
            "pull_requests": _visible_prs(
                Issue.objects.filter(system__isnull=False)
            ).select_related("system")[:10],
        },
    )


def systems_index(request):
    return render(
        request,
        "pages/systems_index.html",
        {"systems": System.objects.select_related("teamlead")},
    )


def system_detail(request, slug):
    system = get_object_or_404(
        System.objects.select_related("teamlead").prefetch_related("admins"),
        slug=slug,
    )
    system_issues = Issue.objects.filter(system=system)
    return render(
        request,
        "pages/system_detail.html",
        {
            "system": system,
            "open_issues": system_issues.filter(is_pull=False, state="open").order_by(
                "-created_at"
            ),
            "pull_requests": _visible_prs(system_issues),
        },
    )


def member_detail(request, username):
    member = get_object_or_404(Member, username=username)
    return render(
        request,
        "pages/member_detail.html",
        {
            "member": member,
            "systems_led": member.systems_led.all(),
            "systems_administered": member.systems_administered.all(),
        },
    )

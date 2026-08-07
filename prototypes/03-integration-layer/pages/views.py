from django.shortcuts import get_object_or_404, render

from .models import Article, Member, System


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


def home(request):
    return render(
        request,
        "pages/home.html",
        {
            "latest_articles": Article.objects.select_related("author", "system")[:3],
            "recent_updates": _recent_updates(),
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
        System.objects.select_related("teamlead").prefetch_related("admins", "articles__author"),
        slug=slug,
    )
    return render(request, "pages/system_detail.html", {"system": system})


def blog_index(request):
    return render(
        request,
        "pages/blog_index.html",
        {"articles": Article.objects.select_related("author", "system")},
    )


def blog_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "system"),
        slug=slug,
    )
    return render(request, "pages/blog_detail.html", {"article": article})


def member_detail(request, username):
    member = get_object_or_404(Member, username=username)
    return render(
        request,
        "pages/member_detail.html",
        {
            "member": member,
            "systems_led": member.systems_led.all(),
            "systems_administered": member.systems_administered.all(),
            "articles": member.articles.select_related("system"),
        },
    )

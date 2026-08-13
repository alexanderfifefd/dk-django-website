from django.shortcuts import get_object_or_404, render

from .models import Article, Member, System


def home(request):
    return render(
        request,
        "pages/home.html",
        {
            "systems": System.objects.all(),
            "latest_articles": Article.objects.select_related("author", "system")[:3],
        },
    )


def systems_index(request):
    return render(
        request,
        "pages/systems_index.html",
        {"systems": System.objects.all()},
    )


def system_detail(request, slug):
    system = get_object_or_404(
        System.objects.select_related("teamlead").prefetch_related(
            "admins", "articles__author"
        ),
        slug=slug,
    )
    return render(request, "pages/system_detail.html", {"system": system})


def members_index(request):
    return render(
        request,
        "pages/members_index.html",
        {
            "members": Member.objects.filter(active=True).prefetch_related(
                "groups", "systems_led", "systems_administered"
            ),
        },
    )


def member_detail(request, username):
    member = get_object_or_404(
        Member.objects.prefetch_related(
            "groups", "systems_led", "systems_administered", "articles__system"
        ),
        username=username,
    )
    return render(request, "pages/member_detail.html", {"member": member})


def articles_index(request):
    return render(
        request,
        "pages/articles_index.html",
        {"articles": Article.objects.select_related("author", "system")},
    )


def article_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "system"),
        slug=slug,
    )
    return render(request, "pages/article_detail.html", {"article": article})


def about(request):
    return render(
        request,
        "pages/about.html",
        {
            "board_members": Member.objects.filter(active=True, groups__slug="board").order_by(
                "username"
            ),
        },
    )


def join(request):
    return render(
        request,
        "pages/join.html",
        {"submitted": request.method == "POST"},
    )

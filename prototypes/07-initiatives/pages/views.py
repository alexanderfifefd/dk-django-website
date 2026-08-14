from django.shortcuts import get_object_or_404, render

from .models import Article, Initiative, Member, System


def home(request):
    systems = System.objects.all()
    initiatives = Initiative.objects.filter(
        status__in=[
            Initiative.Status.ACTIVE,
            Initiative.Status.SEEKING_CONTRIBUTORS,
        ]
    ).prefetch_related("takers").order_by("-start_date", "slug")
    return render(
        request,
        "pages/home.html",
        {
            "featured_systems": systems[:3],
            "featured_initiatives": initiatives[:3],
            "latest_articles": Article.objects.select_related(
                "author", "system", "initiative"
            )[:3],
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
            "admins", "articles__author", "initiatives"
        ),
        slug=slug,
    )
    return render(request, "pages/system_detail.html", {"system": system})


def initiatives_index(request):
    return render(
        request,
        "pages/initiatives_index.html",
        {
            "initiatives": Initiative.objects.prefetch_related(
                "takers", "systems"
            ).order_by("-start_date", "slug"),
        },
    )


def initiative_detail(request, slug):
    initiative = get_object_or_404(
        Initiative.objects.prefetch_related(
            "takers", "systems", "articles__author"
        ),
        slug=slug,
    )
    return render(request, "pages/initiative_detail.html", {"initiative": initiative})


def members_index(request):
    return render(
        request,
        "pages/members_index.html",
        {
            "members": Member.objects.filter(active=True).prefetch_related(
                "groups", "systems_led", "systems_administered", "initiatives_led"
            ),
        },
    )


def member_detail(request, username):
    member = get_object_or_404(
        Member.objects.prefetch_related(
            "groups",
            "systems_led",
            "systems_administered",
            "initiatives_led",
            "articles__system",
            "articles__initiative",
        ),
        username=username,
    )
    return render(request, "pages/member_detail.html", {"member": member})


def articles_index(request):
    return render(
        request,
        "pages/articles_index.html",
        {"articles": Article.objects.select_related("author", "system", "initiative")},
    )


def article_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "system", "initiative"),
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

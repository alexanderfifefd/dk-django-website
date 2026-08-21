from django.db.models import Case, IntegerField, Prefetch, Value, When
from django.shortcuts import get_object_or_404, render

from .models import Article, Group, Initiative, Member, Recruiting, System

ORG_GROUP_ORDER = ["board", "maintainers", "moderators"]

INITIATIVE_STATUS_ORDER = Case(
    When(status=Initiative.Status.ACTIVE, then=Value(0)),
    When(status=Initiative.Status.PROPOSED, then=Value(1)),
    When(status=Initiative.Status.COMPLETED, then=Value(2)),
    When(status=Initiative.Status.PAUSED, then=Value(3)),
    default=Value(99),
    output_field=IntegerField(),
)

SYSTEM_STAGE_ORDER = Case(
    When(stage=System.Stage.PRODUCTION, then=Value(0)),
    When(stage=System.Stage.DEVELOPMENT, then=Value(1)),
    When(stage=System.Stage.IDEA, then=Value(2)),
    default=Value(99),
    output_field=IntegerField(),
)


def _initiative_queryset():
    return Initiative.objects.prefetch_related("takers", "systems").order_by(
        INITIATIVE_STATUS_ORDER,
        "-start_date",
        "slug",
    )


def _system_queryset():
    return System.objects.select_related("teamlead").order_by(
        SYSTEM_STAGE_ORDER,
        "slug",
    )


def _recruiting_initiatives():
    return _initiative_queryset().filter(recruiting=Recruiting.OPEN)


def _recruiting_systems():
    return _system_queryset().filter(recruiting=Recruiting.OPEN)


def home(request):
    systems = _system_queryset()
    initiatives = _initiative_queryset().filter(status=Initiative.Status.ACTIVE)
    return render(
        request,
        "pages/home.html",
        {
            "featured_systems": systems.filter(
                stage__in=[System.Stage.PRODUCTION, System.Stage.DEVELOPMENT]
            )[:3],
            "featured_initiatives": initiatives[:3],
            "latest_articles": Article.objects.select_related(
                "author", "author_group", "system", "initiative"
            )[:3],
        },
    )


def systems_index(request):
    systems = _system_queryset()
    return render(
        request,
        "pages/systems_index.html",
        {
            "production_systems": systems.filter(stage=System.Stage.PRODUCTION),
            "development_systems": systems.filter(stage=System.Stage.DEVELOPMENT),
            "idea_systems": systems.filter(stage=System.Stage.IDEA),
        },
    )


def system_detail(request, slug):
    system = get_object_or_404(
        System.objects.select_related("teamlead").prefetch_related(
            "admins", "articles__author", "articles__author_group", "initiatives"
        ),
        slug=slug,
    )
    return render(request, "pages/system_detail.html", {"system": system})


def initiatives_index(request):
    initiatives = _initiative_queryset()
    return render(
        request,
        "pages/initiatives_index.html",
        {
            "active_initiatives": initiatives.filter(status=Initiative.Status.ACTIVE),
            "proposed_initiatives": initiatives.filter(status=Initiative.Status.PROPOSED),
            "closed_initiatives": initiatives.filter(
                status__in=[Initiative.Status.COMPLETED, Initiative.Status.PAUSED]
            ),
        },
    )


def initiative_detail(request, slug):
    initiative = get_object_or_404(
        Initiative.objects.prefetch_related(
            "takers", "systems", "articles__author", "articles__author_group"
        ),
        slug=slug,
    )
    return render(request, "pages/initiative_detail.html", {"initiative": initiative})


def members_index(request):
    active_members = Member.objects.filter(active=True).order_by("username")
    org_groups = []
    for slug in ORG_GROUP_ORDER:
        group = (
            Group.objects.filter(slug=slug)
            .prefetch_related(
                Prefetch(
                    "members",
                    queryset=active_members.prefetch_related(
                        "systems_led",
                        "systems_administered",
                        "initiatives_led",
                    ),
                )
            )
            .first()
        )
        if group is not None:
            org_groups.append(group)

    return render(
        request,
        "pages/members_index.html",
        {"org_groups": org_groups},
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
        {"articles": Article.objects.select_related("author", "author_group", "system", "initiative")},
    )


def article_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "author_group", "system", "initiative"),
        slug=slug,
    )
    return render(request, "pages/article_detail.html", {"article": article})


def about(request):
    return render(request, "pages/about.html")


def join(request):
    return render(request, "pages/join.html")


def join_account(request):
    return render(request, "pages/join_account.html")


def join_member(request):
    return render(
        request,
        "pages/join_member.html",
        {"submitted": request.method == "POST"},
    )


def join_volunteer(request):
    return render(
        request,
        "pages/join_volunteer.html",
        {
            "submitted": request.method == "POST",
            "recruiting_initiatives": _recruiting_initiatives(),
            "recruiting_systems": _recruiting_systems(),
        },
    )

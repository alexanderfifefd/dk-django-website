from django.shortcuts import get_object_or_404, render

from .models import Article


def home(request):
    return render(
        request,
        "public/home.html",
        {"latest_articles": Article.objects.all()[:3]},
    )


def articles_index(request):
    return render(
        request,
        "public/articles/index.html",
        {"articles": Article.objects.all()},
    )


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "public/articles/detail.html", {"article": article})


def about(request):
    return render(request, "public/about.html")


def design_lab(request):
    return render(request, "public/design_lab.html")


def join(request):
    return render(request, "public/join/index.html")


def join_account(request):
    return render(request, "public/join/account.html")


def join_member(request):
    return render(
        request,
        "public/join/member.html",
        {"submitted": request.method == "POST"},
    )


def join_volunteer(request):
    return render(
        request,
        "public/join/volunteer.html",
        {"submitted": request.method == "POST"},
    )

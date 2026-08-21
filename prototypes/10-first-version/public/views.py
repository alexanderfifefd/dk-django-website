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
        "public/articles_index.html",
        {"articles": Article.objects.all()},
    )


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "public/article_detail.html", {"article": article})


def about(request):
    return render(request, "public/about.html")


def join(request):
    return render(request, "public/join.html")


def join_account(request):
    return render(request, "public/join_account.html")


def join_member(request):
    return render(
        request,
        "public/join_member.html",
        {"submitted": request.method == "POST"},
    )


def join_volunteer(request):
    return render(
        request,
        "public/join_volunteer.html",
        {"submitted": request.method == "POST"},
    )

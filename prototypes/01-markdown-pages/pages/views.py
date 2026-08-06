from django.http import Http404
from django.shortcuts import render

from . import posts


def home(request):
    return render(request, "pages/home.html", {"latest_posts": posts.all_posts()[:3]})


def about(request):
    return render(request, "pages/about.html")


def blog_index(request):
    return render(request, "pages/blog_index.html", {"posts": posts.all_posts()})


def blog_detail(request, slug):
    post = posts.get_post(slug)
    if post is None:
        raise Http404(f"No post with slug {slug!r}")
    return render(request, "pages/blog_detail.html", {"post": post})

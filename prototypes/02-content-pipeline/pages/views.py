from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    return render(request, "pages/home.html", {"latest_posts": Post.objects.all()[:3]})


def about(request):
    return render(request, "pages/about.html")


def blog_index(request):
    return render(request, "pages/blog_index.html", {"posts": Post.objects.all()})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "pages/blog_detail.html", {"post": post})

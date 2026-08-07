from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("systems/", views.systems_index, name="systems_index"),
    path("systems/<slug:slug>/", views.system_detail, name="system_detail"),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("members/<slug:username>/", views.member_detail, name="member_detail"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("systems/", views.systems_index, name="systems_index"),
    path("systems/<slug:slug>/", views.system_detail, name="system_detail"),
    path("members/", views.members_index, name="members_index"),
    path("members/<slug:username>/", views.member_detail, name="member_detail"),
    path("articles/", views.articles_index, name="articles_index"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("about/", views.about, name="about"),
    path("join/", views.join, name="join"),
]

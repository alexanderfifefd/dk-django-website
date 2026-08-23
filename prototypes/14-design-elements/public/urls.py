from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("articles/", views.articles_index, name="articles_index"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("about/", views.about, name="about"),
    path("design-lab/", views.design_lab, name="design_lab"),
    path("join/", views.join, name="join"),
    path("join/account/", views.join_account, name="join_account"),
    path("join/member/", views.join_member, name="join_member"),
    path("join/volunteer/", views.join_volunteer, name="join_volunteer"),
]

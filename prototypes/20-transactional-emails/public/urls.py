from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("join/", views.join, name="join"),
    path("join/follow/", views.join_follow, name="join_follow"),
    path("join/member/", views.join_member, name="join_member"),
    path("join/build/", views.join_build, name="join_build"),
]

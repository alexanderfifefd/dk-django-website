from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("systems/", views.systems_index, name="systems_index"),
    path("systems/<slug:slug>/", views.system_detail, name="system_detail"),
    path("members/", views.members_index, name="members_index"),
    path("members/<slug:username>/", views.member_detail, name="member_detail"),
]

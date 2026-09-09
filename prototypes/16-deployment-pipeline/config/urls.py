from django.urls import include, path

urlpatterns = [
    path("", include("public.urls")),
]

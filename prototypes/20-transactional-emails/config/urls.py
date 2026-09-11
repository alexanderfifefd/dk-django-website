from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path("", include("public.urls")),
]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
        *urlpatterns,
    ]

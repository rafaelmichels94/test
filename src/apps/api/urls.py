from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("settings/", include("apps.api.settings.urls")),
    path("v1/", include("apps.api.healthcheck.urls")),
    path("v1/", include("apps.api.images.urls")),
]

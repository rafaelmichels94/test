from django.urls import path

from apps.api.images.viewsets.list import ImagesViewSet
from apps.api.images.viewsets.retrieve import ImagesRetrieveViewSet 

urlpatterns = [
    path(
        "images/<uuid:pk>/",
        ImagesRetrieveViewSet.as_view(actions={"get": "retrieve", "put": "update"}),
        name="images-get",
    ),
    path(
        "images/",
        ImagesViewSet.as_view(actions={"get": "list"}),
        name="images-list",
    )
]

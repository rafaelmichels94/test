import uuid

from rest_framework.response import Response
from rest_framework import serializers, mixins, status
from apps.domain.models.images.models import Images
from commons.api import viewsets
from apps.api import permissions
from apps.domain import models
from commons.functools import cached_property
from django.shortcuts import get_object_or_404


class ImagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images 
        fields = ["id", "image"]
        read_only_fields = ["id"]

class ImageValidatedSerializer(serializers.Serializer): # noqa
    is_validated = serializers.BooleanField()

class ImagesRetrieveViewSet(viewsets.CreateModelViewSet):
    queryset = models.Images.objects.all()
    permission_classes = [permissions.IsAgent]
    serializer_class = ImagemSerializer

    def create(self, request, *args, **kwargs):
        serializer = ImagemSerializer(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)

        instance = models.Images.objects.create(
            code=serializer.validated_data["code"],
            description=serializer.validated_data["description"],
            quantity=serializer.validated_data["quantity"],
            hide=serializer.validated_data["hide"],
            enable=serializer.validated_data["enable"],
            brand_id=self.request.user.pk,
        )

        serializer = self.get_serializer(
            instance=instance, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

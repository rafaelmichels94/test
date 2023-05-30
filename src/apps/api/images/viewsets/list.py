import uuid

from rest_framework import viewsets 
from rest_framework import serializers
from apps.domain.models.images.models import Images
from commons.api import viewsets
from commons.djutils.api.mixins import FilterQuerysetMixin
from commons.models import filters
from apps.api import permissions


class ImagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images 
        fields = '__all__'

class ImagesViewSet(FilterQuerysetMixin, viewsets.ListModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagemSerializer
    permission_classes = [permissions.IsSupervisor]

    filters = [
        filters.Filter("ids", lookup="pk", cast=uuid.UUID, many=True),
        filters.Filter("is_validated", lookup="is_validated", cast=bool, many=True),
    ]

    def get_queryset(self):
        return super().get_queryset().order_by("-created_at")

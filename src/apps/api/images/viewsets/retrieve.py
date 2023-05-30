import uuid

from rest_framework.response import Response
from rest_framework import viewsets, serializers, mixins, status
from apps.domain.models.images.models import Images
from commons.api import viewsets
from apps.api import permissions
from apps.domain import models
from commons.functools import cached_property
from django.shortcuts import get_object_or_404


class ImagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images 
        fields = '__all__'

class ImageValidatedSerializer(serializers.Serializer): # noqa
    is_validated = serializers.BooleanField()

class ImagesRetrieveViewSet(viewsets.RetrieveModelViewSet, mixins.UpdateModelMixin):
    queryset = models.Images.objects.all()
    permission_classes = [permissions.IsSupervisor]
    serializer_class = ImagemSerializer

    @cached_property
    def image(self):
        return get_object_or_404(models.Images.objects.all(), pk=self.kwargs['pk'])

    def get_queryset(self):
        return super().get_queryset() \
            .filter(pk=self.kwargs['pk'])

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ImageValidatedSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        
        queryset.update_or_create(pk=self.kwargs['pk'], defaults={
            'is_validated': serializer.validated_data['is_validated']
        })

        serializer = ImagemSerializer(instance=self.image, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)

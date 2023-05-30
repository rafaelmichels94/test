from django.utils.translation import gettext_lazy as _
from django.contrib import admin 
from apps.domain import models
from commons.admin.mixins import SmartAdminMixin
from commons.admin.permissions.mixins import PermissionsAdminMixin

@admin.register(models.Images)
class ImagesAdmin(PermissionsAdminMixin, SmartAdminMixin, admin.ModelAdmin):
    list_display = ["id", "image","image_processed", "is_validated"]
    list_filter = ["id", "image", "is_validated"]

    group = _("Administration")

    search_fields = ["is_validated"]

    fieldsets = (
        (None, {"fields": ["image", "image_processed", "is_validated", "inspection"]}),
    )

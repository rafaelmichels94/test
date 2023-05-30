from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models.base import Model


class Images(Model):

    image = models.ImageField(upload_to='images/og/', null=False)
    image_processed = models.ImageField(upload_to='images/processed', null=True)
    is_validated = models.BooleanField(default=False)
    inspection = models.ForeignKey(
        "domain.Inspections",
        verbose_name=_("Inspection"),
        related_name="inspection_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "image"
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

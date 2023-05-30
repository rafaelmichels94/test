from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models.base import Model


class Inspections(Model):

    form = models.ForeignKey(
        "domain.Forms",
        verbose_name=_("Form"),
        related_name="form_inspection",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "inspections"
        verbose_name = _("Inspection")
        verbose_name_plural = _("Inspections")

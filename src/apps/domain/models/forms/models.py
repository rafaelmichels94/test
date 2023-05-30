from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models.base import Model


class Forms(Model):

    date = models.DateTimeField(_("Date"), auto_now_add=True)
    user = models.ForeignKey(
        "domain.User",
        verbose_name=_("User"),
        related_name="user_form",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "forms"
        verbose_name = _("Form")
        verbose_name_plural = _("Forms")

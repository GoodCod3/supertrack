from django.db import models
from django.utils.translation import gettext as _

from supertrack.apps.base_models import BaseModel
from supertrack.helpers.filer import ticket_image_upload_path


class TicketModel(BaseModel):
    image = models.ImageField(
        upload_to=ticket_image_upload_path,
        blank=True,
    )
    total = models.FloatField(_("Total"), default=0.0)
    paid_at = models.DateTimeField(blank=True, null=True)

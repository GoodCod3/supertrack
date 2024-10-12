from django.db import models
from django.utils.translation import gettext as _

from supertrack.apps.base_models import BaseModel
from supertrack.helpers.filer import ticket_image_upload_path


class TicketModel(BaseModel):
    image = models.ImageField(
        upload_to=ticket_image_upload_path,
    )
    total = models.FloatField(_("Total"), default=0.0)
    paid_at = models.DateTimeField(blank=True, null=True)

class TicketProductModel(BaseModel):
    ticket = models.ForeignKey(
        TicketModel,
        on_delete=models.PROTECT,
    )
    name = models.CharField(_("Name"), max_length=200)
    unit_price = models.FloatField(_("Price"), default=0.0)
    total_price = models.FloatField(_("Price"), default=0.0)

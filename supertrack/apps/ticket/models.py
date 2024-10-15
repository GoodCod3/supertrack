from django.db import models
from django.utils.translation import gettext as _

from supertrack.apps.base_models import BaseModel
from supertrack.helpers.filer import ticket_image_upload_path


class TicketModel(BaseModel):
    image = models.FileField(
        upload_to=ticket_image_upload_path,
    )
    total = models.FloatField(_("Total"), default=0.0)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.paid_at} - {self.total}"

class TicketProductModel(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
   
    def __str__(self):
        return self.name
    
class TicketProductRelationshipModel(BaseModel):
    ticket = models.ForeignKey(
        TicketModel,
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        TicketProductModel,
        on_delete=models.PROTECT,
    )
    quantity = models.IntegerField(_("Quantity"), default=0)
    unit_price = models.FloatField(_("Price"), default=0.0)
    total_price = models.FloatField(_("Price"), default=0.0)

    def __str__(self):
        return f"{self.ticket} - {self.product} [Q:{self.quantity} - P:{self.unit_price}]"
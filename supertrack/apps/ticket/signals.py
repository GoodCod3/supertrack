from django.conf import settings

from supertrack.apps.ticket.models import TicketProductModel
from supertrack.apps.ticket.utils.mercadona_ticket_reader import (
    get_mercadona_ticket_info,
)


def register_new_ticket(sender, instance, created, **kwargs):
    if created:
        ticket_info = get_mercadona_ticket_info(instance.image)
        if ticket_info:
            instance.paid_at = ticket_info["purchase_date"]
            instance.total = ticket_info["total"]
            instance.save()

        for product in ticket_info["products"]:
            TicketProductModel.objects.create(
                **{
                    "ticket": instance,
                    "name": product["name"],
                    "quantity": product["quantity"],
                    "unit_price": product["unit_price"],
                    "total_price": product["total_price"],
                }
            )

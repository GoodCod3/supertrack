from supertrack.apps.ticket.models import (
    TicketProductModel,
    TicketProductRelationshipModel,
)
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

        for product_data in ticket_info["products"]:
            product, created = TicketProductModel.objects.get_or_create(
                name=product_data["name"],
            )
            
            TicketProductRelationshipModel.objects.create(
                **{
                    "ticket": instance,
                    "product": product,
                    "quantity": product_data["quantity"],
                    "unit_price": product_data["unit_price"],
                    "total_price": product_data["total_price"],
                }
            )

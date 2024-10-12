from django.conf import settings

from supertrack.apps.ticket.utils.mercadona_ticket_reader import extraer_informacion_ticket



def register_new_ticket(sender, instance, created, **kwargs):
    if created:
        ticket_info = extraer_informacion_ticket(instance.image)
        print("=" * 90)
        print(ticket_info)
        print("=" * 90)




from django.apps import AppConfig
from django.db.models.signals import post_save


class TicketConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "supertrack.apps.ticket"

    def ready(self):
        from supertrack.apps.ticket.models import TicketModel
        from supertrack.apps.ticket.signals import register_new_ticket

        post_save.connect(register_new_ticket, sender=TicketModel)

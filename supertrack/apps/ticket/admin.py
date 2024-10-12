from django.contrib import admin

from supertrack.apps.ticket.models import TicketModel
from supertrack.helpers.admin import BaseModelAdmin


class TicketModelAdmin(BaseModelAdmin):
    model = TicketModel
    empty_value_display = "-empty-"
    list_display = (
        "public_id",
        "paid_at",
    )
    search_fields = ("paid_at",)
    # list_filter = ()


admin.site.register(TicketModel, TicketModelAdmin)
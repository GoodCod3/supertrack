from django.contrib import admin

from supertrack.apps.ticket.models import TicketModel, TicketProductModel
from supertrack.helpers.admin import BaseModelAdmin


class TicketProductModelInline(admin.TabularInline):
    model = TicketProductModel
    extra = 1
    
class TicketProductModelAdmin(BaseModelAdmin):
    model = TicketProductModel
    empty_value_display = "-empty-"
    
    list_display = (
        "public_id",
        "name",
        "unit_price",
        "total_price",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(TicketProductModel, TicketProductModelAdmin)

class TicketModelAdmin(BaseModelAdmin):
    model = TicketModel
    inlines = [
        TicketProductModelInline,
    ]
    empty_value_display = "-empty-"
    list_display = (
        "public_id",
        "paid_at",
        "total",
    )
    search_fields = ("paid_at",)
    # list_filter = ()


admin.site.register(TicketModel, TicketModelAdmin)

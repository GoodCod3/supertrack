from django.contrib import admin

from supertrack.apps.ticket.models import (
    TicketModel,
    TicketProductModel,
    TicketProductRelationshipModel,
)
from supertrack.helpers.admin import BaseModelAdmin


class TicketProductRelationshipModelInline(admin.TabularInline):
    model = TicketProductRelationshipModel
    extra = 1


class TicketProductModelAdmin(BaseModelAdmin):
    model = TicketProductModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)

admin.site.register(TicketProductModel, TicketProductModelAdmin)

class TicketProductRelationshipModelAdmin(BaseModelAdmin):
    model = TicketProductRelationshipModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "ticket",
        "product__name",
        "unit_price",
        "total_price",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(TicketProductRelationshipModel, TicketProductRelationshipModelAdmin)


class TicketModelAdmin(BaseModelAdmin):
    model = TicketModel
    inlines = [
        TicketProductRelationshipModelInline,
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

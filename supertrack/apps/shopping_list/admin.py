from django.utils.safestring import mark_safe
from django.contrib import admin

from supertrack.apps.shopping_list.models import (
    MercadonaShoppingList,
    MercadonaShoppingListProduct,
    ConsumShoppingList,
    ConsumShoppingListProduct,
)
from supertrack.helpers.admin import BaseModelAdmin


class MercadonaShoppingListProductModelInline(admin.TabularInline):
    model = MercadonaShoppingListProduct
    extra = 1


# ======================= Mercadona =======================
class MercadonaShoppingListModelAdmin(BaseModelAdmin):
    model = MercadonaShoppingList
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "user",
    )
    search_fields = ("name",)
    # list_filter = ()
    inlines = [MercadonaShoppingListProductModelInline]


admin.site.register(MercadonaShoppingList, MercadonaShoppingListModelAdmin)

# Consum
class ConsumShoppingListProductModelInline(admin.TabularInline):
    model = ConsumShoppingListProduct
    extra = 1


# ======================= Consum =======================
class ConsumShoppingListModelAdmin(BaseModelAdmin):
    model = ConsumShoppingList
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "user",
    )
    search_fields = ("name",)
    # list_filter = ()
    inlines = [ConsumShoppingListProductModelInline]


admin.site.register(ConsumShoppingList, ConsumShoppingListModelAdmin)

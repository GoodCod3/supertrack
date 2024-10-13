from django.contrib import admin

from supertrack.apps.scrappy.models import (
    MercadonaParentCategoryModel,
    MercadonaCategoryModel,
    MercadonaProductModel,
)
from supertrack.helpers.admin import BaseModelAdmin


class MercadonaProductModelInline(admin.TabularInline):
    model = MercadonaProductModel
    extra = 1

# ======================= Mercadona =======================
class MercadonaParentCategoryModelAdmin(BaseModelAdmin):
    model = MercadonaParentCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(MercadonaParentCategoryModel, MercadonaParentCategoryModelAdmin)

class MercadonaCategoryModelAdmin(BaseModelAdmin):
    model = MercadonaCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(MercadonaCategoryModel, MercadonaCategoryModelAdmin)

class MercadonaProductModelAdmin(BaseModelAdmin):
    model = MercadonaProductModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
        "unit_price",
        "total_price",
        "image",
        "slug",
        "is_new",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(MercadonaProductModel, MercadonaProductModelAdmin)


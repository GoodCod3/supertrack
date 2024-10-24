from django.utils.safestring import mark_safe
from django.contrib import admin

from supertrack.apps.scrappy.models import (
    MercadonaParentCategoryModel,
    MercadonaCategoryModel,
    MercadonaProductModel,
    MercadonaProductCategoryModel,
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

class MercadonaProductCategoryModelAdmin(BaseModelAdmin):
    model = MercadonaProductCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
        "category_image",
    )
    search_fields = ("name", "internal_id")

    def category_image(self, obj):
        try:
            if obj.image:
                return mark_safe(
                    f'<img src="{obj.image}" width="100" height="100"/>'  # noqa: E501
                )
        except ValueError:
            return ""

    category_image.allow_tags = True
    category_image.short_description = "Category image"
    
admin.site.register(MercadonaProductCategoryModel, MercadonaProductCategoryModelAdmin)

class MercadonaProductModelAdmin(BaseModelAdmin):
    model = MercadonaProductModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
        "unit_price",
        "total_price",
        "product_image",
        "slug",
        "is_new",
    )
    search_fields = ("name",)
    list_filter = ("is_new",)

    def product_image(self, obj):
        try:
            return mark_safe(
                f'<img src="{obj.image}" width="100" height="100"/>'  # noqa: E501
            )
        except ValueError:
            return ""

    product_image.allow_tags = True
    product_image.short_description = "Product image"
    
admin.site.register(MercadonaProductModel, MercadonaProductModelAdmin)


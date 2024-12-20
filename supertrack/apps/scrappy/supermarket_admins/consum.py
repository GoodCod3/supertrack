from django.utils.safestring import mark_safe
from django.contrib import admin

from supertrack.apps.scrappy.models import (
    ConsumParentCategoryModel,
    ConsumCategoryModel,
    ConsumProductModel,
    ConsumProductCategoryModel,
)
from supertrack.helpers.admin import BaseModelAdmin


class ConsumProductModelInline(admin.TabularInline):
    model = ConsumProductModel
    extra = 1

# ======================= Consum =======================
class ConsumParentCategoryModelAdmin(BaseModelAdmin):
    model = ConsumParentCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(ConsumParentCategoryModel, ConsumParentCategoryModelAdmin)

class ConsumCategoryModelAdmin(BaseModelAdmin):
    model = ConsumCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(ConsumCategoryModel, ConsumCategoryModelAdmin)

class ConsumProductCategoryModelAdmin(BaseModelAdmin):
    model = ConsumProductCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name", "internal_id")

    
admin.site.register(ConsumProductCategoryModel, ConsumProductCategoryModelAdmin)

class ConsumProductModelAdmin(BaseModelAdmin):
    model = ConsumProductModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "product_image",
        "name",
        "unit_price",
        "parent_category",
        "sub_category",
        "category",
    )
    search_fields = ("name",)
    list_filter = ("category",)

    def product_image(self, obj):
        try:
            return mark_safe(
                f'<img src="{obj.image}" width="100" height="100"/>'  # noqa: E501
            )
        except ValueError:
            return ""

    product_image.allow_tags = True
    product_image.short_description = "Product image"
    def parent_category(self, obj):
        return obj.category.parent_category.parent_category

    parent_category.allow_tags = True
    parent_category.short_description = "Parent category"

    def sub_category(self, obj):
        return obj.category.parent_category.name

    sub_category.allow_tags = True
    sub_category.short_description = "Sub category"
    
admin.site.register(ConsumProductModel, ConsumProductModelAdmin)


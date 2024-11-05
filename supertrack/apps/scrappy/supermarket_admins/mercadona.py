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
        "internal_id",
        "parent_internal_category",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(MercadonaParentCategoryModel, MercadonaParentCategoryModelAdmin)

class MercadonaCategoryModelAdmin(BaseModelAdmin):
    model = MercadonaCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "name",
        "internal_id",
        "parent_category",
        "subcategory_internal_category",
    )
    search_fields = ("name",)
    list_filter = ("parent_category",)


admin.site.register(MercadonaCategoryModel, MercadonaCategoryModelAdmin)

class MercadonaProductCategoryModelAdmin(BaseModelAdmin):
    model = MercadonaProductCategoryModel
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "internal_id",
        "parent_category__parent_category",
        "parent_category",
        "name",
        "parent_category__subcategory_internal_category",
    )
    search_fields = ("name", "internal_id", "parent_category__name")
    list_filter = ("parent_category",)

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
        "product_image",
        "name",
        "unit_price",
        "parent_category",
        "sub_category",
        "category",
    )
    search_fields = ("name",)
    list_filter = ("is_new", "category")

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
    
admin.site.register(MercadonaProductModel, MercadonaProductModelAdmin)


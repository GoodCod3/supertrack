from django.utils.safestring import mark_safe
from django.contrib import admin

from supertrack.apps.scrappy.models import (
    InternalCategory,
    InternalSubCategory,
    InternalSubSubCategory,
    InternalProductCategory,
)
from supertrack.helpers.admin import BaseModelAdmin


# ======================= Parent category =======================
class InternalCategoryModelAdmin(BaseModelAdmin):
    model = InternalCategory
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(InternalCategory, InternalCategoryModelAdmin)

# ======================= Subcategory category =======================
class InternalSubCategoryModelAdmin(BaseModelAdmin):
    model = InternalSubCategory
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
        "parent_category",
    )
    search_fields = ("name",)
    list_filter = ("parent_category",)


admin.site.register(InternalSubCategory, InternalSubCategoryModelAdmin)

# ======================= SubSubcategory category =======================
class InternalSubSubCategoryModelAdmin(BaseModelAdmin):
    model = InternalSubSubCategory
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
        "parent_subcategory",
    )
    search_fields = ("name",)
    # list_filter = ()


admin.site.register(InternalSubSubCategory, InternalSubSubCategoryModelAdmin)

# ======================= Product category =======================
class InternalProductCategoryModelAdmin(BaseModelAdmin):
    model = InternalProductCategory
    empty_value_display = "-empty-"

    list_display = (
        "public_id",
        "name",
    )
    search_fields = ("name",)


admin.site.register(InternalProductCategory, InternalProductCategoryModelAdmin)

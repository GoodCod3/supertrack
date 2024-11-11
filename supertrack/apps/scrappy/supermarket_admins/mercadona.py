from django.utils.safestring import mark_safe
from django.contrib import admin
from django.urls import reverse, path
from django.http import HttpResponseRedirect
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib import messages
from django.shortcuts import render

from supertrack.apps.scrappy.models import (
    MercadonaParentCategoryModel,
    MercadonaCategoryModel,
    MercadonaProductModel,
    MercadonaProductCategoryModel,
)
from supertrack.apps.scrappy.supermarket_admins.forms import CategoryAssignmentForm
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


@admin.action(description='Reassign to a different project')
def assign_category(modeladmin, request, queryset):
    selected_ids = request.POST.getlist(ACTION_CHECKBOX_NAME)
    url = reverse('admin:cat_app_worklog_reassign_project') + f"?ids={','.join(selected_ids)}"
    return HttpResponseRedirect(url)

def assign_product_category_view(request):
    if request.method == "POST":
        print(request.POST)
        form = CategoryAssignmentForm(request.POST)
        if form.is_valid():
            selected_ids = [i for i in
                            request.POST.get('_selected_action').split(',')]
            new_internal_category = form.cleaned_data['category']

            MercadonaProductModel.objects.filter(id__in=selected_ids).update(internal_category=new_internal_category)

            messages.success(request, 'The products category has been assigned successfully.')

            return HttpResponseRedirect(reverse('admin:scrappy_mercadonaproductmodel_changelist'))
        else:
            for field in form:
                for error in field.errors:
                    messages.warning(request, error)
            return HttpResponseRedirect(
                reverse('admin:supertrack_assign_product_category') + f"?ids={request.GET.get('ids')}")

    else:
        ids = request.GET.get('ids', '').split(',')
        queryset = MercadonaProductModel.objects.filter(id__in=ids)
        form = CategoryAssignmentForm(initial={'_selected_action': ','.join(ids)})

        return render(request, 'assign_mercadona_product_category.html', {
            'form': form, 'products': queryset, 'title': 'Assign product category'
        })
        
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
        "internal_category",
    )
    search_fields = ("name",)
    list_filter = ("is_new", "category")
    actions = [assign_category]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('reassign_project/', self.admin_site.admin_view(assign_product_category_view),
                 name="supertrack_assign_product_category"),
        ]
        return custom_urls + urls
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


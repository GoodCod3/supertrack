from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from supertrack.apps.scrappy.models import MercadonaProductModel
from supertrack.apps.shopping_list.models import (
    MercadonaShoppingList,
)


class ShoppingListView(LoginRequiredMixin, TemplateView):
    template_name = "shopping_list_home.html"

    # def _get_current_shopping_list(self):
    #     shopping_list = get_object_or_404(
    #         MercadonaShoppingList, user=self.request.user
    #     )
    #     products = shopping_list.products.select_related("product").all()
    #     total = 0
    #     product_data = []
    #     for product in products:
    #         total_price = product.quantity * product.product.unit_price
    #         total += total_price
    #         product_data.append({
    #             "id": product.product.public_id,
    #             "name": product.product.name,
    #             "price": product.product.unit_price,
    #             "quantity": product.quantity,
    #             "total_price": product.product.unit_price,
    #             "image": product.product.image,
    #         })
        
    #     return {
    #         "total": total,
    #         "products": product_data
    #     }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     mercadona_products = MercadonaProductModel.objects.all()

    #     products = {}
    #     for mercadona_product in mercadona_products:
    #         product_category = mercadona_product.category.parent_category.parent_category.name
    #         if product_category not in products:
    #             products[product_category] = []

    #         products[product_category].append(
    #             {
    #                 "id": mercadona_product.public_id,
    #                 "name": mercadona_product.name,
    #                 "image": mercadona_product.image,
    #                 "price": mercadona_product.unit_price,
    #             }
    #         )

    #     context["products"] = products
    #     context["shopping_list"] = self._get_current_shopping_list()

    #     return context

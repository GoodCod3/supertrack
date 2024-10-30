from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from supertrack.apps.shopping_list.models import (
    MercadonaShoppingList,
    MercadonaShoppingListProduct,
)
from supertrack.apps.scrappy.models import MercadonaProductModel



@require_GET
@login_required
def get_mercadona_products(request):
    if request.user.is_authenticated:
        products = {}
        mercadona_products = MercadonaProductModel.objects.all()[:100]

        for mercadona_product in mercadona_products:
            parent_category = mercadona_product.category.parent_category.parent_category.name
            product_category = mercadona_product.category.parent_category.name
            
            if parent_category not in products:
                products[parent_category] = {}
            
            if product_category not in products[parent_category]:
                products[parent_category][product_category] = []

            products[parent_category][product_category].append(
                {
                    "id": mercadona_product.public_id,
                    "name": mercadona_product.name,
                    "image": mercadona_product.image,
                    "price": mercadona_product.unit_price,
                }
            )
    
        return JsonResponse(products)

    raise Exception("You are not authenticated.")
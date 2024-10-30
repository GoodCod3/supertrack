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
def get_shopping_list(request):
    if request.user.is_authenticated:
        try:
            shopping_list = MercadonaShoppingList.objects.get(user=request.user)
        except MercadonaShoppingList.DoesNotExist:
            return JsonResponse({
                "total": 0,
                "products": []
            })
        else:
            products = shopping_list.products.select_related("product").all()
            total = 0
            product_data = []
            for product in products:
                total_price = product.quantity * product.product.unit_price
                total += total_price
                product_data.append({
                    "id": product.product.public_id,
                    "name": product.product.name,
                    "price": product.product.unit_price,
                    "quantity": product.quantity,
                    "total_price": total_price,
                    "image": product.product.image,
                })
            
            return JsonResponse({
                "total": "{:0.2f}".format(total),
                "products": product_data
            })

    raise Exception("You are not authenticated.")
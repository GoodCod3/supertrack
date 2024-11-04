import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from supertrack.apps.shopping_list.models import (
    ConsumShoppingList,
    MercadonaShoppingList,
    MercadonaShoppingListProduct,
)
from supertrack.apps.scrappy.models import MercadonaProductModel



@require_POST
@login_required
def get_shopping_list(request):
    if request.user.is_authenticated:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        else:
            supermarket = data.get("supermarket")
            
            if supermarket == "mercadona":
                supermarketShoppingList = MercadonaShoppingList
            elif supermarket == "consum":
                supermarketShoppingList = ConsumShoppingList
            else:
                return JsonResponse({"error": "Supermarket does not exist"}, status=400)
            
            try:
                shopping_list = supermarketShoppingList.objects.get(user=request.user)
            except supermarketShoppingList.DoesNotExist:
                return JsonResponse({
                    "total": 0,
                    "products": []
                })
            else:
                products = shopping_list.products.select_related("product").filter(is_deleted=False)
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
                        "total_price":"{:0.2f}".format(total_price) ,
                        "image": product.product.image,
                    })
                
                return JsonResponse({
                    "total": "{:0.2f}".format(total),
                    "products": product_data
                })

    raise Exception("You are not authenticated.")
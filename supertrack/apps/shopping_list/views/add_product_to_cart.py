import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from supertrack.apps.shopping_list.models import (
    MercadonaShoppingList,
    MercadonaShoppingListProduct,
    ConsumShoppingList,
    ConsumShoppingListProduct,
)
from supertrack.apps.scrappy.models import MercadonaProductModel, ConsumProductModel


@require_POST
@login_required
def add_product_to_cart(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        product_id = data.get("productId")
        supermarket = data.get("supermarket")
        if product_id and supermarket:
            if supermarket == "mercadona":
                productModel = MercadonaProductModel
                supermarketShoppingList = MercadonaShoppingList
                supermarketShoppingListProduct = MercadonaShoppingListProduct
            elif supermarket == "consum":
                productModel = ConsumProductModel
                supermarketShoppingList = ConsumShoppingList
                supermarketShoppingListProduct = ConsumShoppingListProduct
            else:
                return JsonResponse({"error": "Supermarket not exist"}, status=400)
                
                
            product = get_object_or_404(productModel, public_id=product_id)
            mercadona_list, created = supermarketShoppingList.objects.get_or_create(
                user=request.user
            )
            shopping_list_product, created = supermarketShoppingListProduct.objects.get_or_create(
                shopping_list=mercadona_list,
                product=product,
                is_deleted=False,
                defaults={"quantity": 1}
            )

            if not created:
                shopping_list_product.quantity += 1
                shopping_list_product.save()
        else:
            return JsonResponse({"error": "Product ID is required"}, status=400)
    return JsonResponse({"status": "success"})

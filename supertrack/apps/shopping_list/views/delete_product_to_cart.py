from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from supertrack.apps.shopping_list.models import (
    MercadonaShoppingList,
    MercadonaShoppingListProduct,
)
from supertrack.apps.scrappy.models import MercadonaProductModel


@require_POST
@login_required
def delete_product_to_cart(request):
    product_id = request.POST.get("product_id")
    if product_id:
        mercadona_list = get_object_or_404(MercadonaShoppingList, user=request.user)
        product_in_list = get_object_or_404(
            MercadonaShoppingListProduct,
            shopping_list=mercadona_list,
            product__public_id=product_id,
        )
        product_in_list.delete()
    else:
        return JsonResponse({"error": "Product ID is required"}, status=400)
    return JsonResponse({"status": "success"})
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
def add_product_to_cart(request):
    product_id = request.POST.get("product_id")
    if product_id:
        product = get_object_or_404(MercadonaProductModel, public_id=product_id)
        mercadona_list, created = MercadonaShoppingList.objects.get_or_create(
            user=request.user
        )
        shopping_list_product, created = MercadonaShoppingListProduct.objects.get_or_create(
            shopping_list=mercadona_list,
            product=product,
            defaults={"quantity": 1}
        )
        if not created:
            shopping_list_product.quantity += 1
            shopping_list_product.save()
    else:
        return JsonResponse({"error": "Product ID is required"}, status=400)
    return JsonResponse({"status": "success"})
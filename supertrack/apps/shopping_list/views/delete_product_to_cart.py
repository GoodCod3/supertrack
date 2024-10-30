import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone

from supertrack.apps.shopping_list.models import (
    MercadonaShoppingList,
    MercadonaShoppingListProduct,
)


@require_POST
@login_required
def delete_product_to_cart(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        product_id = data.get("productId")
        if product_id:
            mercadona_list = get_object_or_404(MercadonaShoppingList, user=request.user)
            product_in_list = get_object_or_404(
                MercadonaShoppingListProduct,
                shopping_list=mercadona_list,
                product__public_id=product_id,
                is_deleted=False,
            )
            product_in_list.is_deleted = True
            product_in_list.deleted_at = timezone.now()
            product_in_list.save()
        else:
            return JsonResponse({"error": "Product ID is required"}, status=400)
    return JsonResponse({"status": "success"})

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
def get_lowest_shopping_list(request):
    if request.user.is_authenticated:
        shopping_list = MercadonaShoppingList.objects.get(user=request.user)
        products = shopping_list.products.select_related("product").filter(is_deleted=False)
        print(products)

    return JsonResponse({"error": "Error"}, status=400)
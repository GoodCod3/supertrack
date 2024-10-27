from django.http import JsonResponse
from django.views.decorators.http import require_POST


@require_POST
def add_product_to_cart(request):
    product_id = request.POST.get("product_id")

    return JsonResponse({"status": "success", "product_id": product_id})

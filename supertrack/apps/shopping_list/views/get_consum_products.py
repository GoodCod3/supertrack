from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from supertrack.apps.scrappy.models import ConsumProductModel



@require_GET
@login_required
def get_consum_products(request):
    if request.user.is_authenticated:
        products = {}
        consum_products = ConsumProductModel.objects.all()[:100]

        for consum_product in consum_products:
            parent_category = consum_product.category.parent_category.parent_category.name
            product_category = consum_product.category.parent_category.name
            
            if parent_category not in products:
                products[parent_category] = {}
            
            if product_category not in products[parent_category]:
                products[parent_category][product_category] = []

            products[parent_category][product_category].append(
                {
                    "id": consum_product.public_id,
                    "name": consum_product.name,
                    "image": consum_product.image,
                    "price": consum_product.unit_price,
                }
            )
    
        return JsonResponse(products)

    raise Exception("You are not authenticated.")
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from supertrack.apps.scrappy.models import MercadonaProductModel


class ShoppingListView(LoginRequiredMixin, TemplateView):
    template_name = "shopping_list_home.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mercadona_products = MercadonaProductModel.objects.all()
        
        products = {}
        for mercadona_product in mercadona_products:
            product_category = mercadona_product.category.parent_category.name
            if product_category not in products:
                products[product_category] = []
            
            products[product_category].append({
                "id": mercadona_product.public_id,
                "name": mercadona_product.name,
                "image": mercadona_product.image,
                "price": mercadona_product.unit_price,
            })
            
        context["products"] = products

        return context

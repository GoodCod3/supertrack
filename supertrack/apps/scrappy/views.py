import requests
import time
from django.views import View
from django.http import JsonResponse

from supertrack.apps.scrappy.models import (
    MercadonaParentCategoryModel,
    MercadonaCategoryModel,
    MercadonaProductCategoryModel,
    MercadonaProductModel,
)


MERCADONA_API_ENDPOINT = "https://tienda.mercadona.es/api/"


class StoreMercadonaProductsView(View):
    def get_parent_categories_from_api(self):
        categories = requests.get(f"{MERCADONA_API_ENDPOINT}/categories/")

        return categories.json() if categories.status_code == 200 else None

    def create_or_update_parent_category(self, data):
        category, created = MercadonaParentCategoryModel.objects.update_or_create(
            internal_id=data['id'],
            defaults={'name': data['name']}
        )
        return category

    def create_or_update_category(self, data, parent_category):
        category, created = MercadonaCategoryModel.objects.update_or_create(
            internal_id=data['id'],
            defaults={
                'name': data['name'],
                'parent_category': parent_category,
            }
        )
        return category

    def create_or_update_product_category(self, data, parent_category):
        category, created = MercadonaProductCategoryModel.objects.update_or_create(
            internal_id=data['id'],
            defaults={
                'name': data['name'],
                'image': data['image'],
                'parent_category': parent_category,
            }
        )
        return category

    def create_or_update_product(self, data, category):
        product, created = MercadonaProductModel.objects.update_or_create(
            internal_id=data['id'],
            defaults={
                'category': category,
                'name': data['display_name'],
                'slug': data['slug'],
                'unit_price': float(data['price_instructions']['unit_price']),
                'total_price': float(data['price_instructions']['reference_price']),
                'image': data['thumbnail'],
                'is_new': data['price_instructions']['is_new'],
            }
        )
        return product

    def fetch_and_store_products(self, category):
        response = requests.get(f"{MERCADONA_API_ENDPOINT}/categories/{category.internal_id}")
        if response.status_code == 200:
            products_data = response.json()

            for category_data in products_data['categories']:
                product_category = self.create_or_update_product_category(category_data, category)
                for product_data in category_data["products"]:
                    self.create_or_update_product(product_data, product_category)


    def sync_categories_and_products(self):
        parent_categories_data = self.get_parent_categories_from_api()
        if parent_categories_data and 'results' in parent_categories_data:
            for category_parent_data in parent_categories_data['results']:
                print(category_parent_data['name'])
                print("=" * 90)
                parent_category = self.create_or_update_parent_category(category_parent_data)
                for category_data in category_parent_data['categories']:
                    # with transaction.atomic():
                    category = self.create_or_update_category(category_data, parent_category)
                    self.fetch_and_store_products(category)
                    time.sleep(0.5)

    def get(self, request, *args, **kwargs):
        success = True
        try:
            self.sync_categories_and_products()
        except Exception as e:
            print(f"Error getting data from Mercadona: {e}")
            success = False

        return JsonResponse({"success": success})


import requests
import time
from django.views import View
from django.http import JsonResponse

from supertrack.apps.scrappy.models import (
    ConsumParentCategoryModel,
    ConsumCategoryModel,
    ConsumProductCategoryModel,
    ConsumProductModel,
)


MERCADONA_API_ENDPOINT = "https://tienda.consum.es/api/rest/V1.0"


class StoreConsumProductsView(View):
    def get_parent_categories_from_api(self):
        categories = requests.get(
            f"{MERCADONA_API_ENDPOINT}/shopping/category/menu/"
        )

        return categories.json() if categories.status_code == 200 else None

    def create_or_update_parent_category(self, data):
        category, created = ConsumParentCategoryModel.objects.update_or_create(
            internal_id=data["id"], defaults={"name": data["name"]}
        )
        return category

    def create_or_update_category(self, data, parent_category):
        category, created = ConsumCategoryModel.objects.update_or_create(
            internal_id=data["id"],
            defaults={
                "name": data["name"],
                "parent_category": parent_category,
            },
        )
        return category

    def create_or_update_product_category(self, data, parent_category):
        category, created = (
            ConsumProductCategoryModel.objects.update_or_create(
                internal_id=data["id"],
                defaults={
                    "name": data["name"],
                    "parent_category": parent_category,
                },
            )
        )
        return category

    def create_or_update_product(self, data, category):
        product, created = MercadonaProductModel.objects.update_or_create(
            internal_id=data["id"],
            defaults={
                "category": category,
                "name": data["display_name"],
                "slug": data["slug"],
                "unit_price": float(data["price_instructions"]["unit_price"]),
                "total_price": float(
                    data["price_instructions"]["reference_price"]
                ),
                "image": data["thumbnail"],
                "is_new": data["price_instructions"]["is_new"],
            },
        )
        return product

    def fetch_and_store_products(
        self,
        product_category,
        selected_page=1,
        selected_offset=0,
    ):
        page = selected_page
        offset = selected_offset
        limit = 20
        all_products = []
        has_more = True
        request_num = 0
        while has_more:
            if request_num > 0 and request_num % 10 == 0:
                print("\t\tWaiting 20 seconds to retreive more products...")
                time.sleep(20)

            params = {
                "page": page,
                "limit": limit,
                "offset": offset,
                "orderById": 5,
                "showRecommendations": "true",
                "categories": product_category.internal_id,
            }
            try:
                response = requests.get(
                    f"{MERCADONA_API_ENDPOINT}/catalog/product", params=params
                )
            except requests.exceptions.RequestException:
                print("\t\t Waiting 1 minute to retry product category...")
                time.sleep(60)
                self.fetch_and_store_products(
                    product_category,
                    selected_page=page,
                    selected_offset=offset,
                )
            else:
                if response.status_code == 200:
                    request_num += 1
                    data = response.json()
                    products = data.get("products", [])
                    all_products.extend(products)
                    has_more = data.get("hasMore", False)
                    total_count = data.get("totalCount", 0)
                    print(
                        f"\t\tFetched {len(products)} products. Total so far: {len(all_products)}/{total_count}"
                    )
                    page += 1
                    offset += limit

                    for product_data in products:
                        internal_id = product_data["id"]
                        name = product_data["productData"]["description"]
                        image = None
                        if product_data["media"]:
                            image = product_data["media"][0]["url"]
                        price = 0
                        discount_price = 0
                        offer_from = None
                        offer_to = None

                        for price_data in product_data["priceData"]["prices"]:
                            if price_data["id"] == "PRICE":
                                price = price_data["value"]["centAmount"]
                            if price_data["id"] == "OFFER_PRICE":
                                discount_price = price_data["value"]["centAmount"]

                        if product_data["offers"]:
                            offer_from = product_data["offers"][0]["from"]
                            offer_to = product_data["offers"][0]["to"]

                        ConsumProductModel.objects.update_or_create(
                            internal_id=internal_id,
                            defaults={
                                "category": product_category,
                                "name": name,
                                "unit_price": price,
                                "offer_price": discount_price,
                                "offer_from": offer_from,
                                "offer_to": offer_to,
                                "image": image,
                            },
                        )

        return all_products

        # for category_data in products_data['categories']:
        #     for product_data in category_data["products"]:
        #         self.create_or_update_product(product_data, product_category)

    def sync_categories_and_products(self):
        parent_categories_data = self.get_parent_categories_from_api()
        if parent_categories_data:
            for category_parent_data in parent_categories_data:
                # if category_parent_data["id"] != 2811:
                #     continue
               

                print(f'{category_parent_data["name"]} - {category_parent_data["id"]}')
                parent_category = self.create_or_update_parent_category(
                    category_parent_data
                )
                for category_data in category_parent_data["subcategories"]:
                    # if category_data["id"] != 2055:
                    #     continue
                    category = self.create_or_update_category(
                        category_data, 
                        parent_category,
                    )
                    print(f"\t{category_data['name']}")
                    if len(category_data["subcategories"]) > 0:
                        for product_category_data in category_data["subcategories"]:
                            # if product_category_data["id"] != 2064:
                            #     continue
                            print(f"\t\t {product_category_data['name']}")
                            product_category = (
                                self.create_or_update_product_category(
                                    product_category_data, 
                                    category
                                )
                            )
                            # import ipdb; ipdb.set_trace()
                            self.fetch_and_store_products(product_category)
                            print("Waiting 10 seconds to retreive next category...")
                            time.sleep(10)
                    else:
                        # Just two categories
                        print(f"\t\t {category_data['name']}")
                        product_category = (
                            self.create_or_update_product_category(
                                category_data, 
                                category
                            )
                        )
                        self.fetch_and_store_products(product_category)
                        print("Waiting 10 seconds to retreive next category...")
                        time.sleep(10)
                        

    def get(self, request, *args, **kwargs):
        success = True
        self.sync_categories_and_products()
        try:
            pass
        except Exception as e:
            print(f"Error getting data from Consum: {e}")
            success = False

        return JsonResponse({"success": success})

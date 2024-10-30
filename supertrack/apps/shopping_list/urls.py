from django.urls import path

from supertrack.apps.shopping_list.views.ShoppingList import ShoppingListView
from supertrack.apps.shopping_list.views.add_product_to_cart import add_product_to_cart
from supertrack.apps.shopping_list.views.delete_product_to_cart import delete_product_to_cart
from supertrack.apps.shopping_list.views.get_mercadona_products import get_mercadona_products
from supertrack.apps.shopping_list.views.get_shopping_list import get_shopping_list


urlpatterns = [
    path(
        "",
        ShoppingListView.as_view(),
        name="shopping_list__home",
    ),
    path(
        "add-to-cart/",
        add_product_to_cart,
        name="shopping_list__add_cart",
    ),
    path(
        "mercadona/products/",
        get_mercadona_products,
        name="shopping_list__get_products",
    ),
    path(
        "delete-product-cart/",
        delete_product_to_cart,
        name="shopping_list__delete_cart",
    ),
    path(
        "mercadona/",
        get_shopping_list,
        name="shopping_list__get_list",
    ),

]

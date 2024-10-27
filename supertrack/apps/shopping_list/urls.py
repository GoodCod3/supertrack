from django.urls import path

from supertrack.apps.shopping_list.views.ShoppingList import ShoppingListView
from supertrack.apps.shopping_list.views.add_product_to_cart import add_product_to_cart

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

]

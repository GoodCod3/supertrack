from django.urls import path

from supertrack.apps.scrappy.views.mercadona import StoreMercadonaProductsView
from supertrack.apps.scrappy.views.consum import StoreConsumProductsView


urlpatterns = [
    path(
        "store/mercadona/products/",
        StoreMercadonaProductsView.as_view(),
        name="mercadona__store_products",
    ),
    path(
        "store/consum/products/",
        StoreConsumProductsView.as_view(),
        name="consum__store_products",
    ),
]

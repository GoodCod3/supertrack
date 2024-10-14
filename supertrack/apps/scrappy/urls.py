from django.urls import path

from supertrack.apps.scrappy.views import StoreMercadonaProductsView

urlpatterns = [
    path(
        "store/mercadona/products/",
        StoreMercadonaProductsView.as_view(),
        name="mercadona__store_products",
    ),
]

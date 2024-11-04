from django.db import models
from django.contrib.auth.models import User

from supertrack.apps.base_models import BaseModel


class MercadonaShoppingList(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user.email

class MercadonaShoppingListProduct(BaseModel):
    shopping_list = models.ForeignKey(
        MercadonaShoppingList,
        on_delete=models.PROTECT,
        related_name="products",
    )
    product = models.ForeignKey(
        "scrappy.MercadonaProductModel",
        on_delete=models.PROTECT,
    )
    quantity = models.IntegerField("Quantity", default=1)

    def __str__(self):
        return f"{self.shopping_list} - {self.product}"

# Consum
class ConsumShoppingList(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user.email

class ConsumShoppingListProduct(BaseModel):
    shopping_list = models.ForeignKey(
        ConsumShoppingList,
        on_delete=models.PROTECT,
        related_name="products",
    )
    product = models.ForeignKey(
        "scrappy.ConsumProductModel",
        on_delete=models.PROTECT,
    )
    quantity = models.IntegerField("Quantity", default=1)

    def __str__(self):
        return f"{self.shopping_list} - {self.product}"
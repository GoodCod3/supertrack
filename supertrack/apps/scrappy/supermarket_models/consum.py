from django.db import models
from django.utils.translation import gettext as _

from supertrack.apps.base_models import BaseModel
from supertrack.helpers.filer import (
    consum_product_image_upload_path,
    consum_category_product_image_upload_path,
)


class ConsumParentCategoryModel(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)

    def __str__(self):
        return self.name
    
class ConsumCategoryModel(BaseModel):
    parent_category = models.ForeignKey(
        ConsumParentCategoryModel,
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)

    def __str__(self):
        return self.name

class ConsumProductCategoryModel(BaseModel):
    parent_category = models.ForeignKey(
        ConsumCategoryModel,
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)


    def __str__(self):
        return f"{self.parent_category} - {self.name}"

class ConsumProductModel(BaseModel):
    category = models.ForeignKey(
        ConsumProductCategoryModel,
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)
    unit_price = models.FloatField(_("Price"), default=0.0)
    image = models.URLField(
        _("Image"),
        max_length=500,
        blank=True,
        null=True
    )
    offer_price = models.FloatField(_("Total Price"), default=0.0)
    offer_from = models.DateTimeField(blank=True, null=True)
    offer_to = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.name}"

from django.db import models
from django.utils.translation import gettext as _

from supertrack.apps.base_models import BaseModel


class MercadonaParentCategoryModel(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)
    parent_internal_category = models.ForeignKey(
        "scrappy.InternalCategory",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
      ordering = ['name']


class MercadonaCategoryModel(BaseModel):
    parent_category = models.ForeignKey(
        MercadonaParentCategoryModel,
        on_delete=models.PROTECT,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)
    subcategory_internal_category = models.ForeignKey(
        "scrappy.InternalSubCategory",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f"{self.name} ({self.parent_category.name})"
    
    class Meta:
      ordering = ['name']

class MercadonaProductCategoryModel(BaseModel):
    parent_category = models.ForeignKey(
        MercadonaCategoryModel,
        on_delete=models.PROTECT,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)
    image = models.URLField(
        _("Image"),
        max_length=500,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.parent_category.parent_category} -> {self.parent_category} -> {self.name}"

    class Meta:
        ordering = ("name",)
        
class MercadonaProductModel(BaseModel):
    category = models.ForeignKey(
        MercadonaProductCategoryModel,
        on_delete=models.PROTECT,
    )
    internal_category = models.ForeignKey(
        "scrappy.InternalProductCategory",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.CharField(_("Internal ID"), max_length=100)
    unit_price = models.FloatField(_("Price"), default=0.0)
    total_price = models.FloatField(_("Total Price"), default=0.0)
    image = models.URLField(
        _("Image"),
        max_length=500,
        blank=True,
        null=True,
    )
    slug = models.SlugField(_("Slug"), max_length=400)
    is_new = models.BooleanField(_("Is new"), default=False)

    def __str__(self):
        return f"{self.category} - {self.name}"

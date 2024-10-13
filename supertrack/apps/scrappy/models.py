from django.db import models
from django.utils.translation import gettext as _

from supertrack.apps.base_models import BaseModel
from supertrack.helpers.filer import mercadona_product_image_upload_path


class MercadonaParentCategoryModel(BaseModel):
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.IntegerField(_("Internal ID"))


class MercadonaCategoryModel(BaseModel):
    parent_category = models.ForeignKey(
        MercadonaParentCategoryModel,
        on_delete=models.PROTECT,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.IntegerField(_("Internal ID"))

class MercadonaProductModel(BaseModel):
    category = models.ForeignKey(
        MercadonaCategoryModel,
        on_delete=models.PROTECT,
    )
    name = models.CharField(_("Name"), max_length=200)
    internal_id = models.IntegerField(_("Internal ID"))
    unit_price = models.FloatField(_("Price"), default=0.0)
    total_price = models.FloatField(_("Price"), default=0.0)
    image = models.ImageField(_("Image"),upload_to=mercadona_product_image_upload_path)
    slug = models.SlugField(_("Slug"))
    is_new = models.BooleanField(_("Is new"), default=False)

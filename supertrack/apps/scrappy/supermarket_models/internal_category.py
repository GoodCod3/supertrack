from django.db import models

from supertrack.apps.base_models import BaseModel


class InternalCategory(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InternalSubCategory(BaseModel):
    parent_category = models.ForeignKey(
        InternalCategory,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.parent_category.name} > {self.name}"


class InternalSubSubCategory(BaseModel):
    parent_subcategory = models.ForeignKey(
        InternalSubCategory,
        on_delete=models.CASCADE,
        related_name="subsubcategories",
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.parent_subcategory.parent_category.name} > {self.parent_subcategory.name} > {self.name}"


class InternalProductCategory(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

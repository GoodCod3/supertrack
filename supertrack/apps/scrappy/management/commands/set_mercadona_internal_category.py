from django.core.management.base import BaseCommand, CommandError

from supertrack.apps.scrappy.models import (
    MercadonaParentCategoryModel,
    MercadonaCategoryModel,
    InternalCategory,
    InternalSubCategory,
)


class Command(BaseCommand):
    help = "Create internal categories and subcategories"

    def handle(self, *args, **options):
        """
        Principal keys represent the parent category,
        subcategories key represent supermarket subcategory name
        and the value the internal category name.
        """
        categories_map = {
            "Aceite, especias y salsas": {
                "category": "Despensa",
                "subcategories": {
                    "Aceite, vinagre y sal": "Aceites y condimentos",
                    "Especias": "Aceites y condimentos",
                    "Mayonesa, ketchup y mostaza": "Conservas y salsas",
                    "Otras salsas": "Conservas y salsas",
                },
            },
            "Agua y refrescos": {
                "category": "Bebidas",
                "subcategories": {
                    "Agua": "Agua y refrescos",
                    "Isotónico y energético": "Isotónicas y energéticas",
                    "Refresco de cola": "Gaseosas y sodas",
                    "Refresco de naranja y de limón": "Gaseosas y sodas",
                    "Refresco de té y sin gas": "Gaseosas y sodas",
                    "Tónica y bitter": "Gaseosas y sodas",
                },
            },
        }

        # for c in MercadonaParentCategoryModel.objects.all():
        #     c.parent_internal_category = None
        #     c.save()
        # for c in MercadonaCategoryModel.objects.all():
        #     c.subcategory_internal_category = None
        #     c.save()

        for (
            parent_category_name,
            parent_category_data,
        ) in categories_map.items():
            parent_category = MercadonaParentCategoryModel.objects.get(
                name=parent_category_name
            )

            internal_parent_category = InternalCategory.objects.get(
                name=parent_category_data["category"]
            )

            parent_category.parent_internal_category = internal_parent_category
            parent_category.save()

            for (
                supermarket_subcategory_name,
                subcategory_internal_name,
            ) in parent_category_data["subcategories"].items():
                supermarket_subcategory = MercadonaCategoryModel.objects.get(
                    parent_category=parent_category,
                    name=supermarket_subcategory_name,
                )
                internal_subcategory = InternalSubCategory.objects.get(
                    parent_category=internal_parent_category,
                    name=subcategory_internal_name,
                )
                
                supermarket_subcategory.subcategory_internal_category = internal_subcategory
                supermarket_subcategory.save()
                

        self.stdout.write(self.style.SUCCESS("Successfully created."))

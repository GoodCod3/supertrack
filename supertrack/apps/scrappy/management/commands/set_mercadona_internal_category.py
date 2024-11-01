from pprint import pprint
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
                    "Mayonesa, ketchup y mostaza": "Salsas",
                    "Otras salsas": "Salsas",
                },
            },
            "Agua y refrescos": {
                "category": "Bebidas",
                "subcategories": {
                    "Agua": "Agua",
                    "Isotónico y energético": "Isotónicas y energéticas",
                    "Refresco de cola": "Refrescos",
                    "Refresco de naranja y de limón": "Refrescos",
                    "Refresco de té y sin gas": "Gaseosas y sodas",
                    "Tónica y bitter": "Gaseosas y sodas",
                },
            },
            "Aperitivos": {
                "category": "Despensa",
                "subcategories": {
                    "Aceitunas y encurtidos": "Frutos secos y aperitivos",
                    "Frutos secos y fruta desecada": "Frutos secos y aperitivos",
                    "Patatas fritas y snacks": "Frutos secos y aperitivos",
                },
            },
            "Arroz, legumbres y pasta": {
                "category": "Despensa",
                "subcategories": {
                    "Arroz": "Arroz",
                    "Legumbres": "Legumbres",
                    "Pasta y fideos": "Pastas",
                },
            },
            "Azúcar, caramelos y chocolate": {
                "category": "Despensa",
                "subcategories": {
                    "Azúcar y edulcorante": "Desayuno y dulces",
                    "Chicles y caramelos": "Desayuno y dulces",
                    "Chocolate": "Desayuno y dulces",
                    "Golosinas": "Desayuno y dulces",
                    "Mermelada y miel": "Desayuno y dulces",
                    "Turrones": "Desayuno y dulces",
                },
            },
            "Bebé": {
                "category": "Infantil",
                "subcategories": {
                    "Alimentación infantil": "Alimentación infantil",
                    "Biberón y chupete": "Higiene y cuidado del bebé",
                    "Higiene y cuidado": "Higiene y cuidado del bebé",
                    "Toallitas y pañales": "Higiene y cuidado del bebé",
                },
            },
            "Bodega": {
                "category": "Bebidas",
                "subcategories": {
                    "Cerveza": "Cerveza",
                    "Cerveza sin alcohol": "Cerveza",
                    "Licores": "Vinos y licores",
                    "Sidra y cava": "Vinos y licores",
                    "Tinto de verano y sangría": "Vinos y licores",
                    "Vino blanco": "Vinos y licores",
                    "Vino lambrusco y espumoso": "Vinos y licores",
                    "Vino rosado": "Vinos y licores",
                    "Vino tinto": "Vinos y licores",
                },
            },
            "Cacao, café e infusiones": {
                "category": "Despensa",
                "subcategories": {
                    "Cacao soluble y chocolate a la taza": "Café",
                    "Café cápsula y monodosis": "Café",
                    "Café molido y en grano": "Café",
                    "Café soluble y otras bebidas": "Café",
                    "Té e infusiones": "Té",
                },
            },
            "Carne": {
                "category": "Frescos",
                "subcategories": {
                    "Arreglos": "Carnes frescas",
                    "Aves y pollo": "Carnes frescas",
                    "Carne congelada": {
                        "parent_category": {
                            "name": "Congelados",
                        },
                        "subcategory": "Carne congelada",
                    },
                    "Cerdo": "Carnes frescas",
                    "Conejo y cordero": "Carnes frescas",
                    "Embutido": "Embutidos",
                    "Empanados y elaborados": "Empanados y elaborados",
                    "Hamburguesas y picadas": "Carnes frescas",
                    "Vacuno": "Carnes frescas",
                },
            },
            "Cereales y galletas": {
                "category": "Despensa",
                "subcategories": {
                    "Cereales": "Desayuno y dulces",
                    "Galletas": "Desayuno y dulces",
                    "Tortitas": "Desayuno y dulces",
                },
            },
            "Charcutería y quesos": {
                "category": "Frescos",
                "subcategories": {
                    "Aves y jamón cocido": "Embutidos",
                    "Bacón y salchichas": "Embutidos",
                    "Chopped y mortadela": "Embutidos",
                    "Embutido curado": "Embutidos",
                    "Jamón serrano": "Embutidos",
                    "Paté y sobrasada": "Embutidos",
                    "Queso curado, semicurado y tierno": {
                        "parent_category": {
                            "name": "Lácteos y huevos",
                        },
                        "subcategory": "Quesos",
                    },
                    "Queso lonchas, rallado y en porciones": {
                        "parent_category": {
                            "name": "Lácteos y huevos",
                        },
                        "subcategory": "Quesos",
                    },
                    "Queso untable y fresco": {
                        "parent_category": {
                            "name": "Lácteos y huevos",
                        },
                        "subcategory": "Quesos",
                    },
                },
            },
            "Congelados": {
                "category": "Congelados", 
                "subcategories": {
                    "Arroz y pasta": "Arroz, pastas y legumbres",
                    "Carne": "Carne congelada",
                    "Helados": "Helados y postres congelados",
                    "Hielo": "Hielo",
                    "Marisco": "Pescado congelado",
                    "Pescado": "Pescado congelado",
                    "Pizzas": "Pizzas y bases congeladas",
                    "Rebozados": "Rebozados",
                    "Tartas y churros": "Helados y postres congelados",
                    "Verdura": "Verduras congeladas",
                },
            },
            # "": {"category": "", "subcategories": {}},
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
            try:
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
                    
                    original_internal_parent_category = internal_parent_category
                    
                    if isinstance(subcategory_internal_name, dict):
                        original_internal_parent_category = InternalCategory.objects.get(
                            name=subcategory_internal_name["parent_category"][
                                "name"
                            ]
                        )
                       
                        try:
                            internal_subcategory = InternalSubCategory.objects.get(
                                parent_category=original_internal_parent_category,
                                name=subcategory_internal_name["subcategory"],
                            )
                        except InternalSubCategory.DoesNotExist:
                            import ipdb; ipdb.set_trace()
                            print()
                            
                    else:
                        try:
                            internal_subcategory = InternalSubCategory.objects.get(
                                parent_category=original_internal_parent_category,
                                name=subcategory_internal_name,
                            )
                        except InternalSubCategory.DoesNotExist:
                            import ipdb; ipdb.set_trace()
                            print()

                    supermarket_subcategory = MercadonaCategoryModel.objects.get(
                        parent_category=parent_category,
                        name=supermarket_subcategory_name,
                    )

                    supermarket_subcategory.subcategory_internal_category = (
                        internal_subcategory
                    )
                    supermarket_subcategory.save()
            except Exception as e:
                print(e)
                print(parent_category_name)
                pprint(parent_category_data)
                break
                

        self.stdout.write(self.style.SUCCESS("Successfully created."))

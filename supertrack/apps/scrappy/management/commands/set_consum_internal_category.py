from pprint import pprint
from django.core.management.base import BaseCommand, CommandError

from supertrack.apps.scrappy.models import (
    ConsumParentCategoryModel,
    ConsumCategoryModel,
    ConsumProductCategoryModel,
    InternalCategory,
    InternalSubCategory,
)


class Command(BaseCommand):
    help = "Create internal categories and subcategories"

    def add_arguments(self, parser):
        parser.add_argument(
            "--print-supermarket-categories",
            action="store_true",
            help="Print all categories and subcategories with initial structure to mapping",
        )

        parser.add_argument(
            "--clean-mapping",
            action="store_true",
            help="Remove all internal categories relationships",
        )

    def print_initial_structure_to_mapping(self):
        # Getting initial structure for supermarket categories and
        # subcategories.
        all_subcategories = ConsumProductCategoryModel.objects.all()
        allcategories_structure = {}
        for subcategory in all_subcategories:
            principal_parent_category = (
                subcategory.parent_category.parent_category.name
            )
            second_parent_category = subcategory.parent_category.name

            if principal_parent_category not in allcategories_structure:
                allcategories_structure[principal_parent_category] = {}

            if (
                second_parent_category
                not in allcategories_structure[principal_parent_category]
            ):
                allcategories_structure[principal_parent_category][second_parent_category] = []
            
            allcategories_structure[principal_parent_category][second_parent_category].append(subcategory.name)

        print(allcategories_structure)

    def clean_internal_categories_relationship(self):
        for c in ConsumParentCategoryModel.objects.all():
            c.parent_internal_category = None
            c.save()

        for c in ConsumCategoryModel.objects.all():
            c.subcategory_internal_category = None
            c.save()

    def handle(self, *args, **options):
        """
        Principal keys represent the parent category,
        subcategories key represent supermarket subcategory name
        and the value the internal category name.
        """
        categories_map = {
            "Bazar": {
                "category": "Limpieza y hogar",
                "subcategories": {
                    "Conservación alimentos y moldes": "Menaje y utensilios",
                    "Desechables": "Menaje y utensilios",
                    "Jardin y exterior": "Jardin y exterior",
                    "Libros": {
                        "parent_category": {
                            "name": "Bazar",
                        },
                        "subcategory": "Libros y artículos de oficina",
                    },
                    "Menaje": "Menaje y utensilios",
                    "Pilas": "Accesorios y utensilios de limpieza",
                    "Prepara la Navidad": "Accesorios y utensilios de limpieza",
                    "Promocionales": "Menaje y utensilios",
                    "Velas": {
                        "parent_category": {
                            "name": "Panadería y pastelería",
                        },
                        "subcategory": "Otros",
                    },
                },
            },
            "Bebidas": {
                "category": "Bebidas",
                "subcategories": {
                    "Aguas": "Agua",
                    "Cavas y sidras": "Vinos y licores",
                    "Cervezas": "Cerveza",
                    "Gaseosas y sodas": "Gaseosas y sodas",
                    "Isotónicas y energéticas": "Isotónicas y energéticas",
                    "Licores": "Vinos y licores",
                    "Refrescos": "Refrescos",
                    "Sangrías y combinados base vino": "Vinos y licores",
                    "Vinos": "Vinos y licores",
                    "Zumos y néctares": "Zumos y néctares",
                },
            },
            "Congelados y helados": {
                "category": "Congelados",
                "subcategories": {
                    "Carnes": "Carne congelada",
                    "Frutas y Verduras": "Verduras congeladas",
                    "Helados": "Helados y postres congelados",
                    "Hielo": "Hielo",
                    "Pan, churros y porras": "Helados y postres congelados",
                    "Pescados y mariscos": "Pescado congelado",
                    "Pizza y bases congeladas": "Pizzas y bases congeladas",
                    "Platos preparados": "Arroz, pastas y legumbres",
                    "Rebozados": "Rebozados",
                },
            },
            "Cuidado personal": {
                "category": "Higiene y cuidado personal",
                "subcategories": {
                    "Accesorios y complementos": "Cuidado facial y corporal",
                    "Afeitado y cuidado masculino": "Afeitado y cuidado para hombre",
                    "Colonias y perfumes": "Desodorantes y perfumes",
                    "Cuidado corporal": "Cuidado facial y corporal",
                    "Cuidado del cabello": "Cuidado del cabello",
                    "Cuidado facial": "Cuidado facial y corporal",
                    "Cuidado manos y pies": "Manicura y pedicura",
                    "Depilación": "Depilación",
                    "Desodorante": "Desodorantes y perfumes",
                    "Higiene bucal": "Higiene bucal",
                    "Higiene corporal": "Cuidado facial y corporal",
                    "Higiene íntima": "Higiene íntima",
                    "Maquillaje": "Maquillaje",
                    "Parafarmacia": {
                        "parent_category": {
                            "name": "Parafarmacia",
                        },
                        "subcategory": "Parafarmacia",
                    },
                    "Solares": "Cuidado facial y corporal",
                },
            },
            "Despensa": {
                "category": "Despensa",
                "subcategories": {
                    "Aperitivos y frutos secos": "Frutos secos y aperitivos",
                    "Arroz, pastas, legumbres": "",
                    "Caldos, sopas y purés": "",
                    "Cocina internacional": "",
                    "Conservas, aceites y condimentos": "",
                    "Desayuno, dulces y café": "",
                    "Harina, levadura y pan rallado": "",
                    "Lácteos y huevos": "",
                    "Nutrición y dietética": "",
                    "Panes y tostadas": "",
                    "Turrones y Dulces de Navidad": "",
                },
            },
            "Droguería y limpieza": {
                "category": "",
                "subcategories": {
                    "Accesorios y utensilios limpieza": "",
                    "Ambientadores": "",
                    "Celulosa": "",
                    "Cuidado ropa": "",
                    "Insecticidas": "",
                    "Limpieza baños": "",
                    "Limpieza calzado y accesorios": "",
                    "Limpieza cocina": "",
                    "Limpieza hogar": "",
                },
            },
            "Ecológico y saludable": {
                "category": "",
                "subcategories": {
                    "Cuidado personal": "",
                    "Despensa": "",
                    "Frescos y refrigerados": "",
                },
            },
            "Frescos": {
                "category": "",
                "subcategories": {
                    "Carnicería": "",
                    "Carnicería corte": "",
                    "Charcutería": "",
                    "Charcutería corte": "",
                    "Frutas": "",
                    "Pescadería": "",
                    "Quesos": "",
                    "Quesos corte": "",
                    "Verduras": "",
                },
            },
            "Horno": {
                "category": "",
                "subcategories": {
                    "Bollería dulce": "",
                    "Bollería salada": "",
                    "Pan de horno": "",
                    "Pan de molde y rebanado": "",
                    "Pan hamburguesas y perritos": "",
                    "Pan rallado": "",
                    "Rosquilletas, picos y snacks": "",
                    "Tartas y repostería": "",
                },
            },
            "Infantil": {
                "category": "",
                "subcategories": {
                    "Alimentación infantil": "",
                    "Higiene": "",
                    "Leches infantiles": "",
                    "Pañales": "",
                    "Puericultura": "",
                },
            },
            "Mascotas": {
                "category": "",
                "subcategories": {
                    "Accesorios": "",
                    "Gatos": "",
                    "Otras mascotas": "",
                    "Perros": "",
                },
            },
            "Platos preparados": {
                "category": "",
                "subcategories": {
                    "Preparados en conserva": "",
                    "Preparados refrigerados": "",
                },
            },
        }
        if options["print_supermarket_categories"]:
            self.print_initial_structure_to_mapping()
        elif options["clean_mapping"]:
            self.clean_internal_categories_relationship()
        else:
            for (
                parent_category_name,
                parent_category_data,
            ) in categories_map.items():
                try:
                    parent_category = ConsumParentCategoryModel.objects.get(
                        name=parent_category_name
                    )

                    try:
                        internal_parent_category = (
                            InternalCategory.objects.get(
                                name=parent_category_data["category"]
                            )
                        )
                    except InternalCategory.DoesNotExist:
                        import ipdb

                        ipdb.set_trace()
                        print()

                    parent_category.parent_internal_category = (
                        internal_parent_category
                    )
                    parent_category.save()

                    for (
                        supermarket_subcategory_name,
                        subcategory_internal_name,
                    ) in parent_category_data["subcategories"].items():

                        original_internal_parent_category = (
                            internal_parent_category
                        )

                        if isinstance(subcategory_internal_name, dict):
                            try:
                                original_internal_parent_category = (
                                    InternalCategory.objects.get(
                                        name=subcategory_internal_name[
                                            "parent_category"
                                        ]["name"]
                                    )
                                )
                            except InternalCategory.DoesNotExist:
                                import ipdb

                                ipdb.set_trace()
                                print()

                            try:
                                internal_subcategory = InternalSubCategory.objects.get(
                                    parent_category=original_internal_parent_category,
                                    name=subcategory_internal_name[
                                        "subcategory"
                                    ],
                                )
                            except InternalSubCategory.DoesNotExist:
                                import ipdb

                                ipdb.set_trace()
                                print()

                        else:
                            try:
                                internal_subcategory = InternalSubCategory.objects.get(
                                    parent_category=original_internal_parent_category,
                                    name=subcategory_internal_name,
                                )
                            except InternalSubCategory.DoesNotExist:
                                import ipdb

                                ipdb.set_trace()
                                print()

                        supermarket_subcategory = (
                            ConsumCategoryModel.objects.get(
                                parent_category=parent_category,
                                name=supermarket_subcategory_name,
                            )
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

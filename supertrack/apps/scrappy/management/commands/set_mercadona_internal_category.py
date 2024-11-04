from pprint import pprint
from django.core.management.base import BaseCommand, CommandError

from supertrack.apps.scrappy.models import (
    MercadonaParentCategoryModel,
    MercadonaCategoryModel,
    MercadonaProductCategoryModel,
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
        all_subcategories = MercadonaProductCategoryModel.objects.all()
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
        for c in MercadonaParentCategoryModel.objects.all():
            c.parent_internal_category = None
            c.save()

        for c in MercadonaCategoryModel.objects.all():
            c.subcategory_internal_category = None
            c.save()

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
            "Conservas, caldos y cremas": {
                "category": "Despensa",
                "subcategories": {
                    "Atún y otras conservas de pescado": "Conservas",
                    "Berberechos y mejillones": "Conservas",
                    "Conservas de verdura y frutas": "Conservas",
                    "Gazpacho y cremas": "Conservas",
                    "Sopa y caldo": "Conservas",
                    "Tomate": "Conservas",
                },
            },
            "Cuidado del cabello": {
                "category": "Higiene y cuidado personal",
                "subcategories": {
                    "Acondicionador y mascarilla": "Cuidado del cabello",
                    "Champú": "Cuidado del cabello",
                    "Coloración cabello": "Cuidado del cabello",
                    "Fijación cabello": "Cuidado del cabello",
                },
            },
            "Cuidado facial y corporal": {
                "category": "Higiene y cuidado personal",
                "subcategories": {
                    "Afeitado y cuidado para hombre": "Afeitado y cuidado para hombre",
                    "Cuidado corporal": "Cuidado facial y corporal",
                    "Cuidado e higiene facial": "Cuidado facial y corporal",
                    "Depilación": "Depilación",
                    "Desodorante": "Desodorantes y perfumes",
                    "Gel y jabón de manos": "Cuidado facial y corporal",
                    "Higiene bucal": "Higiene bucal",
                    "Higiene íntima": "Higiene íntima",
                    "Manicura y pedicura": "Manicura y pedicura",
                    "Perfume y colonia": "Desodorantes y perfumes",
                    "Protector solar y aftersun": "Cuidado facial y corporal",
                },
            },
            "Fitoterapia y parafarmacia": {
                "category": "Parafarmacia",
                "subcategories": {
                    "Fitoterapia": "Fitoterapia",
                    "Parafarmacia": "Parafarmacia",
                },
            },
            "Fruta y verdura": {
                "category": "Frescos",
                "subcategories": {
                    "Fruta": "Verduras y frutas",
                    "Lechuga y ensalada preparada": "Verduras y frutas",
                    "Verdura": "Verduras y frutas",
                },
            },
            "Huevos, leche y mantequilla": {
                "category": "Lácteos y huevos",
                "subcategories": {
                    "Huevos": "Huevos",
                    "Leche y bebidas vegetales": "Leche y bebidas vegetales",
                    "Mantequilla y margarina": "Mantequilla y margarina",
                },
            },
            "Limpieza y hogar": {
                "category": "Limpieza y hogar",
                "subcategories": {
                    "Detergente y suavizante ropa": "Detergentes y limpieza",
                    "Estropajo, bayeta y guantes": "Accesorios y utensilios de limpieza",
                    "Insecticida y ambientador": "Insecticidas y ambientadores",
                    "Lejía y líquidos fuertes": "Limpiahogar y friegasuelos",
                    "Limpiacristales": "Limpieza muebles y multiusos",
                    "Limpiahogar y friegasuelos": "Limpiahogar y friegasuelos",
                    "Limpieza baño y WC": "Limpieza baño",
                    "Limpieza cocina": "Limpieza cocina",
                    "Limpieza muebles y multiusos": "Limpieza muebles y multiusos",
                    "Limpieza vajilla": "Limpieza vajilla",
                    "Menaje y conservación de alimentos": "Menaje y utensilios",
                    "Papel higiénico y celulosa": "Celulosa y papel higiénico",
                    "Pilas y bolsas de basura": "Accesorios y utensilios de limpieza",
                    "Utensilios de limpieza y calzado": "Accesorios y utensilios de limpieza",
                },
            },
            "Maquillaje": {
                "category": "Higiene y cuidado personal",
                "subcategories": {
                    "Bases de maquillaje y corrector": "Maquillaje",
                    "Colorete y polvos": "Maquillaje",
                    "Labios": "Maquillaje",
                    "Ojos": "Maquillaje",
                    "Pinceles y brochas": "Maquillaje",
                },
            },
            "Marisco y pescado": {
                "category": "Frescos",
                "subcategories": {
                    "Marisco": "Pescado y marisco",
                    "Pescado congelado": {
                        "parent_category": {
                            "name": "Congelados",
                        },
                        "subcategory": "Pescado congelado",
                    },
                    "Pescado fresco": "Pescado y marisco",
                    "Salazones y ahumados": "Pescado y marisco",
                    "Sushi": "Sushi",
                },
            },
            "Mascotas": {
                "category": "Mascotas",
                "subcategories": {
                    "Gato": "Gato",
                    "Otros": "Otras mascotas",
                    "Perro": "Perro",
                },
            },
            "Panadería y pastelería": {
                "category": "Panadería y pastelería",
                "subcategories": {
                    "Bollería de horno": "Pan y bollería de horno",
                    "Bollería envasada": "Pan y bollería de horno",
                    "Harina y preparado repostería": "Harina y repostería",
                    "Pan de horno": "Pan y bollería de horno",
                    "Pan de molde y otras especialidades": "Pan de molde y tostado",
                    "Pan tostado y rallado": "Pan tostado y rallado",
                    "Picos, rosquilletas y picatostes": "Pan tostado y rallado",
                    "Tartas y pasteles": {
                        "parent_category": {
                            "name": "Congelados",
                        },
                        "subcategory": "Helados y postres congelados",
                    },
                    "Velas y decoración": "Otros",
                },
            },
            "Pizzas y platos preparados": {
                "category": "Platos preparados",
                "subcategories": {
                    "Listo para Comer": "Platos preparados",
                    "Pizzas": {
                        "parent_category": {
                            "name": "Congelados",
                        },
                        "subcategory": "Pizzas y bases congeladas",
                    },
                    "Platos preparados calientes": "Platos preparados",
                    "Platos preparados fríos": "Platos preparados",
                },
            },
            "Postres y yogures": {
                "category": "Lácteos y huevos",
                "subcategories": {
                    "Bífidus": "Yogures y postres lácteos",
                    "Flan y natillas": "Yogures y postres lácteos",
                    "Gelatina y otros postres": "Yogures y postres lácteos",
                    "Postres de soja": "Yogures y postres lácteos",
                    "Yogures desnatados": "Yogures y postres lácteos",
                    "Yogures griegos": "Yogures y postres lácteos",
                    "Yogures líquidos": "Yogures y postres lácteos",
                    "Yogures naturales y sabores": "Yogures y postres lácteos",
                    "Yogures y postres infantiles": "Yogures y postres lácteos",
                },
            },
            "Zumos": {
                "category": "Bebidas",
                "subcategories": {
                    "Fruta variada": "Zumos y néctares",
                    "Melocotón y piña": "Zumos y néctares",
                    "Naranja": "Zumos y néctares",
                    "Tomate y otros sabores": "Zumos y néctares",
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
                    parent_category = MercadonaParentCategoryModel.objects.get(
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
                            MercadonaCategoryModel.objects.get(
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

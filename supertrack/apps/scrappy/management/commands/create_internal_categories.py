from django.core.management.base import BaseCommand, CommandError

from supertrack.apps.scrappy.models import (
    InternalCategory,
    InternalSubCategory,
)

INTERNAL_CATEGORIES = {
    "Bebidas": [
        "Agua y refrescos",
        "Zumos y néctares",
        "Cerveza y bebidas alcohólicas",
        "Vinos y licores",
        "Isotónicas y energéticas",
        "Gaseosas y sodas",
    ],
    "Despensa": [
        "Arroz, pastas y legumbres",
        "Conservas y salsas",
        "Aceites y condimentos",
        "Harina y repostería",
        "Desayuno y dulces",
        "Frutos secos y aperitivos",
    ],
    "Lácteos y huevos": [
        "Leche y bebidas vegetales",
        "Yogures y postres lácteos",
        "Mantequilla y margarina",
        "Quesos",
    ],
    "Panadería y pastelería": [
        "Pan y bollería de horno",
        "Pan de molde y tostado",
        "Tartas y pasteles",
    ],
    "Frescos": [
        "Carnes frescas y embutidos",
        "Pescado y marisco",
        "Verduras y frutas",
    ],
    "Congelados": [
        "Carne congelada",
        "Pescado congelado",
        "Verduras congeladas",
        "Helados y postres congelados",
        "Pizzas y bases congeladas",
    ],
    "Higiene y cuidado personal": [
        "Cuidado del cabello",
        "Cuidado facial y corporal",
        "Higiene bucal",
        "Desodorantes y perfumes",
        "Maquillaje",
    ],
    "Limpieza y hogar": [
        "Detergentes y limpieza",
        "Insecticidas y ambientadores",
        "Accesorios y utensilios de limpieza",
        "Celulosa y papel higiénico",
    ],
    "Mascotas": [
        "Perro",
        "Gato",
        "Otras mascotas",
    ],
    "Infantil": [
        "Alimentación infantil",
        "Higiene y cuidado del bebé",
    ],
    "Bazar": [
        "Menaje y utensilios",
        "Libros y artículos de oficina",
    ],
}


class Command(BaseCommand):
    help = "Create internal categories and subcategories"

    def set_consum_internal_categories(self):
        categories_map = {
            12: {
                
            }
        }
    
    def handle(self, *args, **options):

        for category_name, subcategories in INTERNAL_CATEGORIES.items():
            internal_category, _ = InternalCategory.objects.get_or_create(
                name=category_name
            )

            for subcategory_name in subcategories:
                InternalSubCategory.objects.get_or_create(
                    name=subcategory_name,
                    parent_category=internal_category,
                )

        self.stdout.write(self.style.SUCCESS("Successfully created."))

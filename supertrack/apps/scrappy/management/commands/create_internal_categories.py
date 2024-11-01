from django.core.management.base import BaseCommand, CommandError

from supertrack.apps.scrappy.models import (
    InternalCategory,
    InternalSubCategory,
)

INTERNAL_CATEGORIES = {
    "Bebidas": [
        "Agua",
        "Refrescos",
        "Zumos y néctares",
        "Bebidas alcohólicas",
        "Cerveza",
        "Vinos y licores",
        "Isotónicas y energéticas",
        "Gaseosas y sodas",
    ],
    "Despensa": [
        "Arroz",
        "Pastas",
        "Legumbres",
        "Conservas",
        "Salsas",
        "Aceites y condimentos",
        "Harina y repostería",
        "Desayuno y dulces",
        "Frutos secos y aperitivos",
        "Café",
        "Té",
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
        "Embutidos",
        "Carnes frescas",
        "Pescado y marisco",
        "Verduras y frutas",
        "Empanados y elaborados",
    ],
    "Congelados": [
        "Carne congelada",
        "Pescado congelado",
        "Verduras congeladas",
        "Helados y postres congelados",
        "Pizzas y bases congeladas",
        "Arroz, pastas y legumbres",
        "Hielo",
        "Rebozados",
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

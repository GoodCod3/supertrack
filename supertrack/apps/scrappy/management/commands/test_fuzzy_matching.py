from django.core.management.base import BaseCommand, CommandError
from rapidfuzz import fuzz

from supertrack.apps.scrappy.models import (
    InternalCategory,
    InternalSubCategory,
    MercadonaProductModel,
)

class Command(BaseCommand):
    help = "Testing Fuzzy Matching"


    def handle(self, *args, **options):
        original_product = "Espárrago Verde congelado 300 Gr"
        best_choice_name=""
        best_choice_score=0
        for product in MercadonaProductModel.objects.filter(name__icontains="Espárrago"):
            name_similarity = fuzz.token_sort_ratio(original_product, product.name)
            # name_similarity = fuzz.token_set_ratio(original_product, product.name)
            print(f"{product.name} - {name_similarity}")
            if name_similarity > best_choice_score:
                best_choice_score = name_similarity
                best_choice_name = product.name
        print()
        print(f"Winner is {best_choice_name} - {best_choice_score}")
        
        self.stdout.write(self.style.SUCCESS("Successfully created."))

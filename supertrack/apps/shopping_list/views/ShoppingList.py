from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ShoppingListView(LoginRequiredMixin, TemplateView):
    template_name = "shopping_list_home.html"


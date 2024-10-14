from django.views import View
from django.http import HttpResponse


class StoreMercadonaProductsView(View):
    async def get(self, request, *args, **kwargs):
        return HttpResponse(True)


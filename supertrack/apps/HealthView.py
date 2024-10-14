from django.views import View
from django.http import JsonResponse

_CURRENT_VERSION = "20241014-v1"  # YYYY-mm-dd


class SuperTrackHealth(View):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a ok if the application is running
        """
        return JsonResponse({"versuib": _CURRENT_VERSION})

"""
URL configuration for supertrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from supertrack.apps.HealthView import SuperTrackHealth
from supertrack.generic_views.custom_login import custom_google_login

API_VERSION = "api/v1"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scrappy/", include("supertrack.apps.scrappy.urls")),
    path("shopping-list/", include("supertrack.apps.shopping_list.urls")),
    path("", include("supertrack.apps.dashboards.urls")),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += [
    path(
        "accounts/google/login/",
        custom_google_login,
        name="google_login_direct",
    ),
]

urlpatterns += [
    path(
        f"{API_VERSION}/health/",
        SuperTrackHealth.as_view(),
        name="supertrack_health",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

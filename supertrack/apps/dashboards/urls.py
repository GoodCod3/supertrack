from django.urls import path

from supertrack.apps.dashboards.views import HomeView

urlpatterns = [
    path(
        "",
        HomeView.as_view(),
        name="dashboards__home",
    ),
]

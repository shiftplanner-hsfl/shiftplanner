"""URL-Konfiguration von ShiftPlanner."""

from django.contrib import admin
from django.urls import path

from scheduling import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
]

"""Top-level URL configuration."""

from django.contrib import admin
from django.urls import path

from .views import healthcheck, home

urlpatterns = [
    path("", home, name="home"),
    path("health/", healthcheck, name="healthcheck"),
    path("admin/", admin.site.urls),
]

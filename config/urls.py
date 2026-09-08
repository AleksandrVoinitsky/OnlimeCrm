"""Top-level URL configuration."""

from django.contrib import admin
from django.urls import path

from .views import healthcheck, home, login_page

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_page, name="login"),
    path("health/", healthcheck, name="healthcheck"),
    path("admin/", admin.site.urls),
]

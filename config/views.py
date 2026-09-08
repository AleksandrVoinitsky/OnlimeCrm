"""Operational endpoints that do not contain business logic."""

from django.db import connection
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


def home(request: HttpRequest):
    """Render the initial application shell."""
    return render(request, "home.html")


def healthcheck(request: HttpRequest) -> JsonResponse:
    """Report process and database availability for the container orchestrator."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception:
        return JsonResponse({"status": "unavailable"}, status=503)
    return JsonResponse({"status": "ok"})

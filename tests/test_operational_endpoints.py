from django.test import Client, TestCase, override_settings


@override_settings(
    STORAGES={
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    }
)
class OperationalEndpointsTests(TestCase):
    def test_home_page_is_available(self) -> None:
        response = Client().get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Вещи, которые")

    def test_login_page_is_available(self) -> None:
        response = Client().get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Войдите")

    def test_healthcheck_reports_available_database(self) -> None:
        response = Client().get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

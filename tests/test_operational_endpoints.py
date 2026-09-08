from django.test import Client, TestCase


class OperationalEndpointsTests(TestCase):
    def test_home_page_is_available(self) -> None:
        response = Client().get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Onlime CRM")

    def test_healthcheck_reports_available_database(self) -> None:
        response = Client().get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

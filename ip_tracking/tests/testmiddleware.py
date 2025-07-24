from django.test import TestCase, Client
from ip_tracking.models import RequestLog


class IPTrackingMiddlewareTest(TestCase):
    """Test case for IPTrackingMiddleware."""

    def setUp(self):
        self.client = Client()

    def test_middleware_logs_requests(self):
        """Test that middleware logs HTTP requests"""
        # Clear existing logs
        RequestLog.objects.all().delete()

        # Make a request to any view (replace with your actual URL)
        response = self.client.get("/")  # or any valid URL in your app

        # Check if log entry was created
        logs = RequestLog.objects.all()
        self.assertEqual(logs.count(), 1)

        log_entry = logs.first()
        self.assertEqual(log_entry.path, "/")
        self.assertIsNotNone(log_entry.ip_address)

    def test_middleware_logs_multiple_requests(self):
        """Test middleware logs multiple requests"""
        initial_count = RequestLog.objects.count()

        # Make multiple requests
        self.client.get("/")
        self.client.get("/admin/")  # This should trigger middleware

        # Check that logs were created
        final_count = RequestLog.objects.count()
        self.assertEqual(final_count, initial_count + 2)

# create a middleware class that logs request details

from typing import Callable
import logging
from django.http import HttpRequest, HttpResponse

from .models import RequestLog

# Configure logger and handler only once at the module level
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    handler = logging.FileHandler("ip_tracking.log", mode="a", encoding="utf-8")
    logger.addHandler(handler)


class IPTrackingMiddleware:
    """Middleware to log request details such as IP address and path."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response
        self._logger = logger

    def __call__(self, request: HttpRequest) -> HttpResponse:
        # Log the IP address and user agent
        ip_address = request.META.get("REMOTE_ADDR")
        path = request.path

        self._logger.info("Request from IP: %s, Path: %s", ip_address, path)
        # Save the log entry
        try:
            if RequestLog.objects.create(ip_address=ip_address, path=path):
                self._logger.info("Logged request: %s - %s", ip_address, path)
            else:
                self._logger.warning("Failed to log request: %s - %s", ip_address, path)

            return self.get_response(request)
        except Exception as e:
            self._logger.error("Error logging request: %s", e)
            return HttpResponse("Internal Server Error", status=500)

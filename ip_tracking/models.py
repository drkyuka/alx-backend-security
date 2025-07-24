"""Django model to log request details such as IP address, user agent, and timestamp."""

from django.db import models
from django.utils import timezone


# Create your models here.
class RequestLog(models.Model):
    """Model to log request details such as IP address, user agent, and timestamp."""

    ip_address = models.GenericIPAddressField()
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"

    class Meta:
        """Meta class to define ordering of the model instances."""

        ordering = ["-timestamp"]
        verbose_name = "Request Log"
        verbose_name_plural = "Request Logs"

from django.urls import path
from . import views


urlpatterns = [
    path("test/", views.sample_view, name="test"),
]

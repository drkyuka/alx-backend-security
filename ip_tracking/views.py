from django.http import HttpResponse, HttpRequest


# Create your views here.
def sample_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, this is a sample view.")

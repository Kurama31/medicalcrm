#from django import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse


def main(request: HttpResponse) -> JsonResponse:
    return JsonResponse(data={
        "error": False,
        "status": "Hello from Django",
        "details": None
    }, status=200)
"""
news_app/views.py

API view functions for the news_app application.
"""

from django.http import JsonResponse


def home(request):
    """
    Home endpoint for the News API.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        JsonResponse: A JSON response with a welcome message and status.
    """
    return JsonResponse({
        "message": "Welcome to the News API",
        "status": "success"
    })

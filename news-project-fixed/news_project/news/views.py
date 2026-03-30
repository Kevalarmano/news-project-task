"""
news/views.py

View functions for the news application.
"""

from django.http import HttpResponse


def home(request):
    """
    Render the home page for the news application.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: A plain-text response confirming the project is running.
    """
    return HttpResponse("News Project is running")

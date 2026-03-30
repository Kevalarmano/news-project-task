"""
news_app/urls.py

URL routing for the news_app application.
"""

from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]

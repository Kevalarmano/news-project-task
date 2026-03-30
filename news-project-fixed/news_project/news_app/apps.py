"""
news_app/apps.py

Application configuration for the news_app application.
"""

from django.apps import AppConfig


class NewsAppConfig(AppConfig):
    """Configuration class for the news_app application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "news_app"

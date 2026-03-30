"""
news_app/admin.py

Registers news_app models with the Django admin site.
"""

from django.contrib import admin
from .models import NewsItem


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    """Admin configuration for the NewsItem model."""

    list_display = ("headline", "created_at")
    search_fields = ("headline",)

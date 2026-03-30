"""
news/admin.py

Registers news application models with the Django admin site.
"""

from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin configuration for the Article model."""

    list_display = ("title", "published_at")
    search_fields = ("title",)

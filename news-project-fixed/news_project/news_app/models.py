"""
news_app/models.py

Defines the data models for the news_app application.
"""

from django.db import models


class NewsItem(models.Model):
    """
    Represents a news item served through the API.

    Attributes:
        headline (str): Short headline for the news item.
        summary (str): Brief summary of the news item.
        created_at (datetime): Timestamp when the record was created.
    """

    headline = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human-readable representation of the news item."""
        return self.headline

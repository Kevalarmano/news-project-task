"""
news/models.py

Defines the data models for the news application.
"""

from django.db import models


class Article(models.Model):
    """
    Represents a news article.

    Attributes:
        title (str): The headline of the article.
        content (str): The full body text of the article.
        published_at (datetime): Timestamp when the article was published.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human-readable string representation of the article."""
        return self.title

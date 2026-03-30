"""Initial migration for the news_app application."""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Create the NewsItem table."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headline", models.CharField(max_length=255)),
                ("summary", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

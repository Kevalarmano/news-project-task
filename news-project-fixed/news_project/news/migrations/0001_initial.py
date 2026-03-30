"""Initial migration for the news app."""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Create the Article table."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("published_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

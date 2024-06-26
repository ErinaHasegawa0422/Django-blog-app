# Generated by Django 5.0.6 on 2024-05-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("slug", models.SlugField()),
                ("intro", models.TextField()),
                ("body", models.TextField()),
                ("posted_data", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsModel",
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
                ("news_name", models.CharField(max_length=255)),
                ("news_content", models.CharField(max_length=255)),
                ("news_description", models.CharField(max_length=255)),
                ("news_image", models.ImageField(upload_to=True)),
                ("news_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "News",
                "db_table": "news",
            },
        ),
    ]

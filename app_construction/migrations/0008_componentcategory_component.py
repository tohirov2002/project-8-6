# Generated by Django 5.0.4 on 2024-05-08 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_construction", "0007_remove_leadership_news_image_leadership_ld_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComponentCategory",
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
                ("CnCategory_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "componentCategories",
                "db_table": "componentCategory",
            },
        ),
        migrations.CreateModel(
            name="Component",
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
                ("cn_name", models.CharField(max_length=255)),
                ("cn_phone", models.CharField(default=1, max_length=255)),
                ("cn_email", models.EmailField(max_length=100, unique=True)),
                ("cn_image", models.ImageField(default=2, upload_to="images/")),
                (
                    "cn_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_construction.componentcategory",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Components",
                "db_table": "component",
            },
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-08 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_construction", "0003_adsmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Categories",
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Masters",
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
                ("master_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Masters",
                "db_table": "masters",
            },
        ),
        migrations.CreateModel(
            name="Specialty",
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
                ("sp_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Specialty",
                "db_table": "specialty",
            },
        ),
        migrations.CreateModel(
            name="Leadership",
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
                ("ld_name", models.CharField(max_length=255)),
                ("ld_admission", models.CharField(max_length=255)),
                ("ld_phone", models.CharField(blank=True, max_length=255, null=True)),
                ("ld_email", models.EmailField(max_length=100, unique=True)),
                (
                    "ld_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_construction.category",
                    ),
                ),
                (
                    "ld_masters",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_construction.masters",
                    ),
                ),
                (
                    "ld_bachelor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_construction.specialty",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Leadership",
                "db_table": "leadership",
            },
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_construction", "0008_componentcategory_component"),
    ]

    operations = [
        migrations.CreateModel(
            name="Standards",
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
                ("st_name", models.CharField(max_length=255)),
                ("st_code", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Standards",
                "db_table": "standards",
            },
        ),
    ]

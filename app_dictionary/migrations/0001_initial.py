# Generated by Django 5.0.4 on 2024-05-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DictionaryModel",
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
                ("name_uz", models.CharField(max_length=255)),
                ("name_ru", models.CharField(max_length=255)),
                ("name_eng", models.CharField(max_length=255)),
                ("name_turk", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Dictionary",
                "db_table": "dictionary",
            },
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_construction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsmodel",
            name="news_image",
            field=models.ImageField(default=1, upload_to="images/"),
        ),
    ]

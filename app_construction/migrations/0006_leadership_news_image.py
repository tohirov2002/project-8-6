# Generated by Django 5.0.4 on 2024-05-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_construction", "0005_alter_leadership_ld_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="leadership",
            name="news_image",
            field=models.ImageField(default=1, upload_to="images/"),
        ),
    ]

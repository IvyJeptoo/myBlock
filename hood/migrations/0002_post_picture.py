# Generated by Django 4.1.3 on 2022-11-17 12:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hood", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="picture",
            field=cloudinary.models.CloudinaryField(
                default=None, max_length=255, verbose_name="image"
            ),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hood", "0003_remove_post_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=250)),
                ("address", models.TextField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]
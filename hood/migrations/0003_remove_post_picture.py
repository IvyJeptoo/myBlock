# Generated by Django 4.1.3 on 2022-11-17 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hood", "0002_post_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="picture",
        ),
    ]

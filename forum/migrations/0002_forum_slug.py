# Generated by Django 4.2.2 on 2023-07-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="forum",
            name="slug",
            field=models.SlugField(default="none"),
        ),
    ]

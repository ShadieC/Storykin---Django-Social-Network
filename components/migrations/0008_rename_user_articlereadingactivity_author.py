# Generated by Django 4.2.2 on 2023-08-13 13:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("components", "0007_alter_articlelike_unique_together_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="articlereadingactivity",
            old_name="user",
            new_name="author",
        ),
    ]

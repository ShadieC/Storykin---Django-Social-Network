# Generated by Django 4.2.2 on 2023-09-02 12:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("components", "0016_articlecomment_contributer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="author",
            new_name="contributer",
        ),
        migrations.RenameField(
            model_name="articlecomment",
            old_name="contributer",
            new_name="author",
        ),
    ]

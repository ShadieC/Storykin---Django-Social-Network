# Generated by Django 4.2.2 on 2023-07-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("components", "0002_post_anonymous"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="ArticleImages/"),
        ),
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="BookImages/"),
        ),
        migrations.AddField(
            model_name="book",
            name="new_price",
            field=models.DecimalField(decimal_places=2, default="0.00", max_digits=10),
        ),
        migrations.AddField(
            model_name="book",
            name="old_price",
            field=models.DecimalField(decimal_places=2, default="0.00", max_digits=10),
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="PostImages/"),
        ),
    ]

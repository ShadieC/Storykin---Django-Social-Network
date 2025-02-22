# Generated by Django 4.2.2 on 2023-08-05 11:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("components", "0006_alter_post_admirers_remove_post_likes_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="articlelike",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="articlelike",
            name="article",
        ),
        migrations.RemoveField(
            model_name="articlelike",
            name="user",
        ),
        migrations.AlterUniqueTogether(
            name="booklike",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="booklike",
            name="book",
        ),
        migrations.RemoveField(
            model_name="booklike",
            name="user",
        ),
        migrations.AlterUniqueTogether(
            name="bookreviewlike",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="bookreviewlike",
            name="book_review",
        ),
        migrations.RemoveField(
            model_name="bookreviewlike",
            name="user",
        ),
        migrations.AlterUniqueTogether(
            name="postcommentlike",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="postcommentlike",
            name="post_comment",
        ),
        migrations.RemoveField(
            model_name="postcommentlike",
            name="user",
        ),
        migrations.RemoveField(
            model_name="article",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="articlecomment",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="book",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="bookreview",
            name="likes",
        ),
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="post_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.RemoveField(
            model_name="postcomment",
            name="likes",
        ),
        migrations.DeleteModel(
            name="ArticleCommentLike",
        ),
        migrations.DeleteModel(
            name="ArticleLike",
        ),
        migrations.DeleteModel(
            name="BookLike",
        ),
        migrations.DeleteModel(
            name="BookReviewLike",
        ),
        migrations.DeleteModel(
            name="PostCommentLike",
        ),
        migrations.AddField(
            model_name="article",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="article_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="articlecomment",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                related_name="articlecomment_likes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="book_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="bookreview",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="book_review", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="postcomment",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                related_name="postcomment_likes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

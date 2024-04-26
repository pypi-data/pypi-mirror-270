# Generated by Django 5.0.4 on 2024-04-24 09:29
import django.contrib.postgres.search
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0012_alter_blogcomment_likes_alter_blogpost_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogposttranslation",
            name="search_document",
            field=models.TextField(
                blank=True, db_index=True, default="", verbose_name="Search Document"
            ),
        ),
        migrations.AddField(
            model_name="blogposttranslation",
            name="search_document_dirty",
            field=models.BooleanField(
                db_index=True, default=False, verbose_name="Search Document Dirty"
            ),
        ),
        migrations.AddField(
            model_name="blogposttranslation",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(
                blank=True, db_index=True, null=True, verbose_name="Search Vector"
            ),
        ),
        migrations.AddField(
            model_name="blogposttranslation",
            name="search_vector_dirty",
            field=models.BooleanField(
                db_index=True, default=False, verbose_name="Search Vector Dirty"
            ),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-11 17:27
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_alter_blogtag_managers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogcategory",
            options={
                "ordering": ["sort_order"],
                "verbose_name": "Blog Category",
                "verbose_name_plural": "Blog Categories",
            },
        ),
        migrations.AlterModelOptions(
            name="blogtag",
            options={
                "ordering": ["sort_order"],
                "verbose_name": "Blog Tag",
                "verbose_name_plural": "Blog Tags",
            },
        ),
        migrations.AlterModelManagers(
            name="blogtag",
            managers=[
                ("active_tags", django.db.models.manager.Manager()),
            ],
        ),
    ]

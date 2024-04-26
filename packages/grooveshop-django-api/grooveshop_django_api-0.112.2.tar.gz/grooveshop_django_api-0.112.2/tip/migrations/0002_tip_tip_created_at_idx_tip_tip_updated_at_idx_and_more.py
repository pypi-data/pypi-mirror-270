# Generated by Django 5.0.3 on 2024-03-31 12:31
import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tip", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="tip",
            index=django.contrib.postgres.indexes.BTreeIndex(
                fields=["created_at"], name="tip_created_at_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="tip",
            index=django.contrib.postgres.indexes.BTreeIndex(
                fields=["updated_at"], name="tip_updated_at_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="tip",
            index=django.contrib.postgres.indexes.BTreeIndex(
                fields=["sort_order"], name="tip_sort_order_idx"
            ),
        ),
    ]

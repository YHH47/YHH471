# Generated by Django 5.1.1 on 2024-10-30 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0005_alter_review_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Review",
        ),
    ]

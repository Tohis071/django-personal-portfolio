# Generated by Django 4.1.6 on 2023-02-20 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="url",
            new_name="new name",
        ),
    ]

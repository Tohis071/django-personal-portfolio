# Generated by Django 4.1.6 on 2023-02-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="onemoretitle",
            field=models.CharField(default=12, max_length=150),
            preserve_default=False,
        ),
    ]

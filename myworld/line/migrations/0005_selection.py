# Generated by Django 4.1.1 on 2023-01-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("line", "0004_capacity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Selection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=255)),
                ("choice", models.CharField(max_length=255)),
            ],
        ),
    ]
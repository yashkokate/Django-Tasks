# Generated by Django 5.1.1 on 2024-09-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petsapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="State",
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
                ("name", models.CharField(max_length=100)),
                ("population", models.IntegerField()),
                ("language", models.CharField(max_length=100)),
                ("capital", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Pet",
        ),
    ]

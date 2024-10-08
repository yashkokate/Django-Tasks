# Generated by Django 5.1.1 on 2024-09-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petsapp", "0003_employee_delete_state"),
    ]

    operations = [
        migrations.CreateModel(
            name="Media",
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
                ("name", models.CharField(max_length=255)),
                (
                    "media_type",
                    models.CharField(
                        choices=[
                            ("Audio", "Audio"),
                            ("Video", "Video"),
                            ("Image", "Image"),
                        ],
                        max_length=10,
                    ),
                ),
                ("format", models.CharField(max_length=50)),
                ("size_mb", models.DecimalField(decimal_places=2, max_digits=10)),
                ("duration_secs", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
    ]

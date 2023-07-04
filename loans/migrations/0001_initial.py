# Generated by Django 4.2.2 on 2023-07-04 18:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loans",
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
                (
                    "loan_initial",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("loan_return", models.DateTimeField(blank=True, null=True)),
                ("is_delay", models.BooleanField(default=False)),
                ("is_returned", models.BooleanField(default=False)),
                ("blocking_date", models.DateTimeField(blank=True, null=True)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="loans",
                        to="copies.copy",
                    ),
                ),
            ],
        ),
    ]

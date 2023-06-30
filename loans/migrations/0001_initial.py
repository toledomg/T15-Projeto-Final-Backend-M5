# Generated by Django 4.2.2 on 2023-06-30 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import loans.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ("loan_initial", models.DateTimeField(auto_now_add=True)),
                ("loan_return", models.DateTimeField(default=loans.models.loan_return)),
                ("is_returned", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loans",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

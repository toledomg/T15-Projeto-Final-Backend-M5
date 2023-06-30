# Generated by Django 4.2.2 on 2023-06-30 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=150)),
                ("author", models.CharField(max_length=150)),
                ("pages", models.IntegerField(blank=True, null=True)),
                ("category", models.CharField(max_length=150)),
                ("copies_count", models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name="Follow",
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
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]

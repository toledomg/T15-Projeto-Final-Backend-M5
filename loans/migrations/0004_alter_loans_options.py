# Generated by Django 4.2.2 on 2023-07-04 12:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("loans", "0003_alter_loans_blocking_date_alter_loans_loan_return"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="loans",
            options={"ordering": ["id"]},
        ),
    ]
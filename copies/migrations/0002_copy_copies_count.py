# Generated by Django 4.2.3 on 2023-07-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='copies_count',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ticket", "0004_alter_ticketmodel_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticketproductmodel",
            name="quantity",
            field=models.IntegerField(default=0, verbose_name="Quantity"),
        ),
    ]

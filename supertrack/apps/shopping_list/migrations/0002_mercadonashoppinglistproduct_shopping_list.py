# Generated by Django 5.1.2 on 2024-10-28 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercadonashoppinglistproduct',
            name='shopping_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='shopping_list.mercadonashoppinglist'),
            preserve_default=False,
        ),
    ]
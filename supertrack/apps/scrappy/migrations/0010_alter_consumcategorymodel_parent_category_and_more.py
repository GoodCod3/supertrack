# Generated by Django 5.1.2 on 2024-10-29 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrappy', '0009_alter_consumproductmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumcategorymodel',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrappy.consumparentcategorymodel'),
        ),
        migrations.AlterField(
            model_name='consumproductcategorymodel',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrappy.consumcategorymodel'),
        ),
        migrations.AlterField(
            model_name='consumproductmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrappy.consumproductcategorymodel'),
        ),
    ]

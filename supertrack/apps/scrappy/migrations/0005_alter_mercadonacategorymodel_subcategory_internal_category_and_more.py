# Generated by Django 5.1.2 on 2024-10-31 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrappy', '0004_rename_parent_category_mercadonaparentcategorymodel_parent_internal_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercadonacategorymodel',
            name='subcategory_internal_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scrappy.internalsubcategory'),
        ),
        migrations.AlterField(
            model_name='mercadonaparentcategorymodel',
            name='parent_internal_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scrappy.internalcategory'),
        ),
    ]

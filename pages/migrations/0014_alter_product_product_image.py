# Generated by Django 4.2.3 on 2023-09-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.CharField(max_length=255),
        ),
    ]

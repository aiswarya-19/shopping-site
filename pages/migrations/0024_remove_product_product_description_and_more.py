# Generated by Django 4.2.5 on 2023-09-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_remove_category_cat_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_description',
        ),
        migrations.AddField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
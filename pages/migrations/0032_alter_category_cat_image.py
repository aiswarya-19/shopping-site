# Generated by Django 4.2.5 on 2023-09-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0031_remove_order_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="cat_image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0021_alter_registration_register_propic"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_cat",
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_desc',
            field=models.TextField(null=True),
        ),
    ]

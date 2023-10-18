# Generated by Django 4.1.3 on 2023-08-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('product_id', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.FloatField(max_length=255)),
                ('product_quantity', models.CharField(max_length=255)),
            ],
        ),
    ]
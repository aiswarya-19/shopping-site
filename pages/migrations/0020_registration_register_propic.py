# Generated by Django 4.1.3 on 2023-09-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_category_cat_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='register_propic',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

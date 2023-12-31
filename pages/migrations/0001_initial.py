# Generated by Django 4.1.3 on 2023-07-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('contact_message', models.TextField()),
            ],
        ),
    ]

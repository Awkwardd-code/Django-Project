# Generated by Django 5.1.4 on 2024-12-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/'),
        ),
    ]
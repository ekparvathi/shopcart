# Generated by Django 5.0.6 on 2024-06-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.FileField(default='default', upload_to='static/images/'),
        ),
    ]

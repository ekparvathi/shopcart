# Generated by Django 5.0.6 on 2024-06-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scartapp', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.BigIntegerField(default=1),
        ),
    ]

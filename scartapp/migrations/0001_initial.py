# Generated by Django 5.0.6 on 2024-06-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=400)),
                ('PIN', models.CharField(max_length=6)),
                ('Phone', models.BigIntegerField()),
                ('Image', models.ImageField(default='default', upload_to='static/images/')),
            ],
        ),
    ]

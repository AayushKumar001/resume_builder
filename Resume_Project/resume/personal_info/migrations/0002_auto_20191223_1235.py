# Generated by Django 2.2.7 on 2019-12-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]

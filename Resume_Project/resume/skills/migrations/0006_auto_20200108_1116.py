# Generated by Django 2.2.7 on 2020-01-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_auto_20191230_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techskill',
            name='experience',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]

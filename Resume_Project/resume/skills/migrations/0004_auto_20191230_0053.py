# Generated by Django 2.2.7 on 2019-12-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_techskill_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techskill',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]

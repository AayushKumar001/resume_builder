# Generated by Django 2.2.7 on 2019-12-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_auto_20191230_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techskill',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]

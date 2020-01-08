# Generated by Django 2.2.7 on 2019-12-08 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=256)),
                ('job_title', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('currently_work', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('career_field', models.TextField()),
                ('career_subfield', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_experience', to='personal_info.ContactInfo')),
            ],
            options={
                'ordering': ['employer'],
            },
        ),
    ]

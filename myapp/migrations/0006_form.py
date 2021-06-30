# Generated by Django 3.0.5 on 2021-06-24 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_teachers_data_blood_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_2_id', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Course', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('topic', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('description', models.CharField(blank=True, default=None, max_length=5000, null=True)),
                ('supervisor_1', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_2', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_3', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_4', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_5', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('external', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('student_1_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.0.5 on 2021-06-24 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('mobile_no', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('designation', models.TextField(blank=True, default=None, null=True)),
                ('photos', models.FileField(blank=True, default=None, null=True, upload_to='teacher/')),
                ('linkedin', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('github', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MSc_Institute_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('MSc_Institute_Country', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('MSc_start_date', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('MSc_end_date', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Phd_Institute_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Phd_Institute_Country', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Phd_start_date', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Phd_end_date', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('gender', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('mobile_no', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('blood_group', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('photos', models.FileField(blank=True, default=None, null=True, upload_to='images/')),
                ('major_cgpa', models.FloatField(blank=True, default=None, max_length=5, null=True)),
                ('total_cgpa', models.FloatField(blank=True, default=None, max_length=5, null=True)),
                ('linkedin', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('github', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Research_area', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Published_Paper', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Published_Journal', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

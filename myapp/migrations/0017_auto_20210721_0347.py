# Generated by Django 3.0.5 on 2021-07-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20210721_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='major_cgpa',
            field=models.FloatField(blank=True, default=0.0, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='total_cgpa',
            field=models.FloatField(blank=True, default=0.0, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='teachers_data',
            name='photos',
            field=models.FileField(blank=True, default=None, null=True, upload_to='teacher/'),
        ),
    ]

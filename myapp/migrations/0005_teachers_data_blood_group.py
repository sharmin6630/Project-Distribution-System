# Generated by Django 3.0.5 on 2021-06-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210624_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_data',
            name='blood_group',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
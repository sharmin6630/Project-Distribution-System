# Generated by Django 3.0.5 on 2021-06-25 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210626_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='assigned_supervisor_id',
            field=models.CharField(blank=True, default=None, max_length=55, null=True),
        ),
    ]

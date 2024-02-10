# Generated by Django 5.0.1 on 2024-02-08 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_machines_machine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='location',
        ),
        migrations.AddField(
            model_name='machine',
            name='installation_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='machine',
            name='power_consumption_per_hour',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
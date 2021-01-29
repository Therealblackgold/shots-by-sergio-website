# Generated by Django 3.1.5 on 2021-01-29 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.2.6 on 2019-12-20 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0052_auto_20191221_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlystatistics',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

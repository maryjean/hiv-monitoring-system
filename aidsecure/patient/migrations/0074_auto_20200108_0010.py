# Generated by Django 2.2.6 on 2020-01-07 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0073_auto_20200107_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medhistform',
            name='date_diagnosed',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]

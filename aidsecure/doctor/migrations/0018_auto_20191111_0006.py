# Generated by Django 2.2.6 on 2019-11-10 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_auto_20191111_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='last_log_in',
            field=models.DateTimeField(verbose_name=datetime.datetime.now),
        ),
    ]

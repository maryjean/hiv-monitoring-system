# Generated by Django 2.2.6 on 2019-11-10 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0034_auto_20191110_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='last_log_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 23, 53, 7, 672511)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_log_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 23, 53, 7, 672511)),
        ),
        migrations.AlterField(
            model_name='patientnotification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 53, 7, 665509)),
        ),
        migrations.AlterField(
            model_name='pendingdoctor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 53, 7, 665509)),
        ),
        migrations.AlterField(
            model_name='personalrecord',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 53, 7, 663513)),
        ),
        migrations.AlterField(
            model_name='personalrecord',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 53, 7, 663513)),
        ),
    ]

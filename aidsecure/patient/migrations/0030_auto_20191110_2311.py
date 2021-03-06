# Generated by Django 2.2.6 on 2019-11-10 15:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0029_auto_20191110_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='last_log_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 15, 11, 9, 459490, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_log_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 15, 11, 9, 459490, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientnotification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 451484, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pendingdoctor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 452832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='personalrecord',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 450489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='personalrecord',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 450489, tzinfo=utc)),
        ),
    ]

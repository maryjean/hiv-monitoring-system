# Generated by Django 2.2.6 on 2019-11-10 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_auto_20191110_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='last_log_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 23, 52, 57, 947999)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_log_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 23, 52, 57, 947999)),
        ),
        migrations.AlterField(
            model_name='doctornotification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 52, 57, 947999)),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 52, 57, 947000)),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='schedule_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 52, 57, 946000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorstats',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 23, 52, 57, 946000)),
        ),
        migrations.AlterField(
            model_name='doctorstats',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 23, 52, 57, 946000)),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 23, 52, 57, 945000)),
        ),
    ]

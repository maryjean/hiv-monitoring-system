# Generated by Django 2.2.6 on 2019-11-10 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_auto_20191110_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='last_log_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 15, 46, 31, 825435, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_log_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 15, 46, 31, 825435, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctornotification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 46, 31, 824434, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 46, 31, 823431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='schedule_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 46, 31, 823431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorstats',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 15, 46, 31, 822434, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorstats',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 15, 46, 31, 822434, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 46, 31, 822434, tzinfo=utc)),
        ),
    ]

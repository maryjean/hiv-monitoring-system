# Generated by Django 2.2.6 on 2019-11-10 15:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20191110_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='last_log_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 15, 11, 9, 445640, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_log_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 10, 15, 11, 9, 445640, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctornotification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 444487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 443486, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='schedule_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 443486, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorstats',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 442485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctorstats',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 442485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 10, 15, 11, 9, 441486, tzinfo=utc)),
        ),
    ]

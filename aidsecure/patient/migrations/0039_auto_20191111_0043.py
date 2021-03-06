# Generated by Django 2.2.6 on 2019-11-10 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0038_auto_20191111_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientnotification',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pendingdoctor',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='personalrecord',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='personalrecord',
            name='updated_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

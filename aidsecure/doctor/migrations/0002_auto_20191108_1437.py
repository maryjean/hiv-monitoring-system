# Generated by Django 2.2.6 on 2019-11-08 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctornotification',
            old_name='subject',
            new_name='notification_type',
        ),
    ]

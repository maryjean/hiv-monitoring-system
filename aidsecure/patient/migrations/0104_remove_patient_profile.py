# Generated by Django 2.2.7 on 2020-04-01 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0103_patient_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='profile',
        ),
    ]
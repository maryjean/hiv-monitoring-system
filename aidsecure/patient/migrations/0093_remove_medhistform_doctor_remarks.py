# Generated by Django 2.2.7 on 2020-02-11 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0092_auto_20200201_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medhistform',
            name='doctor_remarks',
        ),
    ]
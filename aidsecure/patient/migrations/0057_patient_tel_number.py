# Generated by Django 2.2.6 on 2019-12-03 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0056_patient_home_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='tel_number',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]

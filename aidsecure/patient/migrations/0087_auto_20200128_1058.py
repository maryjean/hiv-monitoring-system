# Generated by Django 2.2.6 on 2020-01-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0086_auto_20200128_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medhistform',
            name='date_diagnosed',
            field=models.DateField(blank=True, null=True),
        ),
    ]

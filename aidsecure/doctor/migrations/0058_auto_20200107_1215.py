# Generated by Django 2.2.6 on 2020-01-07 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0057_auto_20191221_0339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlystatistics',
            options={'get_latest_by': 'created_on', 'verbose_name_plural': 'Monthly Statistics'},
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-20 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0056_auto_20191221_0331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlystatistics',
            options={'get_latest_by': 'year', 'verbose_name_plural': 'Monthly Statistics'},
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0059_auto_20191216_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medhistform',
            options={'get_latest_by': ['created_on'], 'verbose_name_plural': 'Medical History Forms'},
        ),
    ]

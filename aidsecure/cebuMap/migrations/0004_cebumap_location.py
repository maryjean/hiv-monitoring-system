# Generated by Django 2.2.6 on 2019-11-06 09:53

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cebuMap', '0003_cebumap'),
    ]

    operations = [
        migrations.AddField(
            model_name='cebumap',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]

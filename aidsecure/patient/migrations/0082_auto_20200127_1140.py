# Generated by Django 2.2.6 on 2020-01-27 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0081_auto_20200124_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='slug',
            field=models.SlugField(),
        ),
    ]

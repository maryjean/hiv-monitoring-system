# Generated by Django 2.2.6 on 2019-11-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cebuMap', '0002_auto_20191106_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='CebuMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceb_map', models.URLField(max_length=250, null=True)),
            ],
        ),
    ]

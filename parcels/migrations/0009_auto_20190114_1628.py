# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-14 16:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0008_auto_20190114_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='date_taken',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 16, 28, 16, 417965, tzinfo=utc)),
        ),
    ]
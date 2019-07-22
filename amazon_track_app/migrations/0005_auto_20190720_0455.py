# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_track_app', '0004_auto_20190719_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackdata',
            name='p_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='trackdata',
            name='p_url',
            field=models.CharField(default='', max_length=250),
        ),
    ]

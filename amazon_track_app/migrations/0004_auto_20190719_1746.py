# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_track_app', '0003_auto_20190719_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackdata',
            name='p_url',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='trackdata',
            name='p_email',
            field=models.EmailField(max_length=254, unique=True, serialize=False, primary_key=True),
        ),
    ]

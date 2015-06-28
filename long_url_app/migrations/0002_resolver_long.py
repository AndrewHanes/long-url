# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('long_url_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resolver',
            name='long',
            field=models.CharField(default='asd', max_length=2084, db_index=True),
            preserve_default=False,
        ),
    ]

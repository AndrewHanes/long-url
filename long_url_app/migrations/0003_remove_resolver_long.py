# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('long_url_app', '0002_resolver_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resolver',
            name='long',
        ),
    ]

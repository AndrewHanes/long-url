# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resolver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ident', models.CharField(db_index=True, max_length=2084)),
                ('to', models.CharField(db_index=True, max_length=2084)),
                ('created_ip', models.CharField(db_index=True, max_length=128)),
                ('last_accessed', models.DateTimeField()),
            ],
        ),
    ]

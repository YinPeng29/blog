# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae')),
                ('category', models.CharField(max_length=50, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe6\xa0\x87\xe7\xad\xbe', blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', models.TextField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]

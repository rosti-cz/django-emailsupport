# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_created=True)),
                ('subject', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('body_html', models.TextField(blank=True)),
                ('state', models.IntegerField(default=1, choices=[(2, 'Assign'), (1, 'New'), (0, 'Closed')])),
            ],
            options={
                'ordering': ('-created', '-state'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submitter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.EmailField(unique=True, max_length=75, db_index=True)),
                ('name', models.CharField(max_length=256, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='email',
            name='submitter',
            field=models.ForeignKey(to='django_emailsupport.Submitter'),
            preserve_default=True,
        ),
    ]

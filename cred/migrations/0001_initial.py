# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cred.fields
from django.conf import settings
import cred.storage


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cred',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, db_index=True)),
                ('url', models.URLField(db_index=True, null=True, blank=True)),
                ('username', models.CharField(db_index=True, max_length=250, null=True, blank=True)),
                ('password', models.CharField(max_length=250, null=True, blank=True)),
                ('descriptionmarkdown', models.BooleanField(default=False, verbose_name='Markdown Description')),
                ('description', models.TextField(null=True, blank=True)),
                ('iconname', models.CharField(default=b'Key.png', max_length=64, verbose_name=b'Icon')),
                ('ssh_key', cred.fields.SizedFileField(storage=cred.storage.CredAttachmentStorage(), null=True, upload_to=b'not required', blank=True)),
                ('attachment', cred.fields.SizedFileField(storage=cred.storage.CredAttachmentStorage(), null=True, upload_to=b'not required', blank=True)),
                ('is_deleted', models.BooleanField(default=False, db_index=True)),
                ('modified', models.DateTimeField(db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ssh_key_name', models.CharField(max_length=64, null=True, blank=True)),
                ('attachment_name', models.CharField(max_length=64, null=True, blank=True)),
                ('group', models.ForeignKey(to='auth.Group')),
                ('groups', models.ManyToManyField(default=None, related_name='child_creds', null=True, to='auth.Group', blank=True)),
                ('latest', models.ForeignKey(related_name='history', blank=True, to='cred.Cred', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audittype', models.CharField(max_length=1, choices=[(b'A', 'Added'), (b'C', 'Changed'), (b'M', 'Only Metadata Changed'), (b'V', 'Only Details Viewed'), (b'X', 'Exported'), (b'D', 'Deleted'), (b'S', 'Scheduled For Change'), (b'P', 'Password Viewed')])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cred', models.ForeignKey(related_name='logs', to='cred.Cred')),
                ('user', models.ForeignKey(related_name='credlogs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-time',),
                'get_latest_by': 'time',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CredChangeQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cred', models.ForeignKey(to='cred.Cred', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cred',
            name='tags',
            field=models.ManyToManyField(default=None, related_name='child_creds', null=True, to='cred.Tag', blank=True),
            preserve_default=True,
        ),
    ]

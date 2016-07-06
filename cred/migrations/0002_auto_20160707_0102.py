# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cred.fields
import cred.storage


class Migration(migrations.Migration):

    dependencies = [
        ('cred', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cred',
            name='slug',
            field=models.CharField(db_index=True, max_length=64, null=True, verbose_name='Slug', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='attachment',
            field=cred.fields.SizedFileField(storage=cred.storage.CredAttachmentStorage(), upload_to=b'not required', null=True, verbose_name='Attachment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='group',
            field=models.ForeignKey(verbose_name='Group', to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='groups',
            field=models.ManyToManyField(related_name='child_creds', default=None, to='auth.Group', blank=True, null=True, verbose_name='Groups'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='password',
            field=models.CharField(max_length=250, null=True, verbose_name='Password', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='ssh_key',
            field=cred.fields.SizedFileField(storage=cred.storage.CredAttachmentStorage(), upload_to=b'not required', null=True, verbose_name='SSH key', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='tags',
            field=models.ManyToManyField(related_name='child_creds', default=None, to='cred.Tag', blank=True, null=True, verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Title', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='url',
            field=models.URLField(db_index=True, null=True, verbose_name='URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cred',
            name='username',
            field=models.CharField(db_index=True, max_length=250, null=True, verbose_name='Username', blank=True),
            preserve_default=True,
        ),
    ]

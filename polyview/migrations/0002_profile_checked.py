# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-02 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration***REMOVED***:

    dependencies = [
        ('polysearch', '0004_auto_20170901_1935'***REMOVED***,
        ('polyview', '0001_initial'***REMOVED***,
    ***REMOVED***

    operations = [
        migrations.AddField(
            model_name='profile',
            name='checked',
            field=models.ManyToManyField(blank=True, to='polysearch.Sections'***REMOVED***,
        ***REMOVED***,
    ***REMOVED***

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration***REMOVED***:

    dependencies = [
        ('polysearch', '0004_auto_20170901_1935'***REMOVED***,
    ***REMOVED***

    operations = [
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('instructor', models.CharField(max_length=50, primary_key=True, serialize=False***REMOVED******REMOVED***,
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True***REMOVED******REMOVED***,
                ('instructor_id', models.SmallIntegerField(blank=True, null=True***REMOVED******REMOVED***,
            ***REMOVED***,
            options={
                'db_table': 'scrape_instructors',
                'managed': False,
        ***REMOVED***,
        ***REMOVED***,
    ***REMOVED***
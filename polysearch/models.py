# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models

class Courses(models.Model***REMOVED***:
    data_id = models.IntegerField(primary_key=True***REMOVED***
    course_ac = models.CharField(max_length=10***REMOVED***
    course_num = models.CharField(max_length=10***REMOVED***
    units = models.CharField(max_length=6***REMOVED***
    course_description = models.CharField(max_length=150***REMOVED***
    course_catalog_desc = models.CharField(max_length=1200***REMOVED***

    def __unicode__(self***REMOVED***:
        return ('{***REMOVED*** {***REMOVED***'***REMOVED***.format(self.course_ac, self.course_num***REMOVED***

    class Meta:
        ordering = ('course_ac', 'course_num'***REMOVED***
        managed = False
        db_table = 'scrape_courses_fall_2017'


class Sections(models.Model***REMOVED***:
    class_field = models.SmallIntegerField(db_column='class', primary_key=True***REMOVED***
    course_id = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course_id'***REMOVED***
    sec_num = models.SmallIntegerField(***REMOVED***
    type = models.CharField(max_length=3, blank=True, null=True***REMOVED***
    instructor = models.CharField(max_length=50, blank=True, null=True***REMOVED***
    available = models.SmallIntegerField(blank=True, null=True***REMOVED***
    taken = models.SmallIntegerField(blank=True, null=True***REMOVED***
    waiting = models.SmallIntegerField(blank=True, null=True***REMOVED***
    status = models.CharField(max_length=20, blank=True, null=True***REMOVED***
    days = models.CharField(max_length=5, blank=True, null=True***REMOVED***
    start = models.TimeField(blank=True, null=True***REMOVED***
    end = models.TimeField(blank=True, null=True***REMOVED***
    building = models.CharField(max_length=30, blank=True, null=True***REMOVED***
    room = models.CharField(max_length=10, blank=True, null=True***REMOVED***
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True***REMOVED***
    sec_group = models.SmallIntegerField(***REMOVED***

    def __unicode__(self***REMOVED***:
        return ('{***REMOVED*** {***REMOVED***'***REMOVED***.format(self.course_id.course_ac, self.course_id.course_num***REMOVED***

    class Meta:
        ordering = ('course_id__course_ac', 'course_id__course_num', 'sec_num'***REMOVED***
        managed = False
        db_table = 'scrape_sections_fall_2017'
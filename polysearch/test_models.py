# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model***REMOVED***:
    name = models.CharField(unique=True, max_length=80***REMOVED***

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model***REMOVED***:
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING***REMOVED***
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING***REMOVED***

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'***REMOVED***,***REMOVED***


class AuthPermission(models.Model***REMOVED***:
    name = models.CharField(max_length=255***REMOVED***
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING***REMOVED***
    codename = models.CharField(max_length=100***REMOVED***

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'***REMOVED***,***REMOVED***


class AuthUser(models.Model***REMOVED***:
    password = models.CharField(max_length=128***REMOVED***
    last_login = models.DateTimeField(blank=True, null=True***REMOVED***
    is_superuser = models.IntegerField(***REMOVED***
    username = models.CharField(unique=True, max_length=150***REMOVED***
    first_name = models.CharField(max_length=30***REMOVED***
    last_name = models.CharField(max_length=30***REMOVED***
    email = models.CharField(max_length=254***REMOVED***
    is_staff = models.IntegerField(***REMOVED***
    is_active = models.IntegerField(***REMOVED***
    date_joined = models.DateTimeField(***REMOVED***

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model***REMOVED***:
    user = models.ForeignKey(AuthUser, models.DO_NOTHING***REMOVED***
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING***REMOVED***

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'***REMOVED***,***REMOVED***


class AuthUserUserPermissions(models.Model***REMOVED***:
    user = models.ForeignKey(AuthUser, models.DO_NOTHING***REMOVED***
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING***REMOVED***

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'***REMOVED***,***REMOVED***


class DjangoAdminLog(models.Model***REMOVED***:
    action_time = models.DateTimeField(***REMOVED***
    object_id = models.TextField(blank=True, null=True***REMOVED***
    object_repr = models.CharField(max_length=200***REMOVED***
    action_flag = models.SmallIntegerField(***REMOVED***
    change_message = models.TextField(***REMOVED***
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True***REMOVED***
    user = models.ForeignKey(AuthUser, models.DO_NOTHING***REMOVED***

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model***REMOVED***:
    app_label = models.CharField(max_length=100***REMOVED***
    model = models.CharField(max_length=100***REMOVED***

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'***REMOVED***,***REMOVED***


class DjangoMigrations(models.Model***REMOVED***:
    app = models.CharField(max_length=255***REMOVED***
    name = models.CharField(max_length=255***REMOVED***
    applied = models.DateTimeField(***REMOVED***

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model***REMOVED***:
    session_key = models.CharField(primary_key=True, max_length=40***REMOVED***
    session_data = models.TextField(***REMOVED***
    expire_date = models.DateTimeField(***REMOVED***

    class Meta:
        managed = False
        db_table = 'django_session'


class Sections(models.Model***REMOVED***:
    class_field = models.IntegerField(db_column='class', primary_key=True***REMOVED***  # Field renamed because it was a Python reserved word.
    course = models.CharField(max_length=10, blank=True, null=True***REMOVED***
    number = models.IntegerField(blank=True, null=True***REMOVED***
    type = models.CharField(max_length=3, blank=True, null=True***REMOVED***
    instructor = models.CharField(max_length=50, blank=True, null=True***REMOVED***
    available = models.IntegerField(blank=True, null=True***REMOVED***
    taken = models.IntegerField(blank=True, null=True***REMOVED***
    waiting = models.IntegerField(blank=True, null=True***REMOVED***
    status = models.CharField(max_length=20, blank=True, null=True***REMOVED***
    days = models.CharField(max_length=5, blank=True, null=True***REMOVED***
    start = models.IntegerField(blank=True, null=True***REMOVED***
    end = models.IntegerField(blank=True, null=True***REMOVED***
    building = models.CharField(max_length=30, blank=True, null=True***REMOVED***
    room = models.CharField(max_length=10, blank=True, null=True***REMOVED***

    class Meta:
        managed = False
        db_table = 'sections'

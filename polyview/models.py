# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from polysearch.models import Courses, Sections

class Profile(models.Model***REMOVED***:
    user = models.OneToOneField(User, on_delete=models.CASCADE***REMOVED***
    followed = models.ManyToManyField(Courses, blank=True***REMOVED***
    checked = models.ManyToManyField(Sections, blank=True***REMOVED***

    def __unicode__(self***REMOVED***:
        return self.user.first_name  + self.user.last_name

    @receiver(post_save, sender=User***REMOVED***
    def create_user_profile(sender, instance, created, **kwargs***REMOVED***:
        if created:
            Profile.objects.create(user=instance***REMOVED***
    
    @receiver(post_save, sender=User***REMOVED***
    def save_user_profile(sender, instance, **kwargs***REMOVED***:
        instance.profile.save(***REMOVED***
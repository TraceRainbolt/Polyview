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
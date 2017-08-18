# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline***REMOVED***:
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin***REMOVED***:
    inlines = (ProfileInline, ***REMOVED***

    def get_inline_instances(self, request, obj=None***REMOVED***:
        if not obj:
            return list(***REMOVED***
        return super(CustomUserAdmin, self***REMOVED***.get_inline_instances(request, obj***REMOVED***

admin.site.unregister(User***REMOVED***
admin.site.register(User, CustomUserAdmin***REMOVED***
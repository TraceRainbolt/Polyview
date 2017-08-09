# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from models import Sections
from .forms import ClassForm
from django.template import loader
from django.http import HttpResponseRedirect
import form_data

from itertools import groupby
import form_data

def get_classes(request***REMOVED***:
    form = ClassForm(request.POST or None***REMOVED***
    if form.is_valid(***REMOVED***:
        search_results, results_count = find_classes(form***REMOVED***
        context = { 'form' : form, 
                    'search_results' : search_results, 
                    'full_dep' : form_data.departments,
                    'results_count': results_count***REMOVED***
        return render(request, 'polysearch/search.html', context***REMOVED***
    return render(request, 'polysearch/search.html', {'form' : form ***REMOVED******REMOVED***

def find_classes(form***REMOVED***:  
    parameters = {'department' : form.cleaned_data['class_department'***REMOVED***,
                  'instructor' : form.cleaned_data['class_instructor'***REMOVED***, 
                  'status'     : form.cleaned_data['class_status'***REMOVED***,
                  'class'      : form.cleaned_data['class_field'***REMOVED***,
                  'taken'      : form.cleaned_data['class_taken'***REMOVED***,
                  'avail'      : form.cleaned_data['class_avail'***REMOVED***,
                  'wait'       : form.cleaned_data['class_wait'***REMOVED***,
                  'building'   : form.cleaned_data['class_building'***REMOVED***,
                  'rating_min' : form.cleaned_data['class_rating_min'***REMOVED***,***REMOVED***
    return parse_results(Sections.objects.all(***REMOVED***, parameters***REMOVED***

def parse_results(results, parameters***REMOVED***:
    # Only filter results if user entered value (some reuqire None check as blank number field = 0***REMOVED***
    for key, value in parameters.items(***REMOVED***:
        if key == 'department' and value:
            results = results.filter(course__in=value***REMOVED***
        if key == 'status' and value:
            results = results.filter(status=value***REMOVED***
        if key == 'instructor' and value:
            results = results.filter(instructor__icontains=value***REMOVED***
        if key == 'class' and value:
            results = results.filter(class_field=value***REMOVED***
        if key == 'taken' and value is not None:
            results = results.filter(taken__gte=value***REMOVED***
        if key == 'avail' and value is not None:
            results = results.filter(available__gte=value***REMOVED***
        if key == 'wait' and value is not None:
            results = results.filter(waiting__gte=value***REMOVED***
        if key == 'building' and value:
            results = results.filter(building__icontains=value***REMOVED***
        if key == 'rating_min' and value is not None:
            results = results.filter(rating__gte=value***REMOVED***
    return group_by_heiarchy(results***REMOVED***, len(results***REMOVED***

def group_by_heiarchy(results***REMOVED***:
    # This is so the template can render the courses/sections grouped properly
    results = ([list(j***REMOVED*** for i, j in groupby(results, lambda x: x.course***REMOVED******REMOVED******REMOVED***
    for k, result in enumerate(results***REMOVED***:
        results[k***REMOVED*** = ([list(j***REMOVED*** for i, j in groupby(result, lambda x: x.course_num***REMOVED******REMOVED******REMOVED***
    return results

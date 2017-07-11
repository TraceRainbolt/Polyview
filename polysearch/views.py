# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from models import Sections
from .forms import ClassForm
from django.template import loader
from django.http import HttpResponseRedirect

from itertools import groupby

def get_class(request***REMOVED***:
    if request.method == 'POST':
        form = ClassForm(request.POST***REMOVED***
        if form.is_valid(***REMOVED***:
            search_results = find_classes(form***REMOVED***
            context = { 'form' : form, 'search_results' : search_results ***REMOVED***
            return render(request, 'polysearch/index.html', context***REMOVED***
    else:
        form = ClassForm(***REMOVED***
    return render(request, 'polysearch/index.html', {'form' : form ***REMOVED******REMOVED***

def find_classes(form***REMOVED***:
    class_department = form.cleaned_data['class_department'***REMOVED***
    class_status = form.cleaned_data['class_status'***REMOVED***
    class_instructor = form.cleaned_data['class_instructor'***REMOVED***
    class_field = form.cleaned_data['class_field'***REMOVED***
    class_taken = form.cleaned_data['class_taken'***REMOVED***
    class_avail = form.cleaned_data['class_avail'***REMOVED***
    class_wait = form.cleaned_data['class_wait'***REMOVED***
    class_building = form.cleaned_data['class_building'***REMOVED***
    results  = Sections.objects.all(***REMOVED***
    
    parameters = {'department' : class_department,
                  'instructor' : class_instructor, 
                  'status' : class_status,
                  'class' : class_field,
                  'taken' : class_taken,
                  'avail' : class_avail,
                  'wait' : class_wait,
                  'building' : class_building***REMOVED***

    for key, value in parameters.items(***REMOVED***:
        if key == 'department' and value:
            results = results.filter(course=value***REMOVED***
        if key == 'status' and value:
            results = results.filter(status=value***REMOVED***
        if key == 'instructor' and value:
            results = results.filter(instructor__icontains=value***REMOVED***
        if key == 'class' and value:
            results = results.filter(class_field=value***REMOVED***
        if key == 'taken' and value is not None:
            results = results.filter(taken=value***REMOVED***
        if key == 'avail' and value is not None:
            results = results.filter(available=value***REMOVED***
        if key == 'wait' and value is not None:
            results = results.filter(waiting=value***REMOVED***
        if key == 'building' and value:
            results = results.filter(building__icontains=value***REMOVED***
    results = ([list(j***REMOVED*** for i, j in groupby(results, lambda x: x.course***REMOVED******REMOVED******REMOVED***
    return results

def index(request***REMOVED***:
    search_results = Sections.objects.order_by('class_field'***REMOVED***
    context = {
        'search_results' : search_results,
***REMOVED***
    
    return render(request, 'polysearch/index.html', context***REMOVED***

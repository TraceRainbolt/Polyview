# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Courses, Sections
from .forms import CourseForm, SectionForm
from django.template import loader
import form_data
from django.views.decorators.csrf import csrf_exempt

from itertools import groupby
import form_data

MAX_RESULTS = 500


def get_classes(request***REMOVED***:
    if 'section-search' in request.POST:
        return sectionSearchView(request***REMOVED***
    else:
        return courseSearchView(request***REMOVED***
    return render(request, 'polysearch/search.html'***REMOVED***


def sectionSearchView(request***REMOVED***:
    form = SectionForm(request.POST or None***REMOVED***
    if form.is_valid(***REMOVED***:
        search_results, results_count = find_sections(form, 'section', request***REMOVED***
        context = {'form': form,
                   'search_results': search_results,
                   'results_type'  : "section",
                   'full_dep'      : form_data.departments,
                   'results_count' : results_count***REMOVED***
        return render(request, 'polysearch/search.html', context***REMOVED***
    return render(request, 'polysearch/search.html', {'form': form***REMOVED******REMOVED***


def courseSearchView(request***REMOVED***:
    form = CourseForm(request.POST or None***REMOVED***
    course_info = ('course_ac', 'course_num', 'data_id'***REMOVED***
    user = request.user
    if user.is_authenticated:
        user_followed_names = user.profile.followed.values(*course_info***REMOVED***
    else:
        user_followed_ids = request.session.get('data_ids'***REMOVED***
        if user_followed_ids:
            user_followed_names = Courses.objects.all(***REMOVED***.filter(
                data_id__in=user_followed_ids***REMOVED***.values(*course_info***REMOVED***
        else:
            user_followed_names = None
    if form.is_valid(***REMOVED***:
        search_results, results_count = find_sections(form, 'course', request***REMOVED***
        if user.is_authenticated:
            user_followed = query_values(user.profile.followed, 'data_id'***REMOVED***
        else:
            user_followed = request.session.get('data_ids'***REMOVED***
        context = {'form'          : form,
                   'search_results': search_results,
                   'results_type'  : "course",
                   'full_dep'      : form_data.departments,
                   'results_count' : results_count,
                   'user_followed' : user_followed,
                   'user_followed_names' :  user_followed_names***REMOVED***
        return render(request, 'polysearch/search.html', context***REMOVED***
    return render(request, 'polysearch/search.html', {'form': form, 'user_followed_names' :  user_followed_names***REMOVED******REMOVED***


def find_sections(form, page, request***REMOVED***:
    if page == 'course':
        parameters = {'department': form.cleaned_data['class_department'***REMOVED***,
                      'area'      : form.cleaned_data['class_area'***REMOVED******REMOVED***
        return parse_results_courses(Courses.objects.all(***REMOVED***, parameters***REMOVED***
    elif page == 'section':
        parameters = {'instructor': form.cleaned_data['class_instructor'***REMOVED***,
                      'status'    : form.cleaned_data['class_status'***REMOVED***,
                      'section'   : form.cleaned_data['class_field'***REMOVED***,
                      'taken'     : form.cleaned_data['class_taken'***REMOVED***,
                      'avail'     : form.cleaned_data['class_avail'***REMOVED***,
                      'wait'      : form.cleaned_data['class_wait'***REMOVED***,
                      'building'  : form.cleaned_data['class_building'***REMOVED***,
                      'rating_min': form.cleaned_data['class_rating_min'***REMOVED***, ***REMOVED***
        if request.user.is_authenticated:
            user_courses = request.user.profile.followed.all(***REMOVED***.values('data_id'***REMOVED***
        else:
            user_courses = request.session.get('data_ids'***REMOVED***
        query_set = Sections.objects.all(***REMOVED***.filter(course_id__in=user_courses***REMOVED***
        return parse_results_sections(query_set, parameters***REMOVED***


def parse_results_courses(results, parameters***REMOVED***:
    for key, value in parameters.items(***REMOVED***:
        if key == 'department':
            results = results.filter(course_ac__in=value***REMOVED***
    results = ([list(j***REMOVED*** for i, j in groupby(results, lambda x: x.course_ac***REMOVED******REMOVED******REMOVED***
    return results, len(results***REMOVED***


def parse_results_sections(results, parameters***REMOVED***:
    # Only filter results if user entered value (some reuqire None check as
    # blank number field = 0***REMOVED***
    for key, value in parameters.items(***REMOVED***:
        if key == 'status' and value:
            results = results.filter(status=value***REMOVED***
        if key == 'instructor' and value:
            results = results.filter(instructor__icontains=value***REMOVED***
        if key == 'section' and value:
            results = results.filter(section_field=value***REMOVED***
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
    return group_by_heiarchy(results[:MAX_RESULTS***REMOVED******REMOVED***, len(results[:MAX_RESULTS***REMOVED******REMOVED***


@csrf_exempt
def add_selected_course(request***REMOVED***:
    course_id =  request.POST.get('course_id', None***REMOVED***
    course = Courses.objects.all(***REMOVED***.get(data_id=course_id***REMOVED***
    if request.user.is_authenticated:
        request.user.profile.followed.add(course***REMOVED***
    else:
        if 'data_ids' in request.session:
            if course.data_id not in request.session['data_ids'***REMOVED***:
                request.session['data_ids'***REMOVED*** += [course.data_id***REMOVED***
        else:
            request.session['data_ids'***REMOVED*** = [course.data_id***REMOVED***
    return JsonResponse({ 'course' :course.course_ac, 
        'course_num' : course.course_num ***REMOVED******REMOVED***

@csrf_exempt
def remove_selected_course(request***REMOVED***:
    course_id =  request.POST.get('course_id', None***REMOVED***
    course = Courses.objects.all(***REMOVED***.get(data_id=course_id***REMOVED***
    if request.user.is_authenticated:
        request.user.profile.followed.remove(course***REMOVED***
    else:
        if 'data_ids' in request.session:
            data_ids = request.session['data_ids'***REMOVED***
            data_ids.remove(course.data_id***REMOVED***
            request.session['data_ids'***REMOVED*** = data_ids
        else:
            print "Error: User removing class when no classes following."
    return JsonResponse({ 'course' :course.course_ac, 
        'course_num' : course.course_num ***REMOVED******REMOVED***



def group_by_heiarchy(results***REMOVED***:
    # This is so the template can render the courses/sections grouped properly
    results = ([list(j***REMOVED*** for i, j in groupby(results, lambda x: x.course_id.course_ac***REMOVED******REMOVED******REMOVED***
    for k, result in enumerate(results***REMOVED***:
        results[k***REMOVED*** = ([list(j***REMOVED***
        for i, j in groupby(result, lambda x: x.course_id.course_num***REMOVED******REMOVED******REMOVED***
    return results

def query_values(query_set, *values***REMOVED***:
    query_set = query_set.values(*values***REMOVED***
    query_set =  [x.values(***REMOVED***[0***REMOVED*** for x in query_set***REMOVED***
    return query_set

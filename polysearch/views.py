# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import groupby

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Courses, Sections
from .forms import CourseForm, SectionForm
from django.template import loader
import form_data
from django.views.decorators.csrf import csrf_exempt

import form_data
from scheduler import Schedule, SectionCombo

MAX_RESULTS = 500

def search_view(request***REMOVED***:
    if 'section-search' in request.POST:
        return section_search_view(request***REMOVED***
    if 'schedule-search' in request.POST:
        return schedule_search_view(request***REMOVED***
    else:
        return course_search_view(request***REMOVED***
    return render(request, 'polysearch/search.html'***REMOVED***


def section_search_view(request***REMOVED***:
    form = SectionForm(request.POST or None***REMOVED***
    session_sections = request.session.get('sections_checked'***REMOVED***
    sections_checked = session_sections if session_sections else [***REMOVED***
    if form.is_valid(***REMOVED***:
        search_results, results_count = find_classes(request, form***REMOVED***
        context = {'form': form,
                   'search_results': search_results,
                   'full_dep'      : form_data.departments,
                   'results_count' : results_count,
                   'sections_checked' : sections_checked***REMOVED***
        return render(request, 'polysearch/results_pages/section_search.html', context***REMOVED***
    return render(request, 'polysearch/results_pages/course_search.html', 
    ***REMOVED***'form': form, 'sections_checked' : sections_checked***REMOVED******REMOVED***


def course_search_view(request***REMOVED***:
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
            user_followed_names = [***REMOVED***
    if form.is_valid(***REMOVED***:
        search_results, results_count = find_sections(request, form***REMOVED***
        if user.is_authenticated:
            user_followed = query_values(user.profile.followed, 'data_id'***REMOVED***
        else:
            user_followed = request.session.get('data_ids', [***REMOVED******REMOVED***
        context = {'form'          : form,
                   'search_results': search_results,
                   'full_dep'      : form_data.departments,
                   'results_count' : results_count,
                   'user_followed' : user_followed,
                   'user_followed_names' :  user_followed_names ***REMOVED***
        return render(request, 'polysearch/results_pages/course_search.html', context***REMOVED***
    return render(request, 'polysearch/results_pages/course_search.html', 
    ***REMOVED***'form': form, 'user_followed_names' :  user_followed_names ***REMOVED******REMOVED***


def schedule_search_view(request***REMOVED***:
    form = SectionForm(request.POST or None***REMOVED***
    schedule_results = find_schedules(request***REMOVED***
    if form.is_valid(***REMOVED***:
        search_results = None
        context = {'form': form,
                   'search_results': search_results,***REMOVED***
        return render(request, 'polysearch/results_pages/schedule_search.html', context***REMOVED***
    return render(request, 'polysearch/results_pages/schedule_search.html', {'form': form***REMOVED******REMOVED***


def find_schedules(request***REMOVED***:
    course_ids = request.session.get('sections_checked', [***REMOVED******REMOVED***
    available_sections = Sections.objects.all(***REMOVED***.filter(class_field__in=course_ids***REMOVED***
    parse_schedules(available_sections, course_ids***REMOVED***


def find_sections(request, form***REMOVED***:
    parameters = {'department': form.cleaned_data['class_department'***REMOVED***,
                  'area'      : form.cleaned_data['class_area'***REMOVED******REMOVED***
    return parse_results_courses(Courses.objects.all(***REMOVED***, parameters***REMOVED***

def find_classes(request, form***REMOVED***:
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
        user_courses = request.session.get('data_ids', [***REMOVED******REMOVED***
    query_set = Sections.objects.all(***REMOVED***.filter(course_id__in=user_courses***REMOVED***
    return parse_results_sections(query_set, parameters***REMOVED***

def parse_schedules(sections, course_ids***REMOVED***:
    course_info = sections.order_by('course_id'***REMOVED***.values('course_id', 'sec_group', 'days','start', 'end'***REMOVED***
    print course_info[0***REMOVED***['end'***REMOVED***

    # course_groups = [list(j***REMOVED*** for _, j in groupby(course_info, lambda x: x.get('course_id'***REMOVED******REMOVED******REMOVED***
    # for i, group in enumerate(course_groups***REMOVED***:
    #     course_groups[i***REMOVED*** = [tuple(j***REMOVED*** for _, j in groupby(group, lambda x: x.get('sec_group'***REMOVED******REMOVED******REMOVED***

    # for course in course_groups:
    #     for section in course:
    #         find_fit_courses(course_groups, section***REMOVED***


def find_fit_courses(course_groups, section***REMOVED***:
    course_groups.remove(section***REMOVED***
    for course in course_groups:
        for section_group in course:
            time_compatible(section, new_section***REMOVED***

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


@csrf_exempt
def add_selected_course(request***REMOVED***:
    course_id =  request.POST.get('course_id', None***REMOVED***
    course = Courses.objects.all(***REMOVED***.get(data_id=course_id***REMOVED***
    if request.user.is_authenticated:
        request.user.profile.followed.add(course***REMOVED***
    else:
        if 'data_ids' in request.session:
            if course.data_id not in request.session['data_ids'***REMOVED***:
                request.session['data_ids'***REMOVED***.append(course.data_id***REMOVED***
                request.session.modified = True
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
            request.session['data_ids'***REMOVED***.remove(course.data_id***REMOVED***
            request.session.modified = True
        else:
            print "Error: User removing class when no classes following."
    return JsonResponse({ 'course' :course.course_ac, 
        'course_num' : course.course_num ***REMOVED******REMOVED***


@csrf_exempt
def add_section(request***REMOVED***:
    class_num =  request.POST.get('class_num', None***REMOVED***
    section = Sections.objects.all(***REMOVED***.get(class_field=class_num***REMOVED***
    if 'sections_checked' in request.session:
        request.session['sections_checked'***REMOVED***.append(section.class_field***REMOVED***
        request.session.modified = True
    else:
        request.session['sections_checked'***REMOVED*** = [section.class_field***REMOVED***
    return JsonResponse({ 'class_num' : section.class_field ***REMOVED******REMOVED***


@csrf_exempt
def remove_section(request***REMOVED***:
    class_num =  request.POST.get('class_num', None***REMOVED***
    if 'sections_checked' in request.session:
        request.session['sections_checked'***REMOVED***.remove(int(class_num***REMOVED******REMOVED***
        request.session.modified = True
    else:
        print "Error: User removing section when no sections following."
    return JsonResponse({ 'class_num' : int(class_num***REMOVED*** ***REMOVED******REMOVED***




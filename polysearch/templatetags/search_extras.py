from django.template.defaulttags import register
from django import template
from django.forms import CheckboxSelectMultiple

@register.filter
def get_item(dictionary, key***REMOVED***:
    return dictionary.get(key***REMOVED***

@register.filter(name='is_checkbox'***REMOVED***
def is_checkbox(field***REMOVED***:
    return field.field.widget.__class__.__name__ == CheckboxSelectMultiple(***REMOVED***.__class__.__name__


@register.filter(name='time_display'***REMOVED***
def time_display(count***REMOVED***:
    hour = (count / 2***REMOVED*** + 7
    fmt = "pm" if hour >= 12 else "am"
    hour = hour if hour <= 12 else hour - 12
    return "{***REMOVED*** {***REMOVED***".format(hour, fmt***REMOVED***
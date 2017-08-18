from django.template.defaulttags import register
from django import template
from django.forms import CheckboxSelectMultiple

@register.filter
def get_item(dictionary, key***REMOVED***:
    return dictionary.get(key***REMOVED***

@register.filter(name='is_checkbox'***REMOVED***
def is_checkbox(field***REMOVED***:
  return field.field.widget.__class__.__name__ == CheckboxSelectMultiple(***REMOVED***.__class__.__name__
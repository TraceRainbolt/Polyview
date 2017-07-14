from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key***REMOVED***:
    return dictionary.get(key***REMOVED***
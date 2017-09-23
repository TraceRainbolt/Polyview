from django import forms

class FilteredSelectMultiple(forms.SelectMultiple***REMOVED***:
    ***REMOVED***
    A SelectMultiple with a JavaScript filter interface.

    Note that the resulting JavaScript assumes that the jsi18n
    catalog has been loaded in the page

    This has been repurposed for my own use, and was originally
    for the django admin console.
    ***REMOVED***

    @property
    def media(self***REMOVED***:
        js = ["core.js", "SelectBox.js", "SelectFilter2.js"***REMOVED***
        return forms.Media(js=["admin/js/%s" % path for path in js***REMOVED******REMOVED***

    def __init__(self, verbose_name, is_stacked, attrs=None, choices=(***REMOVED******REMOVED***:
        self.verbose_name = verbose_name
        self.is_stacked = is_stacked
        super(FilteredSelectMultiple, self***REMOVED***.__init__(attrs, choices***REMOVED***

    def get_context(self, name, value, attrs***REMOVED***:
        context = super(FilteredSelectMultiple, self***REMOVED***.get_context(name, value, attrs***REMOVED***
        context['widget'***REMOVED***['attrs'***REMOVED***['class'***REMOVED*** = 'selectfilter'
        if self.is_stacked:
            context['widget'***REMOVED***['attrs'***REMOVED***['class'***REMOVED*** += 'stacked'
        context['widget'***REMOVED***['attrs'***REMOVED***['data-field-name'***REMOVED*** = self.verbose_name
        context['widget'***REMOVED***['attrs'***REMOVED***['data-is-stacked'***REMOVED*** = int(self.is_stacked***REMOVED***
        return context
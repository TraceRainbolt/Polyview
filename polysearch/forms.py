from django import forms
from models import Sections
import form_data

class ClassForm(forms.Form***REMOVED***:
    class_department = forms.MultipleChoiceField(label='Department:',choices=form_data.department_choices, widget = forms.CheckboxSelectMultiple, required=False***REMOVED***
    class_instructor = forms.CharField(label='Instructor name:', max_length=50,required=False***REMOVED***
    class_status = forms.ChoiceField(label='Class status:',choices=form_data.status_choices, required=False***REMOVED***
    class_field = forms.IntegerField(label='Class #:',max_value=9999,required=False***REMOVED***
    class_taken = forms.IntegerField(label='Min. Taken:',max_value=999,required=False***REMOVED***
    class_avail = forms.IntegerField(label='Min. Available:',max_value=999,required=False***REMOVED***
    class_wait  = forms.IntegerField(label='Min. Waiting:',max_value=999,required=False***REMOVED***
    class_building = forms.CharField(label='Building:',max_length=50, required=False***REMOVED***
    class_rating_min = forms.DecimalField(label='Min. Polyrating:', max_digits = 3, max_value=4,min_value=0, required=False***REMOVED***
    # class_rating_max = forms.DecimalField(label='Maximum Polyrating:', max_digits = 3, max_value=4,min_value=0, required=False***REMOVED***
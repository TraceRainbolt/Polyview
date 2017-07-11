from django import forms
from models import Sections
import form_data

class ClassForm(forms.Form***REMOVED***:
    class_department = forms.ChoiceField(label='Department:',choices=form_data.department_choices, required=False***REMOVED***
    class_instructor = forms.CharField(label='Instructor name:', max_length=50,required=False***REMOVED***
    class_status = forms.ChoiceField(label='Class status:',choices=form_data.status_choices, required=False***REMOVED***
    class_field = forms.IntegerField(label='Class #:',max_value=9999,required=False***REMOVED***
    class_taken = forms.IntegerField(label='Taken:',max_value=999,required=False***REMOVED***
    class_avail = forms.IntegerField(label='Available:',max_value=999,required=False***REMOVED***
    class_wait  = forms.IntegerField(label='Waiting:',max_value=999,required=False***REMOVED***
    class_building = forms.CharField(label='Building:',max_length=50, required=False***REMOVED***

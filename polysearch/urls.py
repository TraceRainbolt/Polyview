from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    url(r'^$', views.get_classes, name='search'***REMOVED***,
    url(r'^ajax/add_course/$', views.add_selected_course, name='add_course'***REMOVED***,
    url(r'^ajax/remove_course/$', views.remove_selected_course, name='remove_course'***REMOVED***,
***REMOVED***
 
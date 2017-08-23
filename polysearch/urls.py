from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    url(r'^$', views.search_view, name='search'***REMOVED***,
    url(r'^ajax/add_course/$', views.add_selected_course, name='add_course'***REMOVED***,
    url(r'^ajax/remove_course/$', views.remove_selected_course, name='remove_course'***REMOVED***,
    url(r'^ajax/add_section/$', views.add_section, name='add_section'***REMOVED***,
    url(r'^ajax/remove_section/$', views.remove_section, name='remove_section'***REMOVED***,
***REMOVED***
 
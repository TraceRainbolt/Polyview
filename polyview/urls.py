***REMOVED***polyview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home'***REMOVED***
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(***REMOVED***, name='home'***REMOVED***
Including another URLconf
    1. Import the include(***REMOVED*** function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'***REMOVED******REMOVED***
***REMOVED***
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="polyview/home.html"***REMOVED***, name="home"***REMOVED***,
    url(r"^soc/", include("social.apps.django_app.urls", namespace="social"***REMOVED***, name="signin"***REMOVED***,
    url(r'^profile/', include('polyprofile.urls'***REMOVED***, name="profile"***REMOVED***,
    url(r'^search/', include('polysearch.urls'***REMOVED***, name="search"***REMOVED***,
    url(r'^about/', TemplateView.as_view(template_name="polyview/about.html"***REMOVED***, name="about"***REMOVED***,
    url('^', include('django.contrib.auth.urls'***REMOVED******REMOVED***,
    url(r'^admin/', admin.site.urls***REMOVED***,
***REMOVED***

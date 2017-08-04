***REMOVED***
WSGI config for polyview project.

It exposes the WSGI callable as a module-level variable named ``application``.

***REMOVED***
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
***REMOVED***
***REMOVED***
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/webapps/polyview_env/local/lib/python2.7/site-packages'***REMOVED***

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/webapps/polyview_app'***REMOVED***
sys.path.append('/home/webapps/polyview_app/polyview'***REMOVED***

os.environ['DJANGO_SETTINGS_MODULE'***REMOVED*** = 'polyview.settings.production'

# Activate your virtual env
activate_env=os.path.expanduser("B:\Projects\Other Projects\Polyview\polyview_env\Scripts\\activate_this.py"***REMOVED***
execfile(activate_env, dict(__file__=activate_env***REMOVED******REMOVED***

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application(***REMOVED***

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application(***REMOVED***

***REMOVED***

os.environ['DJANGO_SETTINGS_MODULE'***REMOVED*** = 'mysite.settings'

os.environ['DJANGO_CONFIGURATION'***REMOVED*** = 'Production'
os.environ['DJANGO_SECRET_KEY'***REMOVED*** = 'RANDOM_SECRET_KEY_HERE'
os.environ['DJANGO_AWS_ACCESS_KEY_ID'***REMOVED*** = 'YOUR_AWS_ID_HERE'
os.environ['DJANGO_AWS_SECRET_ACCESS_KEY'***REMOVED*** = 'YOUR_AWS_SECRET_ACCESS_KEY_HERE'
os.environ['DJANGO_AWS_STORAGE_BUCKET_NAME'***REMOVED*** = 'YOUR_AWS_S3_BUCKET_NAME_HERE'
os.environ['SENDGRID_USERNAME'***REMOVED*** = 'YOUR_SENDGRID_USERNAME'
os.environ['SENDGRID_PASSWORD'***REMOVED*** = 'YOUR_SENDGRID_PASSWORD'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application(***REMOVED***
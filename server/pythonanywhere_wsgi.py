import os
import sys

path = '/home/jensenry/pets_api/server'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
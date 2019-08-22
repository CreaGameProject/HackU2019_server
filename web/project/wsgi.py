import os
from django.core.wsgi import get_wsgi_application

settings = 'project.settings.' + ('dev' if os.environ['DEBUG'] == 'true' else 'prod')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
application = get_wsgi_application()

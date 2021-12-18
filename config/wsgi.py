import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('APP_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_dev')

application = get_wsgi_application()

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'letslearn.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=(settings.BASE_DIR / "staticroot") )
application.add_files(settings.BASE_DIR / "mediafiles", prefix="mediafiles/")
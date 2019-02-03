# Import all the regular settings from settings.py but override some for development
from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["your-ip-or-hostname"]

import os
import json

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "/django/unimportantFile.json")) as secrets_file:
    settings = json.load(secrets_file)

admin_user = django.contrib.auth.models.User.objects.create_superuser(
   username=settings["ADMIN_USERNAME"],
   email=settings["ADMIN_EMAIL"],
   password=settings["ADMIN_PASSWORD"])

admin_user.save()

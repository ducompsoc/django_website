import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# Namespace app
app_name = 'events'

urlpatterns = [
    # ex: / the root of the django app
    path('', views.IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=os.path.join(settings.MEDIA_ROOT, 'events/static/events/img'))   # Not good in production

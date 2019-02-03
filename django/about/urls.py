from django.urls import path

from . import views

# Namespace app
app_name = 'about'

urlpatterns = [
    # ex: / the root of the django app
    path('', views.IndexView.as_view(), name='index'),
]

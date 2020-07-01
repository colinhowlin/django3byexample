"""Module for defining URL patterns and routes"""

from django.urls import path
from . import views

# Namespace
app_name = 'root_site'

urlpatterns = [
    path('', views.index, name='root_site_index'),
]
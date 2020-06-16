"""Module for defining URL patterns and routes"""

from django.urls import path
from . import views

# Namespace
app_name = 'blog'

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]

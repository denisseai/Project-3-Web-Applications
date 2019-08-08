"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #Include auth urls.
    path('', include('django.contrib.auth.urls')),
    #Register page
    path('register/', views.register, name='register'),
]

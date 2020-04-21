"""Youtube app resource configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main')
]

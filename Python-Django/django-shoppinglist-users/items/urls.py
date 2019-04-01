"""items URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
    path('<name>', views.item, name='item')
]

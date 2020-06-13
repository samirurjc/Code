from django.urls import path

from .views import MainView, UploadView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('upload/', UploadView.as_view(), name='upload')
]
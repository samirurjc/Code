from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import UploadForm
from .models import Image

class MainView(ListView):
    model = Image
    template_name = 'main.html'

class UploadView(CreateView):
    model = Image
    form_class = UploadForm
    template_name = 'upload.html'
    success_url = reverse_lazy('main')
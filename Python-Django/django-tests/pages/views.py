from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import ContentForm
from .models import Page

class Counter():

    def __init__(self):
        self.count: int = 0;

    def increment(self) -> int:
        self.count += 1;
        return(self.count)

counter: Counter = Counter()

def index(request):

    pages = Page.objects.all()
    return(render(request, 'pages/index.html', {'item_list': pages}))

def page(request, name):

    if request.method == 'POST':
        try:
            p = Page.objects.get(name=name)
        except Page.DoesNotExist:
            p = Page(name=name)
        form = ContentForm(request.POST)
        if form.is_valid():
            p.content = form.cleaned_data['content']
            p.save()

    if request.method == 'GET' or request.method == 'POST':
        try:
            p = Page.objects.get(name=name)
            content_form = ContentForm(initial={'content': p.content})
            status = 200
        except Page.DoesNotExist:
            content = "Page " + name + " not found."
            content_form = ContentForm()
            status = 404
        content_template = loader.get_template('pages/content.html')
        content_html = content_template.render({'page': name,
                                                'form': content_form},
                                               request)
        return(HttpResponse(content_html, status=status))

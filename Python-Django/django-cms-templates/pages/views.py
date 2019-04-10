from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Page

def index(request):

    pages = Page.objects.all()
    return(render(request, 'pages/index.html', {'item_list': pages}))

@csrf_exempt
def page(request, name):

    if request.method == 'PUT':
        try:
            p = Page.objects.get(name=name)
        except Page.DoesNotExist:
            p = Page(name=name)
        p.content = request.body.decode("utf-8")
        p.save()

    if request.method == 'GET' or request.method == 'PUT':
        try:
            p = Page.objects.get(name=name)
            content = p.content
            status = 200
        except Page.DoesNotExist:
            content = "Page " + name + " not found."
            status = 404
        main_template = loader.get_template('pages/main.html')
        main_html = main_template.render({'content': content}, request)
        return(HttpResponse(main_html, status=status))

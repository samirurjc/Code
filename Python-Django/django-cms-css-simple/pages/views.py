from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Page

html_template = """<!DOCTYPE html>
<html lang="en" >
  <head>
    <meta charset="utf-8" />
    <title>Django CMS</title>
  </head>
  <body>
    {body}
  </body>
</html>
"""

html_item_template = "<li><a href='{name}'>{name}</a></li>"

def index(request):

    pages = Page.objects.all()
    if len(pages) == 0:
        body = "No pages yet."
    else:
        body = "<ul>"
        for p in pages:
            body += html_item_template.format(name=p.name)
        body += "</ul>"
    return(HttpResponse(html_template.format(body=body)))

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
            if name.endswith('.css'):
                content_type='text/css'
            else:
                content_type='text/html'
            response = HttpResponse(content,content_type=content_type)
        except Page.DoesNotExist:
            response = HttpResponseNotFound("Page " + name + " not found")
        return(response)

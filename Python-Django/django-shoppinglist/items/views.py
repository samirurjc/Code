from django.http import HttpResponse
from django.middleware.csrf import get_token

# Create your views here.

html_template = """<!DOCTYPE html>
<html lang="en" >
  <head>
    <meta charset="utf-8" />
    <title>Shopping list</title>
  </head>
  <body>
    {content}
  </body>
</html>
"""

item_page_template = """<p><a href="/">Full shopping list</a></p>
<h2>Item: {name}</h2>
<form action="/{name}" method="POST">
  Quantity to shop: <input name="value" type="number" value="{quantity}"/>
  <input type="submit" value="Change" />
  <input type="hidden" name="csrfmiddlewaretoken" value="{token}" />
</form>
"""

item_template = """
<li><a href="/{name}">{name}</a>: {quantity}</li> 
"""

usual_items = ['milk', 'bread', 'oranges', 'butter', 'apples']

usual_item_template = '<a href="/{name}">{name}</a> '

items = {}

def index(request):

    list = "<ul>"
    for name in items:
        list += item_template.format(name=name, quantity=items[name])
    list += "</ul>"

    list += "<p>Usual items: "
    for name in usual_items:
        list += usual_item_template.format(name=name)
    list += "</p>"

    html = html_template.format(content="<h1>List of items to shop</h1>" + list)
    return HttpResponse(html)

def item(request, name):

    if request.method == 'POST':
        items[name] = request.POST.get('value')

    if request.method == 'GET' or request.method == 'POST':
        csrf_token = get_token(request)
        if name in items:
            quantity = str(items[name])
        else:
            quantity = '0'
        content = item_page_template.format(name=name, quantity=quantity,
                                            token=csrf_token)
        html = html_template.format(content=content)
    return HttpResponse(html)
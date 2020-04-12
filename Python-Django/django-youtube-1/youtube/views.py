"""Views for YouTube app
"""
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token

from .ytchannel import YTChannel
from . import data

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Selected</h1>
      <ul>
      {selected}
      </ul>
    <h1>Selectable</h1>
      <ul>
      {selectable}
      </ul>
  </body>
</html>
"""

VIDEO = """
      <li>
        <form action='/' method='post'>
          <a href='{link}'>{title}</a>
          <input type='hidden' name='id' value='{id}'>
          <input type='hidden' name='csrfmiddlewaretoken' value='{token}'>
          <input type='hidden' name='{name}' value='True'> 
          <input type='submit' value='{action}'>
        </form>
      </li>
"""

def build_html(name, list, action, token):

    html = ""
    for video in list:
        html = html + VIDEO.format(link=video['link'],
                                   title=video['title'],
                                   id=video['id'],
                                   name=name,
                                   action=action,
                                   token=token)
    return html


def move_video(from_list, to_list, id):

    found = None
    for i, video in enumerate(from_list):
        if video['id'] == id:
            found = from_list.pop(i)
    if found:
        to_list.append(found)


def main(request):

    if request.method == 'POST':
        if 'id' in request.POST:
            if request.POST.get('select'):
                move_video(from_list=data.selectable,
                           to_list=data.selected,
                           id=request.POST['id'])
            elif request.POST.get('deselect'):
                move_video(from_list=data.selected,
                           to_list=data.selectable,
                           id=request.POST['id'])
    csrf_token = get_token(request)
    print("Selectable:", data.selectable)
    selected = build_html(name='deselect', list=data.selected,
                          action='Deselect', token=csrf_token)
    selectable = build_html(name='select', list=data.selectable,
                            action='Select', token=csrf_token)
    htmlBody = PAGE.format(selected=selected, selectable=selectable)
    return HttpResponse(htmlBody)

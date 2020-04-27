"""Views for YouTube app
"""
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token

from .ytchannel import YTChannel
from . import models

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Django YouTube (version 2)</h1>
    <h2>Selected</h2>
      <ul>
      {selected}
      </ul>
    <h2>Selectable</h2>
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

def build_html(name, selected, action, token):

    html = ""
    videos = models.Video.objects.filter(selected=selected)
    for video in videos:
        html = html + VIDEO.format(link=video.link,
                                   title=video.title,
                                   id=video.id,
                                   name=name,
                                   action=action,
                                   token=token)
    return html


def change_video(id, selected):

    video = models.Video.objects.get(id=id)
    video.selected=selected
    video.save()

def main(request):

    if request.method == 'POST':
        if 'id' in request.POST:
            if request.POST.get('select'):
                change_video(id=request.POST['id'], selected=True)
            elif request.POST.get('deselect'):
                change_video(id=request.POST['id'], selected=False)
    csrf_token = get_token(request)
    selected = build_html(name='deselect', selected=True,
                          action='Deselect', token=csrf_token)
    selectable = build_html(name='select', selected=False,
                            action='Select', token=csrf_token)
    htmlBody = PAGE.format(selected=selected,
                                selectable=selectable)
    return HttpResponse(htmlBody)

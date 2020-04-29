"""Views for YouTube app
"""
from django.http import HttpResponse
from django.template import RequestContext, Template

from . import models

PAGE = Template("""
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Django YouTube (version 4)</h1>
    <h2>Selected</h2>
      {% include video_tmpl with list=selected name="deselect" action="Deselect" %}
    <h2>Selectable</h2>
      {% include video_tmpl with list=selectable name="select" action="Select" %}
  </body>
</html>
""")

VIDEO = Template("""
      <ul>
      {% for video in list %}
      <li>
        <form action='/' method='post'>
          {% csrf_token %}
          <a href='{{video.link}}'>{{video.title}}</a>
          <input type='hidden' name='id' value='{{video.id}}'>
          <input type='hidden' name='{{name}}' value='True'> 
          <input type='submit' value='{{action}}'>
        </form>
      </li>
      {% endfor %}
      </ul>
""")


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
    selected = models.Video.objects.filter(selected=True)
    selectable = models.Video.objects.filter(selected=False)
    htmlBody = PAGE.render(RequestContext(request,
                                          {'selected': selected,
                                           'selectable': selectable,
                                           'video_tmpl': VIDEO}))
    return HttpResponse(htmlBody)

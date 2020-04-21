"""Views for YouTube app
"""
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token

from .ytchannel import YTChannel
from . import data
from . import models


def build_html(name, selected, action, token):

    html = ""
    videos = models.Video.objects.filter(selected=selected)
    for video in videos:
        html = html + data.VIDEO.format(link=video.link,
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
    htmlBody = data.PAGE.format(selected=selected,
                                selectable=selectable)
    return HttpResponse(htmlBody)

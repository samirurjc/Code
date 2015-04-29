from django.conf.urls.defaults import *
import django.views.static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^apps/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'apps'}),

    url(r'^$', 'words_provider.words.views.gimmeindex'),
    url(r'^words/(.*)$', 'words_provider.words.views.gimmeword'),
    url(r'^prefix/(.*)/(.*)$', 'words_provider.words.views.gimmewordsprefix'),

)

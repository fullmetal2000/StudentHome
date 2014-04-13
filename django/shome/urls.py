from django.conf.urls.defaults import *
import os
from firstsite import settings
urlpatterns = patterns('',
    url(r'^$', 'shome.views.main_page'),
    url(r'^login/$', 'shome.views.user_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^create_user/$', 'shome.views.create_new_user'),
    url(r'^static_path/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.CURRENT_DIR,'../static/')})
)
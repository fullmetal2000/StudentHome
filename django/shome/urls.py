
import os
from firstsite import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework import routers
from shome import views

urlpatterns = patterns('',
    url(r'^$', 'shome.views.main_page'),
    url(r'^university/$', 'shome.views.university_info'),
    url(r'^import_csv/$', 'shome.views.add_csv'),
    url(r'^login/$', 'shome.views.user_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^create_user/$', 'shome.views.create_new_user'),
)
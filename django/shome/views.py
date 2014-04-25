# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext

import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shome.models import UniversityInfo
from shome.serializers import UniversitySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import csv

def import_csv(file_csv):
    records = csv.reader(file_csv)
    for uinfo in records:
        university = UniversityInfo.objects.filter(name = uinfo[0])
        if university.count() == 0:
            univ = UniversityInfo()
            univ.name         = uinfo[0]
            univ.url          = uinfo[1]
            univ.introduction = uinfo[2]
            univ.ranking      = uinfo[3]
            univ.studentnum   = uinfo[4]
            univ.fee          = uinfo[5]
            univ.image        = uinfo[6]
            univ.apartment    = uinfo[7]
            univ.food         = uinfo[8]
            univ.housing      = uinfo[9]
            univ.car          = uinfo[10]
            univ.translink    = uinfo[11]
            univ.shopping     = uinfo[12]
            univ.tourist      = uinfo[13]
            univ.sports       = uinfo[14]
            univ.googlemaps   = uinfo[15]
            univ.save()


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def university_info(request):
    if request.method == 'GET':
        university = UniversityInfo.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def mainpage_user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        form = AuthenticationForm(request.POST)

        if user is not None:
            if user.is_active:
                login(request, user)
                return form
            else:
                logger.error("disabled account")
                # Return a 'disabled account' error message
        else:
            logger.error("invalid login")
            # Return an 'invalid login' error message.
    else:
        form = AuthenticationForm(request)

    return form

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        form = AuthenticationForm(request.POST)

        if user is not None:
            if user.is_active:
                logger.error("valid")
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                logger.error("disabled account")
                # Return a 'disabled account' error message
        else:
            logger.error("invalid login")
            # Return an 'invalid login' error message.
    else:
        form = AuthenticationForm(request)

    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['username'].widget.attrs['placeholder'] = "用户名"
    form.fields['password'].widget.attrs['class'] = "form-control"
    form.fields['password'].widget.attrs['placeholder'] = "密码"
    #request.login_form = form
    template_user = {
        'form': form,
    }
    template_user.update(csrf(request))
    return render_to_response("login.html", template_user)

def create_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # user must be actived for login to work
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    form.fields['username'].widget.attrs['class'] = "form-control custom-form"
    form.fields['username'].widget.attrs['type'] = "email"
    form.fields['username'].widget.attrs['id'] = "inputEmail3"
    form.fields['username'].widget.attrs['placeholder'] = "Email或用户名"
    form.fields['password1'].widget.attrs['class'] = "form-control custom-form"
    form.fields['password1'].widget.attrs['type'] = "password"
    form.fields['password1'].widget.attrs['id'] = "inputPassword3"
    form.fields['password1'].widget.attrs['placeholder'] = "密码"
    form.fields['password2'].widget.attrs['class'] = "form-control custom-form"
    form.fields['password2'].widget.attrs['type'] = "password"
    form.fields['password2'].widget.attrs['id'] = "inputPassword3"
    form.fields['password1'].widget.attrs['placeholder'] = "确认密码"

    template_user = {
        'form': form,
    }
    template_user.update(csrf(request))

    return render_to_response("newuser.html", template_user)

def main_page(request):
    form = mainpage_user_login(request)
    template = {
        'user': request.user,
        'form': form,
    }
    template.update(csrf(request))
    return render_to_response("index.html", template)

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

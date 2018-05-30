# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request,'mywebpage/index.html')

def validate(request):
    errors = User.objects.validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user=User.objects.create(name=request.POST['name'],username=request.POST['username'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session ['name'] = request.POST['name']
        request.session ['id'] = user.id
        return redirect('/dashboard')

def login(request):
    errors = User.objects.login_validation(request.POST)
    if errors:
        if errors['login']  =="Successfully logged in!":
            user=User.objects.filter(username=request.POST['username'])
            request.session ['name'] = user[0].first_name
            request.session ['id'] = user[0].id
            return redirect('/dashboard')
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

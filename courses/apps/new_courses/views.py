# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request,'new_courses/index.html', {"courses":Course.objects.all()})

def add(request):
    errors = Course.objects.validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else: 
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
        return redirect('/')

def delete(request, id):
    return render(request, 'new_courses/delete.html', {"course": Course.objects.get(id=id)})

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def root(request):
    context={
        "users":User.objects.all()
    }
    return render(request,'users/index.html', context)

def show(request, id):
    return render(request, 'users/users.html',{"user":User.objects.get(id=id)})

def create(request):
    return render(request, 'users/create.html')

def submit(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/create')
    else: 
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
        print User.objects.all()
        return redirect('/users')

def edit(request, id):
    return render(request, 'users/update.html', {"user":User.objects.get(id=id)})

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return render(request, 'users/update.html', {"user":User.objects.get(id=id)})
    else: 
        user=User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')

def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')
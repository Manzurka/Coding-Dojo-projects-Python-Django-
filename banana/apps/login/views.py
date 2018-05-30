# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

# Create your views here.
def index(request):
    # if 'notification' not in request.session:
    #     request.session['notification']= " "
    return render(request,'login/index.html')

def add(request):
    errors = User.objects.validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    if not User.objects.filter(email=request.POST['email']):
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session ['name'] = request.POST['first_name']
        request.session['message'] = "Successfully registered!"
        print User.objects.all()
        print User.objects.get(id=3).password
        return redirect('/success')
    else:
        request.session['notification'] = "There is a user with this email!"
        return redirect('/')

def login(request):
    if User.objects.filter(email=request.POST['email']):
        user=User.objects.filter(email=request.POST['email'])
        if (bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode())):
            request.session ['name'] = user[0].first_name
            request.session['message'] = "Successfully logged in!"
            return redirect('/success')
        if not (bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode())):
            request.session['notification'] = "Invalid password!"
            return redirect('/')
    if not User.objects.filter(email=request.POST['email']): 
            request.session['notification'] = "Invalid  email!"
            return redirect('/')

def success(request):
    return render(request,'login/success.html')
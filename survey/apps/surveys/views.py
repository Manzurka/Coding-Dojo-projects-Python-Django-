# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def submit(request):
    request.session['time'] +=1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def show(request):
   
    context={
        "message" : "Thanks for submitting this form! You have submitted this form " + str(request.session['time']) + " times now."
    }
    
    return render(request, 'surveys/result.html', context)

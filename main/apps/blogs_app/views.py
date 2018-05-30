# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "List of blogs"
    return HttpResponse(response)

def new(request):
    response = "Create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect ('/blogs/new')

def show(request, num):
    response = "Placeholder to display block "+num
    return HttpResponse(response)

def edit(request, num):
    response = "Placeholder to edit block " +num
    return HttpResponse(response)

def destroy(request, num):
    return redirect ('/blogs')
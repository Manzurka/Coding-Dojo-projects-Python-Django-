# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    context={
        "random": get_random_string(length=14).upper
    }
    return render(request, 'hobby/index.html', context)

def generate(request):
    request.session['attempt'] += 1
    return redirect ('/')

def reset(request):
    request.session['attempt'] = 0
    return redirect ('/')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import localtime, strftime

def index(request):
    context={
            'timestamp': strftime("%b-%d-%Y %H:%M %p", localtime())
    }
    if 'list' not in request.session:
        request.session['list'] = []   
    return render(request, 'session_words/index.html', context)

def add(request):
    request.session['list'].append(request.POST)
    request.session.modified = True
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')
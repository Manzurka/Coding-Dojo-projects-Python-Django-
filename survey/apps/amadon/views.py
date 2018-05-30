# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'items' not in request.session:
        request.session['items']= 0

    if 'sum' not in request.session:
        request.session['sum']= 0

    return render(request, 'amadon/index.html')

def submit(request):
    request.session['quantity']= int(request.POST['quantity'])
    
    if request.POST['product_id'] == '001':  
        request.session['price']= 19.99
        return redirect('/amadon/checkout')

    if request.POST['product_id'] == '002':
        request.session['price']= 29.99
        return redirect('/amadon/checkout')

    if request.POST['product_id'] == '003':  
        request.session['price']= 4.99
        return redirect('/amadon/checkout')

    if request.POST['product_id'] == '004':
        request.session['price']= 49.99
        return redirect('/amadon/checkout')

    return redirect('/amadon')

def show(request):
    request.session['bill'] = request.session['price'] * request.session['quantity']
    request.session['sum'] += request.session['price'] * request.session['quantity']
    request.session['items'] += request.session['quantity']
    return render(request, 'amadon/checkout.html')



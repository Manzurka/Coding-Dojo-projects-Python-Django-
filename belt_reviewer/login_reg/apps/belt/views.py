# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def root(request):
    return render(request,'belt/index.html')

def validate(request):
    errors = User.objects.validation(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session ['name'] = request.POST['first_name']
        request.session ['id'] = user.id
        return redirect('/books')

def login(request):
    errors = User.objects.login_validation(request.POST)
    if errors:
        if errors['login']  =="Successfully logged in!":
            user=User.objects.filter(email=request.POST['email'])
            request.session ['name'] = user[0].first_name
            request.session ['id'] = user[0].id
            return redirect('/books')
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

def showbooks(request):
    context={
        "books": Book.objects.all(), 
        "reviews": Review.objects.all(), 
       
    }
    return render(request,'belt/books.html', context)

def addbook(request):
    return render(request,'belt/addbook.html', {"books": Book.objects.values('author').distinct().all()})

def submit(request):
    errors = Book.objects.book_validation(request.POST)
    if errors:  
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add')
    else:
        user=User.objects.get(id=request.session ['id'])
        if request.POST['author'] == 'none':
            author =  request.POST['new_author']
        else:
            author =  request.POST['author']
        book=Book.objects.create(name=request.POST['book_name'], author=author)
        Review.objects.create(rating=int(request.POST['rating']), content=request.POST['content'], user=user, book=book)
        print request.POST['author']
        print request.POST
        request.session ['book_id'] = book.id
        return redirect('/books')
        
def showbook(request, id):
    context={
        "book": Book.objects.get(id=id),
        "reviews": Review.objects.all()
    }
    return render(request, 'belt/showbook.html', context)

        
def showuser(request, id):
    context={
        "user": User.objects.get(id=id),
        "reviews": Review.objects.all(), 
        "count": User.objects.get(id=id).user_reviews.count()
    }

    return render(request, 'belt/showuser.html', context)

def delete(request, id):
    book=Review.objects.get(id=id).book
    Review.objects.get(id=id).delete()
    return redirect(reverse ('book:book_id', kwargs={'id': book.id}))

def addreview(request, id):
     user=User.objects.get(id=request.session ['id'])
     book=Book.objects.get(id=id)
     Review.objects.create(rating=int(request.POST['rating']), content=request.POST['content'], user=user, book=book)
     return redirect(reverse ('book:book_id', kwargs={'id': book.id}))
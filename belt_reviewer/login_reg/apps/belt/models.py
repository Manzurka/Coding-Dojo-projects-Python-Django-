# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validation(self, postData):
        errors={}
        if len(postData['first_name']) < 2:
           errors['first_name']="First Name cannot be less than 2 characters!"
        if not NAME_REGEX.match(postData['first_name']):
            errors['first_name']="Invalid First Name!"
        if len(postData['last_name']) < 2:
            errors['last_name']="Last Name cannot be less than 2 characters!"
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name']="Invalid Last Name!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Invalid Email Address!"
        if self.filter(email=postData['email']):
            errors['email']="This email is in use!"
        if len(postData['password']) < 8:
                errors['password']="Password is less than 8 characters!"
        if postData['pw_confirmation']!= postData['password']:
            errors['password']="Password should match!"
       
        return errors

    def login_validation(self, postData):
        errors={}
        if User.objects.filter(email=postData['email']):
            user=User.objects.filter(email=postData['email'])
            if (bcrypt.checkpw(postData['password'].encode(), user[0].password.encode())):
                errors['login'] = "Successfully logged in!"
            if not (bcrypt.checkpw(postData['password'].encode(), user[0].password.encode())):
               errors['login'] = "Invalid password!"
        if not User.objects.filter(email=postData['email']): 
            errors['login'] = "Invalid  email!"
        
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


class BookManager(models.Manager):
    def book_validation(self, postData):
        errors={}
        if Book.objects.filter(name=postData['book_name']):
            errors['book']="This book is already in our catalog"
       
        return errors
            

class Book(models.Model):
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BookManager()

class Review(models.Model):
    rating=models.IntegerField()
    content=models.TextField(max_length=1000)
    book=models.ForeignKey(Book, related_name= "reviews")
    user=models.ForeignKey(User, related_name = "user_reviews")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
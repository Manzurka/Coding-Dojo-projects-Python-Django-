# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
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
            errors['first_name']="First Name cannot contain numbers!"
        if len(postData['last_name']) < 2:
            errors['last_name']="Last name cannot be less than 2 characters!"
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name']="Last Name cannot contain numbers!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Invalid Email Address!"
        if len(postData['password']) < 8:
            errors['password']="Password should be 8 characters!"
        if postData['pw_confirmation']!= postData['password']:
            errors['pw_confirmation']="Password should match!"
        return errors
     

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

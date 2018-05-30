# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors["first_name"]="Name should be at least 2 characters"
        if not NAME_REGEX.match(postData['first_name']):
            errors["first_name"]= "Name cannot contain numbers"
        if len(postData['last_name'])<2:
            errors["last_name"]="Last name should be at least 2 characters"
        if not NAME_REGEX.match(postData['last_name']):
            errors["last_name"]="Last name cannot contain numbers"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"]="Invalid Email"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     age = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# def hello()
#     return self.name

    # all_users = User.objects.all() # SELECT
    # print all_users[0].hello()


# class Post(models.Model):
#     content = models.TextField
#     author = models.ForeignKey (User, related_name = "posts") # to call this function - related_name

    # Post.objects.create(content = "Hello World", author = User.object.get(id=1)) # to create post  INSERT

    # Steve = User.objects.get(id=1)
    # Steve.posts.all() # posts that Steve wrote {content} 
    # first_post = Post.objects.get(id=1)
    # print first_post.author # gives us User object {id, name, age, ..}

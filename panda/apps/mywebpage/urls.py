from django.conf.urls import url
from django.contrib import messages
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate$', views.validate),
    url(r'^login$', views.login)
    # url(r'^$', views.),
    # url(r'^$', views.),
    # url(r'^$', views.),
    # url(r'^$', views.)
]
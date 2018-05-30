from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root), # '/ninjagold'
    url(r'^/process_money$', views.process) # '/ninjagold/process_money'
   
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # '/amadon'
    url(r'^/buy$', views.submit),  # '/amadon/buy' POST
    url(r'^/checkout$', views.show) # '/amadon/checkout'
]
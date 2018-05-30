from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^/(?P<id>\d+)$', views.show),
    url(r'^/create$', views.create),
    url(r'^/users/submit$', views.submit),
    url(r'^/(?P<id>\d+)/edit$', views.edit),
    url(r'^/(?P<id>\d+)/update$', views.update),
    url(r'^/(?P<id>\d+)/delete$', views.delete)
]
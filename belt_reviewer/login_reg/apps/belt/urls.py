from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^validate$', views.validate),
    url(r'^login$', views.login),
    url(r'^books$', views.showbooks),
    url(r'^add$', views.addbook),
    url(r'^submit$', views.submit),
    url(r'^books/(?P<id>\d+)$', views.showbook, name='book_id'),
    url(r'^books/addreview/(?P<id>\d+)$', views.addreview),
    url(r'^user/(?P<id>\d+)$', views.showuser),
    url(r'^books/delete/(?P<id>\d+)$', views.delete)
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # '/session_word'
    url(r'^/add_word$', views.add),  # 'session_word/add_word'
    url(r'^/clear$', views.clear)  # 'session_word/clear'
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(?P<article_id>\d+)$', views.read, name='read'),
]

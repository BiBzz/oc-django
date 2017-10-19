from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<post_id>\d+)-(?P<post_slug>.+)$', views.read, name='read'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # /hello/create/Pawel/
    url(r'^create/(?P<person_name>[\w\-]+)/$', views.create, name='create'),

    # /hello/delete/Pawel/
    url(r'^delete/(?P<person_name>[\w\-]+)/$', views.delete, name='delete'),
]

from django.conf.urls import url, include
from . import views

urlpatterns = [    
    url(r'^/$', views.show),
    url(r'^/new', views.add),
    url(r'^/add_trip', views.add_show),
    url(r'^/detail/(?P<id>\d+)',views.detail),
    url(r'^/edit/(?P<id>\d+)', views.edit),
    url(r'^/update_trip', views.update),
    url(r'^/remove/(?P<id>\d+)', views.remove),
    url(r'^/join/(?P<id>\d+)', views.join),    
    url(r'^/pass/(?P<id>\d+)', views.pass_it),    
    url(r'^', views.index),   
    
]

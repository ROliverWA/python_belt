from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),    
    url(r'^validate_exists$', views.validate_login),
    url(r'^validate$', views.validate),
    url(r'^verify$', views.verify),        
    url(r'^success$', views.success),
    url(r'^logout$', views.peace_out),
    url(r'^check_email$', views.check_me_out)
]
import siteapp.views as siteapp
from django.urls import re_path
from django.conf.urls import handler404, handler500

app_name="siteapp"

#handler404 = siteapp.handler404
#handler500 = siteapp.handler500

urlpatterns = [
	re_path(r'^$', siteapp.home, name='home'),
	re_path(r'^new_url/$', siteapp.new_url, name='new_url'),
	re_path(r'^[a-zA-Z0-9]+$', siteapp.redirect_url, name='redirect_url'),
]
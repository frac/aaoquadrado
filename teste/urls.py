from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
import views as resource

urlpatterns = patterns('',
    url(r'^login/$', resource.login),
    url(r'^pessoa/', resource.pessoa),

)




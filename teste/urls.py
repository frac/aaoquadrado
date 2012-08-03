from django.conf.urls.defaults import *
import views as resource

urlpatterns = patterns('',
    url(r'^login/$', resource.login),
    url(r'^pessoa/(?P<token>\d+)/$', resource.pessoa),
)




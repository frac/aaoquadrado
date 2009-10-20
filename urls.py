from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^aaoquadrado/', include('aaoquadrado.foo.urls')),
    #    (r'^info/', include('aaoquadrado.info.urls')),
    #(r'^$', direct_to_template, {'template': "index.html"}),
    (r'^$', redirect_to, {'url': "/home"}),

    #(r'^detalhes$', direct_to_template, {'template': "detalhes.html"}),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)


from django.conf import settings

if settings.DEBUG:
    import os
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
        )


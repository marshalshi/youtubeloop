from django.conf.urls import patterns, include, url
from autoloop.views import loopone, search, babe_page, gasol
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'youtube.views.home', name='home'),
    # url(r'^youtube/', include('youtube.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', search, name="search"),
    url(r'^babe/$', babe_page, name="babe"),
    url(r'^watch/$', loopone, name="loopauto_one"),
    url(r'gasol/', gasol, name='gasol'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),
                            )

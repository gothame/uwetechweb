from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns(('uwe.views'),
    # Examples:
    # url(r'^$', 'uwetech.views.home', name='home'),
    url(r'^$', 'index'),
    url(r'^about/$', 'about'),
    url(r'^products/$', 'products'),
    url(r'^services/$', 'services'),
    url(r'^support/$', 'support'),
    url(r'^project/$', 'project'),
    url(r'^jiejue/(?P<page>\w+)$','jiejue'),
    url(r'^jiejue/$','jiejue2'),
    url(r'^about/(?P<page>\w+)$','about'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

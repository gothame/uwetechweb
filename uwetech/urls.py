from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls.static import static
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uwetech.views.home', name='home'),
    url(r'^$', include('uwe.urls')),
    url(r'^page/',include('uwe.urls'))

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
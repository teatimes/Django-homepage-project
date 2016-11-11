import django
from django.conf import settings
from django.conf.urls.static import static
django.setup()

from os.path import dirname, abspath, join

from django.conf.urls import url, include
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

	url(r'^', include('src.apps.homepage.urls')),
	url(r'^blog/', include('src.apps.blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
]# + static(settings.STATIC_URL, settings.STATIC_ROOT) #

#if settings.DEBUG is True:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

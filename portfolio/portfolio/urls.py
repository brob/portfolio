from django.conf.urls import patterns, include, url
from projects.models import Skill, Project
from projects.views import *


from django.conf import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', home),
	url(r'^projects/$', projectList),
	url(r'^projects/(?P<slug>[-_\w]+)', projectDetail)
)

urlpatterns += patterns('',
    (r'^photologue/', include('photologue.urls')),
)


if settings.DEBUG:
	
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

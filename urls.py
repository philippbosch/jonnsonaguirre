import os.path

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT, 'media')}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jssettings/$', 'django.views.generic.simple.direct_to_template', {'template': 'jssettings.js', 'mimetype': 'application/x-javascript', 'extra_context': {'settings':settings}}, name="jssettings"),
    url(r'/work-(?P<slug>[^/]+)/$', 'jonnsonaguirre.works.views.work_details', name='project_details'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('cms.urls')),
)

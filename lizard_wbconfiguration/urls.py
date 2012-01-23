# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()

API_URL_NAME = 'lizard_annotation_api_root'
NAME_PREFIX = 'lizard_annotation_'

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('lizard_wbconfiguration.api.urls')),
    )
urlpatterns += debugmode_urlpatterns()

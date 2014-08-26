from django.conf.urls import patterns, include, url
from testcase import urls as testcase_urls

from django.contrib import admin
admin.autodiscover()
handler404 = 'TCMS.views.pagenotfound'
handler403 = 'TCMS.views.notauthorized'

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^testcase/', include(testcase_urls)),
    (r'^$', 'TCMS.views.index'),
	(r'^home/', 'TCMS.views.home'),
    (r'^login/$','TCMS.views.login'),
    (r'^auth/$','TCMS.views.auth_view'),
    (r'^logout/$','TCMS.views.logout'),
    (r'^invalid/$','TCMS.views.invalid_login'),

    url(r'^project/', include('project.urls')),
    url(r'^execution/', include('execution.urls')),
)

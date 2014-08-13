from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'TCMS.views.index'),
	(r'^home/', 'TCMS.views.home'),
    (r'^login/$','TCMS.views.login'),
    (r'^auth/$','TCMS.views.auth_view'),
    (r'^logout/$','TCMS.views.logout'),
    (r'^loggedin/$','TCMS.views.loggedin'),
    (r'^invalid/$','TCMS.views.invalid_login'),
)

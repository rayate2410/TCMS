from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
	(r'^home/', 'django_test.views.home'),
    (r'^login/$','django_test.views.login'),
    (r'^auth/$','django_test.views.auth_view'),
    (r'^logout/$','django_test.views.logout'),
    (r'^loggedin/$','django_test.views.loggedin'),
    (r'^invalid/$','django_test.views.invalid_login'),
    (r'^register/$','django_test.views.register_user'),
    (r'^register_success/$','django_test.views.register_success'),
)

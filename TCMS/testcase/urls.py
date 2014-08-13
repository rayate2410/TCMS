from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'testcase.views.home'),
)
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'testcase.views.home'),
    (r'^load_category/$', 'testcase.views.load_category'),
    (r'^load_testcases/$', 'testcase.views.load_testcases'),
    (r'^add/$', 'testcase.views.add_testcase'),
)
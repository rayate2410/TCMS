from django.conf.urls import patterns, include, url
import execution.views as exec_views



urlpatterns = patterns('',
   
    url(r'^$', exec_views.index),
    url(r'^get/(?P<ex_id>\d+)/$', exec_views.get_execution_detail),
    url(r'^start/$', exec_views.start_execution),
    #url(r'^(?P<p_id>\d+)/category/add/$', exec_views.add_category),
    url(r'^execute/(?P<ex_id>\d+)/tc/(?P<eh_id>\d+)/$', exec_views.execute),
    
    url(r'^get/(?P<ex_id>\d+)/filter/$', exec_views.filtered_data),
    url(r'^get/(?P<tp_id>\d+)/allocate/$', exec_views.allocate_task),
    
)
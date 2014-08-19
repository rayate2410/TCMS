from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from testcase.models import TestCase
from project.models import Project
from project.models import Category
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.context_processors import csrf

@login_required
def home(request):
    c = {}
    c.update(csrf(request))
    projects = Project.objects.all()
    c['projects'] = projects
    return render_to_response('testcase_home.html',
                              c, context_instance=RequestContext(request))

def load_category(request):
    if request.method == "POST":
        p_name = request.POST['p_name']
    else:
        p_name = ""
    q = Project.objects.get(name=p_name)
    categories = q.category_set.all()
    return render_to_response('load_category.html',
                              {'categories' : categories })
    
def load_testcases(request):
    if request.method == "POST":
        p_name = request.POST['p_name']
        c_name = request.POST['c_name']

    q = Project.objects.get(name=p_name)
    print q.name
    c = q.category_set.get(name=c_name)
    print c
    testcases = c.testcase_set.all()
    print testcases 
    
    return render_to_response('testcase_list.html',
                              {'testcases' : testcases })
    
def add_testcase(request):
    if request.method == "POST":
        print request
    c = {}
    c.update(csrf(request))
    return render_to_response('add_testcase.html',
                              c, context_instance=RequestContext(request))
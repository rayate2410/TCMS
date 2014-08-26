from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from testcase.models import TestCase
from project.models import Project
from project.models import Category
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.context_processors import csrf
from testcase import parser

tc = TestCase()

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
        pid = request.POST['p_name']
    else:
        pid = ""
    q = Project.objects.get(id=pid)
    categories = q.category_set.all()
    return render_to_response('load_category.html',
                              {'categories' : categories })
    
def load_testcases(request):
    if request.method == "POST":
        pid = request.POST['p_name']
        cid = request.POST['c_name']
    
    testcases = tc.filter(pid, by="category", cid=cid) 
    
    return render_to_response('testcase_list.html',
                              {'testcases' : testcases })
    
def add_testcase(request):
    message = ""
    if request.method == "POST":
        req = request.POST
        project = Project.objects.get(pid=req['project'])
        req['project'] = project 
        req['category'] = project.category_set.get(cid=req['category'])
        req['last_modified_by'] = request.user
        test_case = TestCase(req)
        try:
            test_case.save()
            message = "Testcase has been added successfully"
        except:
            message = "Failed to add testcase"
        
    c = {}
    c.update(csrf(request))
    projects = Project.objects.all()
    c['projects'] = projects
    c['message'] = message
    return render_to_response('add_testcase.html',
                              c, context_instance=RequestContext(request))

def import_testcases(request):
    message = ""
    if request.method == "POST":
        cid = request.POST['category']
        pid = request.POST['project']
        project = Project.objects.get(id=pid)
        category = project.category_set.get(id=cid)
        file_path = request.POST['file']
        xls_parser = parser.ParseXls()
        

        try:
            message = "Testcases have been imported successfully"
        except:
            message = "Failed to import testcases"
        
    c = {}
    c.update(csrf(request))
    projects = Project.objects.all()
    c['projects'] = projects
    c['message'] = message
    return render_to_response('import_testcases.html',
                              c, context_instance=RequestContext(request))

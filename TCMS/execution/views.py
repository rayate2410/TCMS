from __future__ import division
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import TestPlan, ExecutionHistory, ExecutionTask
from project.models import Project, Category, Build, Browser, ClientDevice
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

import time
from testcase.models import TestCase

from django.http.response import HttpResponse
from django.core.context_processors import csrf


# Create your views here.
def index(request):
    testplans = TestPlan.objects.all()
    return render_to_response('executions_home.html', {'testplans' : testplans, 'active':'active'})
    
def start_execution(request):
    args = {}
    args.update(csrf(request))
    
    projects = Project.objects.all()
    args['projects'] = projects
    args['active'] = 'active'
    
    if request.POST:
        
        title = request.POST['title']
        build = Build.objects.get(id=request.POST['build'])
        project = Project.objects.get(id=request.POST['project'])
        description = request.POST['description']
        
        test_plan = TestPlan(project = project, title = title, build = build , description = description, started_by = request.user)
        test_plan.save()
            
        return HttpResponseRedirect("/execution/")
        
    else:
        return render_to_response('start_execution.html', args)


def get_execution_detail(request, ex_id):
    execution = TestPlan.objects.get(id = ex_id)
    execution_history = execution.executionhistory_set.all()
    categories =  execution.executionhistory_set.values('testcase__category__name').distinct()
    
    return render_to_response('execution_detail.html', {'execution': execution,'execution_history': execution_history, 'active':'active', 'categories':categories})

def execute(request, ex_id, eh_id):
    args = {}
    args.update(csrf(request))
    execution = TestPlan.objects.get(id = ex_id)
    execution_history = execution.executionhistory_set.get(id=eh_id)
    args['execution'] = execution
    args['execution_history'] = execution_history
   
    
    if request.POST:
        
        result = request.POST['result']
        bug_id = request.POST['bugid']
        comment = request.POST['comment']
        
        if result == 'PASS':
            execution_history.bugid = 0
            execution_history.comment = ''
            if comment !='':
                execution_history.comment = comment
       
        else:
            if bug_id != '' and comment !='':
                execution_history.bugid = bug_id
                execution_history.comment = comment
        
        execution_history.result = result
        #print request.user
        execution_history.executed_by = request.user
        execution_history.save()
        
        # Calculate execution status.
        total_tc = execution.executionhistory_set.count()
        passed_tc = execution.executionhistory_set.filter(result='PASS').count()
        failed_tc = execution.executionhistory_set.filter(result='FAIL').count()
        nap_tc = execution.executionhistory_set.filter(result='NAp').count()
        
        
        
        execution_status = ( (passed_tc + failed_tc + nap_tc)/total_tc ) * 100
        
        #print execution_status 
        
        execution.status = execution_status
        
        execution.save()
          
        return render_to_response('execution.html', args)

        
    else:
        return render_to_response('execution.html', args)
    


def filtered_data(request, ex_id):
    execution = TestPlan.objects.get(id = ex_id)
    execution_history = None
    filter_by = None
    
    categories =  execution.executionhistory_set.values_list('testcase__category__name', flat=True).distinct()
    
    
    
    if 'by' not in request.GET:
        by = "All"
        execution_history = execution.executionhistory_set.all()
    
    
        
        
    else:
        filter_by = request.GET['by']
    
        if filter_by == 'pass':
            by = "Passed"
            execution_history = execution.executionhistory_set.filter(result='PASS')
        elif filter_by == 'fail':
            by = "Failed"
            execution_history = execution.executionhistory_set.filter(result='FAIL')
        elif filter_by == 'nap':
            by = "Not Applicable"
            execution_history = execution.executionhistory_set.filter(result='NAp')
        elif filter_by == 'ne':
            by = "Not Executed"
            execution_history = execution.executionhistory_set.filter(result='NE')
        elif filter_by == 'executed':
            by = "Executed"
            execution_history = execution.executionhistory_set.filter(result__in=['PASS','FAIL','NAp'])
        else:
            by = "All"
            execution_history = execution.executionhistory_set.all()
    args = {}      
    args['execution'] = execution
    args['execution_history'] = execution_history 
    args['categories'] = categories
    #args['categories'] = execution.executionhistory_set.all().testcase_set.all()
    
    
    
    args['filter_by'] = by
    return render_to_response('execution_filter.html', args)

def allocate_task(request, tp_id):
    args = {}
    args.update(csrf(request))
    testplan = TestPlan.objects.get(id = tp_id)
    args['testplan'] = testplan
    args['users'] = User.objects.all()
    args['browsers'] = Browser.objects.all()
    args['client_devices'] = ClientDevice.objects.all()
    
    
    if request.POST:
        print "POST"
        title = request.POST['title']
        description = request.POST['description']
        allocate_to = User.objects.get(id=request.POST['allocate_to'])
        client_device = ClientDevice.objects.get(id=request.POST['client_device'])
        browser = Browser.objects.get(id=request.POST['browser'])
        category = Category.objects.get(id=request.POST['category'])
        
        execution_task = ExecutionTask(testplan = testplan, title = title, description = description, allocated_to = allocate_to, allocated_by = request.user,client_device = client_device, browser = browser, category=category)
        execution_task.save()
        
        return HttpResponseRedirect("/execution/")
        
    else:
        return render_to_response('allocate_task.html', args)
    


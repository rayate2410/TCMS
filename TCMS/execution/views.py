from __future__ import division
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import Execution,ExecutionHistory
from project.models import Project, Category
from django.http import HttpResponseRedirect

import time
from testcase.models import TestCase

from django.http.response import HttpResponse
from django.core.context_processors import csrf


# Create your views here.
def index(request):
    execution = Execution.objects.all()
    return render_to_response('executions_home.html', {'executions' : execution, 'active':'active'})
    
def start_execution(request):
    args = {}
    args.update(csrf(request))
    
    projects = Project.objects.all()
    args['projects'] = projects
    args['active'] = 'active'
    
    if request.POST:
        #print "post"
        title = request.POST['title']
        version = request.POST['version']
        project = Project.objects.get(id=request.POST['project'])
        categories = request.POST.getlist('categories')
        description = request.POST['description']
        
        execution = Execution(project = project, title = title, version = version , description = description,started_by = request.user)
        execution.save()
        
        for category in categories:
            testcases = TestCase.objects.filter(category=category)
            
            for testcase in testcases:
                execution_history_tc = ExecutionHistory(execution=execution, testcase = testcase)
                execution_history_tc.save()
                
            
        return HttpResponseRedirect("/execution/")
        
    else:
        return render_to_response('start_execution.html', args)


def get_execution_detail(request, ex_id):
    execution = Execution.objects.get(id = ex_id)
    execution_history = execution.executionhistory_set.all()
    return render_to_response('execution_detail.html', {'execution': execution,'execution_history': execution_history, 'active':'active'})

def execute(request, ex_id, eh_id):
    args = {}
    args.update(csrf(request))
    execution = Execution.objects.get(id = ex_id)
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
    

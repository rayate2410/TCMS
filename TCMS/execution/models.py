from django.db import models as django_models
from project import models as project_models
from testcase import models as tc_models
from django.contrib.auth.models import User 
from datetime import datetime

# Execution Models

class TestPlan(django_models.Model):
    project = django_models.ForeignKey(project_models.Project)
    build = django_models.ForeignKey(project_models.Build)
    title = django_models.CharField(max_length=200)
    description =  django_models.TextField()
    start_date = django_models.DateTimeField("Date", auto_now_add=True)
    started_by = django_models.ForeignKey(User)
    
    
class ExecutionTask(django_models.Model):
    testplan = django_models.ForeignKey(TestPlan)
    category = django_models.ForeignKey(project_models.Category)
    description =  django_models.TextField()
    title = django_models.CharField(max_length=200)
    allocated_by = django_models.ForeignKey(User, related_name = 'executiontask_allocated_by')
    allocated_to = django_models.ForeignKey(User,related_name = 'executiontask_allocated_to')
    start_date = django_models.DateTimeField("Date", auto_now_add=True)
    status = django_models.IntegerField(default=0)
    client_device = django_models.ForeignKey(project_models.ClientDevice)
    browsers = django_models.CharField(max_length=200, null=True, blank=True)    
    
    def __unicode__(self):
        return self.title
    
    def passed(self):
        return self.executionhistory_set.filter(result = 'PASS').count()
    
    def failed(self):
        return self.executionhistory_set.filter(result = 'FAIL').count()
    
    def nap(self):
        return self.executionhistory_set.filter(result = 'NAp').count()
    

'''
class Execution(django_models.Model):
    project = django_models.ForeignKey(project_models.Project)
    
    title = django_models.CharField(max_length=200)
    started_by = django_models.ForeignKey(User)
    version = django_models.CharField(max_length=200)
    description =  django_models.TextField()
    start_date = django_models.DateField("Date", auto_now_add=True)
    status = django_models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
    
    def passed(self):
        return self.executionhistory_set.filter(result = 'PASS').count()
    
    def failed(self):
        return self.executionhistory_set.filter(result = 'FAIL').count()
    
    def nap(self):
        return self.executionhistory_set.filter(result = 'NAp').count()
'''
    
    
class ExecutionHistory(django_models.Model):
    execution = django_models.ForeignKey(ExecutionTask)
    testcase = django_models.ForeignKey(tc_models.TestCase)
    result = django_models.CharField(max_length=10,default='NE')
    bugid = django_models.IntegerField(default=0)
    comment = django_models.TextField(default='')
    executed_by = django_models.ForeignKey(User ,null=True, default = None)
    modified_date = django_models.DateField("Date", auto_now_add=True)
    
    def next(self):
        try:
            return ExecutionHistory.objects.get(pk=self.pk+1)
        except:
            return None

    def previous(self):
        try:
            return ExecutionHistory.objects.get(pk=self.pk-1)
        except:
            return None

    
    
    
    
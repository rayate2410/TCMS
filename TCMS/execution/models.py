from django.db import models as django_models
from project import models as project_models
from testcase import models as tc_models
from django.contrib.auth.models import User 
from datetime import datetime

# Execution Models

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
    
    
class ExecutionHistory(django_models.Model):
    execution = django_models.ForeignKey(Execution)
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

    
    
    
    
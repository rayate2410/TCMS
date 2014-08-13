from django.db import models as django_models
from project import models as project_models
from testcase import models as tc_models
from django.contrib.auth.models import User 

# Execution Models

class Execution(django_models.Model):
    category = django_models.ForeignKey(project_models.Category)
    title = django_models.CharField(max_length=200)
    started_by = django_models.ForeignKey(User)
    version = django_models.CharField(max_length=200)
    description =  django_models.TextField()
    start_date = django_models.DateField('Date Created')
    status = django_models.IntegerField()
    
    def __unicode__(self):
        return self.title
    
    
class ExecutionHistory(django_models.Model):
    execution = django_models.ForeignKey(Execution)
    testcase = django_models.ForeignKey(tc_models.TestCase)
    result = django_models.CharField(max_length=10)
    bugid = django_models.IntegerField()
    comment = django_models.TextField()
    modified_date = django_models.DateField('Date Modified')
    
    
    
    
    
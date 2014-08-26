# Testcase Models.
from django.db import models as django_models
from project import models as project_models
from django.contrib.auth.models import User 
# Testcase Models.

class TestCase(django_models.Model):
    project = django_models.ForeignKey(project_models.Project)
    category = django_models.ForeignKey(project_models.Category)
    title = django_models.CharField(max_length=200)
    steps = django_models.TextField()
    expected_result = django_models.TextField()
    creation_date = django_models.DateTimeField('Date Created',auto_now_add=True)
    created_by = django_models.ForeignKey(User)
    is_automated = django_models.BooleanField()
    status = django_models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.title

    

class TestcaseHistory(django_models.Model):
    testcase = django_models.ForeignKey(TestCase)
    project = django_models.ForeignKey(project_models.Project)
    title = django_models.CharField(max_length=200)
    steps = django_models.TextField()
    expected_result = django_models.TextField()
    is_automated = django_models.BooleanField()
    modified_date = django_models.DateTimeField('Date Modified',auto_now_add=True)
    modified_by = django_models.ForeignKey(User)
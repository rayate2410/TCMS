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
    creation_date = django_models.DateField('Date Created')
    modified_date = django_models.DateField('Date Modified')
    last_modified_by = django_models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title

    


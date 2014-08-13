from django.db import models

# Project Models.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()
    
    def __unicode__(self):
        return self.name
    

class Category(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    description =  models.TextField()
    
    def __unicode__(self):
        return self.name


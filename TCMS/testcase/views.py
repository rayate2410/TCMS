from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from testcase.models import TestCase
from project.models import Project
from project.models import Category

def home(request):
    projects = Project.objects.all()
    return render_to_response('testcase_home.html',{'projects' : projects })

def load_category(request, p_name):
    project = Project.objects.get(title=p_name)
    categories = project.category_set.all()
    return render_to_response('testcase_categories.html',{'categories' : categories })
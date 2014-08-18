from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import Project,Category
from forms import ProjectForm
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.http.response import HttpResponse
from django.core.context_processors import csrf

# Project views are here.

@login_required(login_url='/login')
def index(request):
    projects = Project.objects.all()
    return render_to_response('project_home.html', {'projects' : projects, 'active':"active"})
   
@login_required(login_url='/login')
def get_project_detail(request,p_id=1):
    project = Project.objects.get(id=p_id)
    categories = project.category_set.all()
   
    return render_to_response('project_detail.html', {'project': project, 'categories': categories, 'active':'active'})

@login_required(login_url='/login')
def add_project(request):
    args = {}
    args.update(csrf(request))
    args['active'] = 'active'
    
    if request.POST:
        proj_name = request.POST['proj_name']
        proj_desc = request.POST['proj_desc']
        
        if Project.objects.filter(name = proj_name):
            args['message'] = 'Same project already exists.'
            return render_to_response('add_project.html', args)
        else:
            project = Project(name = proj_name, description = proj_desc)
            project.save()
            print project.id   
            return HttpResponseRedirect('/project/get/'+str(project.id)+'/')
        
    else:
        
        return render_to_response('add_project.html', args)

@login_required(login_url='/login')
def add_category(request, p_id):
    args = {}
    args.update(csrf(request))
    project = Project.objects.get(id=p_id)
    args['project'] = project
    args['active'] = 'active'
    
    if request.POST:
        category_name = request.POST['category']
        category_desc = request.POST['description']
        
        if project.category_set.filter(name=category_name):
            args['message'] = 'Same category already exists in this project'
            return render_to_response('add_category.html', args)
        else:
            category = Category(project = project, name = category_name, description = category_desc)
            category.save()   
            return HttpResponseRedirect('/project/get/'+str(p_id)+"/")
        
    else:
        
        return render_to_response('add_category.html', args)

def get_project_category(request):
    project_id = request.GET['proj_id']
    data = []
    if Project.objects.get(id=project_id):
        project = Project.objects.get(id=project_id)
        
        for category in project.category_set.all():
            data.append({ "id": category.id, "name": category.name })
                      
    return HttpResponse(simplejson.dumps(data, indent=4), 
                    mimetype="application/json") 
        
        
    

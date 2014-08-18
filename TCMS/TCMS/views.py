from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required


def index(request):
    c = {}
    c.update(csrf(request))
    return HttpResponseRedirect('/login')

@login_required
def home(request):
    c = {}
    c.update(csrf(request))
    c['user']= request.user
    return render_to_response('dashboard.html',c)

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)
    
def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name' : request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')
    
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def pagenotfound(request):
    return render_to_response('page_not_found.html')
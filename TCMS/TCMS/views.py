from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext


def index(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    return HttpResponseRedirect('/login')

@login_required
def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('dashboard.html',c,context_instance=RequestContext(request))

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
        c = {}
        c.update(csrf(request))
        c['message'] = "Invalid credentials"
        return render_to_response('login.html', c)
       
    
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name' : request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')
    
def logout(request):
    auth.logout(request)
    c = {}
    c.update(csrf(request))
    c['message'] = "You have successfully logged out."
    return render_to_response('login.html', c)

def pagenotfound(request):
    return render_to_response('page_not_found.html')

def notauthorized(request):
    return render_to_response('not_authorized.html')
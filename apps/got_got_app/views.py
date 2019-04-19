from django.shortcuts import render, redirect
from .models import GetUser, Events, valid_entry_new
from django.contrib import messages
from datetime import datetime

def index(request):
    if 'logged_in' in request.session:        
        user = GetUser(request.session['uid'])
        events = Events.GetEventsForMember(request.session['uid'])
        notin = Events.GetEventsNoMember(request.session['uid'])
        host = Events.GetHostedForMember(request.session['uid'])
        context = {
            'user' : user,
            'events': events,    
            'notin' : notin       
        }
        return render(request, 'got_got_app/dashboard.html', context)
    else: 
        return redirect('/')

def show(request):
    if 'logged_in' in request.session:
        b = Events.GetEvents()
        context = {'events':b}
        return render(request, 'got_got_app/shows.html', context)
    else:
        return redirect('/')

def add(request):
    if 'logged_in' in request.session:   
        return render(request, 'got_got_app/new.html')
    else:
        return redirect('/')
    
def add_show(request):
    if 'logged_in' in request.session:
        if request.method=="POST":
            data = request.POST
            start = request.POST['start']
            end = request.POST['end']         
            if start > end:
                request.session['x'] = data
                request.session['derp'] = "Please refrain from time travel"
                return redirect('/trip/new')
            x = valid_entry_new(data)
            print(x)
            if x > 0:
                request.session['x'] = data
                request.session['derp'] = "Destination and plan must contain at least 3 characters"
                return redirect('/trip/new')
            
            else:
                if 'derp' in request.session:
                    del request.session['derp']
                u = request.session['uid']
                x = Events.create_event(request.POST, u)
                return redirect('/trip/dashboard')
    else:
        return redirect('/')

def detail(request,id):
    if 'logged_in' in request.session:
        e = Events.show_event(id)
        m = Events.GetMembersForEvent(id)
        u = request.session['uid']
        context = {
            'event':e,
            'guests':m,
            'uid':u
        }
        return render(request,'got_got_app/detail.html',context)
    else:
        return redirect('/')
    
def join(request, id):
    if 'logged_in' in request.session:
        u= request.session['uid']
        Events.join_event(id, u)
        return redirect('/got_got_app/show')
    else:
        return redirect('/')

def edit(request, id):
    if 'logged_in' in request.session:
        u = Events.show_event(id)
        n = GetUser(request.session['uid'])[0].first_name
        s = (u.start)
        s_f = datetime.strftime(s, "%Y-%m-%d")    
        e = u.end
        e_f = datetime.strftime(e, "%Y-%m-%d")
        context = {
            'event':u,
            'user': n,
            'start':s_f,
            'end':e_f
        }
        return render(request,'got_got_app/edit.html', context)
    else:
        return redirect('/')
    
def update(request):
    if 'logged_in' in request.session:
        if request.method=="POST":
            data = request.POST        
            start = request.POST['start']
            end = request.POST['end']         
            if start > end:
                request.session['x'] = data
                request.session['derp'] = "Please refrain from time travel"
                return redirect('/trip/new')
            else:                      
                x = valid_entry_new(data)        
            if x > 0:
                request.session['x'] = data
                request.session['derp'] = "Destination and plan must contain at least 3 characters"
                return redirect('/trip/new')        
            else: 
                if 'derp' in request.session:
                    del request.session['derp']
                u = request.session['uid']
                x = Events.UpdateEvent(request.POST)
                return redirect('/trip/dashboard')
    else:
        return redirect('/')
    

def remove(request, id):
    if 'logged_in' in request.session:
        Events.RemoveEvent(id)
        return redirect('trips/dashboard')
    else:
        return redirect('/')

def join(request, id):
    if 'logged_in' in request.session:
        u = request.session['uid']
        Events.join_event(id, u)
        return redirect('/trip/dashboard')
    else:
        return redirect('/')
    
def pass_it(request, id):
    if 'logged_in' in request.session:
        u = request.session['uid']
        Events.LeaveEvent(id, u)
        return redirect('/trip/dashboard')
    else:
        return redirect('/')
        
        
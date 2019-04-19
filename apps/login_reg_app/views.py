from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):    
    return render(request, 'login_reg_app/index.html')

def validate(request):
    errors = Users.objects.validate(request.POST)        
    if len(errors) > 1:        
        request.session['errors'] = errors
        return redirect('/')  
    else:
        u = Users.create(request,request.POST)
        request.session['email'] = request.POST['email']
        request.session['pw'] = request.POST['pw']
        return redirect('/verify')
        
def validate_login(request):      
    errors = Users.objects.validate_exists(request.POST)
    if len(errors) > 1:            
        request.session['errors'] = errors    
        return redirect('/')
    else:            
        request.session['email'] = request.POST['email']
        request.session['pw'] = request.POST['pw']      
        return redirect('/verify')

def verify(request):  
    request.session['logged_in'] = False
    data = {
        'email' : request.session['email'],
        'pw' : request.session['pw']
    }
    errors = Users.objects.verify(data)  
    if errors == "yep":        
        request.session.flush()
        uid = Users.objects.get(email = data['email']).id 
        request.session['uid']= uid
        request.session['fname'] = Users.objects.get(email = data['email']).first_name
        request.session['logged_in'] = True
        return redirect('/success')        
    else:
        return redirect('/')
        
def success(request):
    if request.session['logged_in']:
        id = request.session['uid']
        context = {
            'name' : Users.objects.get(id = id).first_name
        }
        
        return redirect('/trip')
    else:
        return redirect('/')

def peace_out(request):
    request.session.flush()
    return redirect('/')

@csrf_exempt
def check_me_out(request):
    e = Users.objects.get(email = request.POST['email']).first_name
    if e:
        e ={'e': e}        
        return JsonResponse(e)
    
    
    
   
    
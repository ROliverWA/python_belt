from django.db import models
from apps.login_reg_app.models import Users
from datetime import datetime






class Events(models.Model):
    dest= models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    plan = models.CharField(max_length=255)
    host = models.ForeignKey(Users, related_name="event")
    guests = models.ManyToManyField(Users, related_name ="guest")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def create_event(data, u):        
        u = GetUser(u)
        print('uuuuuuu')
        print(u[0])
        e = Events.objects.create(dest=data['dest'], start=data['start'], 
        end=data['end'], host=u[0], plan=data['plan'])
        e.guests.add(u[0])
        print(e)
        return e
    
    def show_event(data):
        s = Events.objects.get(id=data)
        return s
        
    def join_event(event, user):
        e = Events.objects.get(id=event) 
        u = GetUser(user)
        e.guests.add(u[0])
        
    def cancel_event(data):
        e = Events.objects.get(id=data)
        Events.objects.delete(e)
        ON_DELETE= CASCADE
        
    def GetEventsForMember(id):
        x = Events.objects.filter(guests = id).order_by('-id')
        return x    
   
    def GetMembersForEvent(id):
        x = Users.objects.filter(guest = id)
        return x  
    
    def GetEvents():
        x = Events.objects.all()
        return x
    
    def GetEventCountForMember(id):
        x = Events.objects.filter(guests = id)
        x = len(x)
        return x
    
    def GetHostedForMember(id):
        x = Events.objects.filter(host=id)
        x = len(x)
        return x
    
    def UpdateEvent(data):        
        x = Events.objects.get(id=data['id'])
        x.dest = data['dest']
        x.start = data['start']
        x.end = data['end']
        x.plan = data['plan']
        x.save()
        
    def RemoveEvent(data):
        Events.objects.get(id = data).delete()
        
    def GetEventsNoMember(id):
        x = Events.objects.exclude(guests = id)
        return  x
    
    def LeaveEvent(id, user):
        e = Events.objects.get(id = id)
        u = Users.objects.get(id = user)
        e.guests.remove(u)
        
        
        
        
    
def valid_entry_new(data):
    errors = 0    
   
    if len(data['plan']) < 3:
        errors = 1
    if len(data['dest']) < 3:
        errors = 1    
    return errors
   
        
        
        
    
    
def GetUser(u):
    a = Users.objects.filter(id = u)      
    return a


    
        
        
        
        
    


































    

    

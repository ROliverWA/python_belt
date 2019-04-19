from django.db import models
import re
import bcrypt

email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{3}$') 
pw_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$-_!%*?&]{8,}$")
name_pattern= re.compile(r"^([A-Za-z]+$)")



class loginManager(models.Manager):
    def validate(self, data):
        errors = {}
        errors['register'] = "Errors Occured"
        if not len(data['fname']) > 2:
            errors['fname'] = "First name must be at least 2 chr long."
        elif not name_pattern.match(data['fname']):
            errors['fname_let'] = "First name can only contain letters."
        if not len(data['lname']) > 2:
            errors['lname'] = "Last name must be at least 2 chr long."
        elif not name_pattern.match(data['lname']):
                errors['lname_lets'] = "Last name can only contain letters"
        if not email_pattern.match(data['email']):
            errors['email_format'] = "Must provide a vaild email"
        elif Users.objects.filter(email = data['email']).exists():
            errors['email_exists'] = "User already exists, try logging in."
        if not data['pw'] == data['conf']:
            errors['pw_match'] = "Passwords must match."            
        elif not pw_pattern.match(data['pw']):
            errors['pw_format'] = "Password must contain 1 UPPERCASE, 1 lowercase, 1 numb3r, and 1 $pecial char.  It must also be at least 8 chars long."    
        return errors
    
    def validate_exists(self, data):
        
        errors = {}
        errors['login'] = 'Errors Occured'
        err = 0
        if not email_pattern.match(data['email']):
            err = 1            
        elif not Users.objects.filter(email = data['email']).exists():
            err = 1              
        if not pw_pattern.match(data['pw']):
            err = 1
        if (err == 1):
            errors['login_msg'] = "We are unable to log you in at this time."
        return errors
    
    def verify(self, data):
        valid= "nope"        
        u = Users.objects.get(email = data['email'])       
        if bcrypt.checkpw(data['pw'].encode(), u.pw_hash.encode()):
            valid = "yep"
            return valid
        else:
            valid = "nope"
            errors = {}
            errors['login'] = 'Errors Occured'
            errors['login_msg'] = 'We are unable to log you in at this time.'
            return valid
    

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = loginManager()
    
    def create(self, data):        
            i_love_hash = bcrypt.hashpw(data['pw'].encode(), bcrypt.gensalt())
            u = Users.objects.create(first_name=data['fname'], last_name=data['lname'], email=data['email'], pw_hash=i_love_hash.decode())            
            return data

   


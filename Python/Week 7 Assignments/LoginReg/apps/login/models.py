# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
# Create your models here.
class LoginManager(models.Manager):
    def validate(self, postdata):
        regexEmail = re.search(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$', postdata['email'])
        errors = []
        print postdata
        if len(postdata['first_name']) < 2:
            errors.append("First Name must be atleast 2 characters")
        if not postdata['first_name'].isalpha():
            errors.append("First name must contain only letters")
        if len(postdata['last_name']) < 2:
            errors.append("Last Name must be atleast 2 characters")
        if not postdata['last_name'].isalpha():
            errors.append("Last name must contain only letters")
        if not regexEmail:
            errors.append("Email is not valid")
        duplicateEmail = len(self.filter(email=postdata['email']))
        if duplicateEmail > 0:
            errors.append("Email already registered")
        if len(postdata['password']) < 5:
            errors.append("Password needs to be atleast 5 characters")
        if postdata['password'] != postdata['confirm_password']:
            errors.append("Passwords do not match!")
        
        return errors

    def create_user(self, clean_data):
        hashed = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            email=clean_data['email'],
            password = hashed
    )

    def check_user(self, PostData):
        results = {"status": False, 'errors': [], 'user' : None }
        ThisUser = self.filter(email = PostData['email'] ).first()
        if (None == ThisUser):
            results['errors'].append('There is no user found with email {}'.format(PostData['email']) )
        else:
            incomingpw = PostData['password']
            dbpw = ThisUser.password
            if bcrypt.checkpw(incomingpw.encode(), dbpw.encode()):
                results['status'] = True
                results['user'] = ThisUser
            else:
                results['errors'].append("Password is not correct!")
                results['status'] = False
        return results;
      


class Login(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

    
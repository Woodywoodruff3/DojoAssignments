# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class LoginManager(models.Manager):
    def validate(self, postdata):
        regexEmail = re.search(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$', postdata['e_mail'])
        errors = []
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
        duplicateEmail = len(self.filter(e_mail=postdata['e_mail']))
        if duplicateEmail > 0:
            errors.append("Email already registered")
        if len(postdata['password']) < 5:
            errors.append("Password needs to be atleast 5 characters")
        if postdata['password'] != postdata['confirm_password']:
            errors.append("Passwords do not match!")
        
        return errors

    def create_user(self, clean_data):
        return self.create()

class Login(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    e_mail = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()
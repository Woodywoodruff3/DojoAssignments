# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors = []
        #fields cannot be blank
        if len(post_data['first_name']) < 1:
            errors.append("First Name cannot be blank")

        if len(post_data['last_name']) < 1:
            errors.append("Last Name cannot be blank")
        #email verification
        if len(post_data['email']) < 1:
            errors.append("Email cannot be blank")
        
        return errors

    def create_user(self, clean_data):
            return self.create(
                first_name=clean_data['first_name'],
                last_name=clean_data['last_name'],
                email=clean_data['email']
            )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "Name: {} {} Email: {}".format(self.first_name, self.last_name, self.email)


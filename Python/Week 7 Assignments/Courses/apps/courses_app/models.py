# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(request, postdata):
        errors = []
        if len(postdata['name']) < 5:
            errors.append("Course name must be at least 5 characters long")
        if len(postdata['desc']) < 15:
            errors.append("Description must be 15 characters long")
        return errors

        

class Course(models.Model):
    course = models.CharField(max_length = 255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.name

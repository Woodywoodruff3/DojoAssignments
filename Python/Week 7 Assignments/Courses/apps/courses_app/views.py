# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'course' : courses
    }
    return render(request, 'courses_app/index.html', context)

def add_course(request):
    errs = Course.objects.validate(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        if request.method == 'POST':
            Course.objects.create(course=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')

def destroy(request, user_id):

    context = {
        'course_data' : Course.objects.get(id=user_id)
    }
    return render(request, 'courses_app/destroy.html', context)

def remove(request, user_id):
    course = Course.objects.get(id=user_id)
    course.delete()
    return redirect('/')
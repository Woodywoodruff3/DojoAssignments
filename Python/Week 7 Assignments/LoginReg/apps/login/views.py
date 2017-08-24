# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def success(request):
    return render(request, 'login/success.html')

def register(request):
    
    errs = Login.objects.validate(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
            
        return redirect('/')
    else:
        #register user
        new_user = Login.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        request.session['first_name'] = new_user.first_name      
    return redirect('/success')

def login(request):
    user = results = Login.objects.check_user(request.POST)
    if results['status'] == False:
        for e in results['errors']:
            messages.error(request, e)
        return redirect("/")
    request.session['first_name'] = results['user'].first_name
    return redirect('/success')
    
def logoff(request):
    request.session['first_name'] = ""
    print request.session['first_name']
    return redirect('/')
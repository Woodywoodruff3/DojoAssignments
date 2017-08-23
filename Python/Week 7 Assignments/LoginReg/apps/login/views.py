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
    print request.POST
    errs = Login.objects.validate(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    
        
            
    return redirect('/')
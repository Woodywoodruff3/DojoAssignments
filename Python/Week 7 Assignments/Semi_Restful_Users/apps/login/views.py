# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'login/index.html', context)

def add_user(request):
    print request.POST
    errs = User.objects.validate_registration(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        # add User
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, "Thank you for registering {} {}".format(new_user.first_name, new_user.last_name))
    return redirect('/users')

def update_user(request, user_id):
    update_user = User.objects.get(id=user_id)
    update_user.first_name = request.POST['first_name']
    update_user.last_name = request.POST['last_name'] 
    update_user.email = request.POST['email'] 
    update_user.save() 
    return redirect('/users')

def new_user(request):
    return render(request, 'login/add_user.html')

def show(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, 'login/show.html', context)

def edit(request, user_id):
    context = {
        'user' : User.objects.get(id = user_id)
    }
    return render(request, 'login/edit.html', context)

def destroy(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/users')
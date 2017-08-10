# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
# Create your views here.
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def users(request):
    response = "Placeholder to later display all the list of users"
    return HttpResponse(response)


# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
# Create your views here.
def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

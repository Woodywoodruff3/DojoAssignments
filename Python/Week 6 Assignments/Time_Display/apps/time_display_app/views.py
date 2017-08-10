# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    # get_time = strftime("%H:%M:%S", gmtime())
    # get_date = strftime("%m %d, %Y", gmtime())
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%I:%M %p")
    }
    return render(request, 'time_display_app/index.html', context)

# Create your views here.

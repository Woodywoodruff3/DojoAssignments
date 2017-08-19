# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
from time import strftime

def index(request):
    if not 'total_gold' in request.session:
        request.session['total_gold'] = 0
    if not 'activity' in request.session:
        request.session['activity'] = []

    print request.session['activity']
    return render(request, 'ninjagold/index.html')

def clear(request):
    request.session['total_gold'] = 0
    request.session['activity'] = []
    return redirect('/')

def process_gold(request):
    selection = request.POST['location']
    date = strftime("%Y/%m/%d %I:%M %p")
    if selection == 'farm':
        gold =  random.randint(10, 20)
        
    elif selection == 'cave':
        gold = random.randint(5,10)
    
    elif selection == 'house':
        gold = random.randint(2,5)

    elif selection == 'casino':
        gold = random.randint(-50, 50)

    context = {
        'location' : selection,
        'amount': gold,
        'time': date
    }    
    
    activities = request.session['activity']
    activities.insert(0, context)
    request.session['activity'] = activities
    request.session['total_gold'] += gold


    return redirect('/')


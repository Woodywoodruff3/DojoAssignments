# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from ..review.models import *
# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    errs = Login.objects.validate(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
            
        return redirect('/')
    else:
        #register userac
        new_user = Login.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        request.session['name'] = new_user.name
        request.session['emai'] = new_user.email 
    return redirect('/books')

def login(request):
    user = results = Login.objects.check_user(request.POST)
    if results['status'] == False:
        for e in results['errors']:
            messages.error(request, e)
        return redirect("/")
    print results
    request.session['name'] = results['user'].name
    request.session['email'] = results['user'].email
    request.session['id'] = results['user'].id
    print request.session['id']
    return redirect('/books')

def logout(request):
    request.session['name'] = ""
    request.session['email'] = ""
    return redirect('/')

def show(request, user_id): 
     user = User.objects.get(id=user_id) 
     book_ids = user.reviews_left.all().values("book").distinct() 
     user_books = [] 
     for book in book_ids: 
         user_books.append(Book.objects.get(id=book['book'])) 
     context = { 
         'user': user, 
         'unique_book_reviews': user_books 
     } 
     return render(request, 'login/show.html', context) 


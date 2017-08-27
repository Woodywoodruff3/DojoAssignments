# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.db.models import Count
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def books(request):
        context = {
                'recent': Review.objects.recent_and_not()[0],
                'more': Review.objects.recent_and_not()[1]
        }
        return render(request, 'review/books.html', context)

def add(request):
        context = {
                'author': Author.objects.all()
        }
        return render(request, 'review/add.html', context)

def show(request, book_id):
        book = Book.objects.get(id=book_id)
        reviews = book.books.all()
        context={
                'book': book,
                'reviews': reviews
        }
        
        return render(request, 'review/show.html', context)

def create(request):
        print request.session['email']
        errs = Review.objects.review_validate(request.POST)
        if errs:
                for e in errs:
                        messages.error(request, e)
        else:
                Review.objects.create_review(request.POST, request.session['email'])

        
        return redirect('/books')

def create_extra(request, book_id):
        print book_id, type(book_id)
        the_book = Book.objects.get(id=book_id)
        new_book_data = {
                'title': the_book.title,
                'author': the_book.author.id,
                'rating': request.POST['rating'],
                'review': request.POST['review'],
                'new_author': ''
        }
        errs = Review.objects.review_validate(new_book_data)
        if errs:
                for e in errs:
                        messages.error(request, e)
        else:
                Review.objects.create_review(new_book_data, request.session['email'])
        return redirect('books/{}'.format(book_id))

def remove(request, login_id):
        
        Review.objects.filter(id=login_id).delete()
        return redirect('books/book_id')

def user(request, user_id):
        
       
        new_user = Login.objects.get(id=user_id)
        reviews = new_user.review_left.all()
        total = len(reviews)
        context={
                'user': new_user,
                'reviews': reviews,
                'total' : total
        }
        return render(request, 'review/home.html', context)
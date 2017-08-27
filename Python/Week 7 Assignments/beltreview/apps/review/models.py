# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import *
from django.db import models

# Create your models here.
## AUTHOR ##
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="authors")

    def __str__(self):
        return self.title

class ReviewManager(models.Manager):
    def review_validate(self, post_data):
        errors = []
        #title and review cannot be blank
        if len(post_data['title']) < 1 or len(post_data['review']) < 1:
            errors.append("Fields cannot be left blank")
            #New Author needs to have 3 or more char
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append("New author must have 3 or more characters")
            #New Author needs to have 3 or more char
        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append('New author must have 3 or more characters')
            #Make sure rating is submitted.
        if not int(post_data['rating']):
            errors.append("Please add a rating")
    
        return errors

    def create_review(self, clean_data, email):
        #Get or Create Author
        
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])
        #Get or Create Book
        the_book = None
        if not Book.objects.filter(title=clean_data['title']):
            the_book = Book.objects.create(
                title=clean_data['title'],
                author=the_author
            )
        else:
            the_book = Book.objects.get(title=clean_data['title'])
        
        self.create(
            review = clean_data['review'],
            rating = clean_data['rating'],
            book = the_book,
            reviewer = Login.objects.get(email = email)
        )
    
    def recent_and_not(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
        containing the rest
        '''
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])
    

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="books")
    reviewer = models.ForeignKey(Login, related_name="review_left")
    created_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    def __str__(self):
        return "Book: (self.book.title)" 
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# the index function is called when root is visited
def index(request):
    
    return render(request, 'session_words/index.html')

def process(request):
    
    try:
        font_color = request.POST['color']
    except:
        font_color = 'black'
    try:
        font_size = request.POST['big_fonts']
    except: 
        font_size = 'off'
    new_word ={
        'word': request.POST['added_word'],
        'color': font_color,
        'size': font_size,
        "time": strftime("%I:%M %p"),
        "date": strftime("%b %d, %Y")
    }
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    word_list = request.session['words']
    word_list.append(new_word)
    request.session['words'] = word_list
    
    return redirect('/')

def clear(request):
    del request.session['words']
    return redirect('/')
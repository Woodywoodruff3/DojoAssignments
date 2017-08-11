from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited

def index(request):
    
    context = {
        "random": get_random_string(length=14)
    }
    total = request.session.get('total')
    if not total:
        request.session['total'] = 1
    else:
        request.session['total'] += 1
    return render(request, 'random_word_app/index.html', context)

def clear(request):
    request.session['total'] = None
    return redirect('/')
   
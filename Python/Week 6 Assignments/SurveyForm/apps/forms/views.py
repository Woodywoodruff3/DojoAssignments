from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):

    return render(request, 'forms/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']

    print request.session['name']
    return redirect('/results')

def results(request):
    total = request.session.get('total')
    if not total:
        request.session['total'] = 1
    else:
        request.session['total'] += 1

    context = {
        'name' : request.session.get('name'),
        'location' : request.session.get('location'),
        'language' : request.session.get('language'),
        'comments' : request.session.get('comments'),

    }
    return render(request, 'forms/results.html', context)

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'all_time' in request.session:
        request.session['all_time'] = 0
    if not 'count' in request.session:
        request.session['count'] = 0

    print request.session['all_time']
    return render(request, 'store/index.html')

def buy(request):
    item = request.POST['product_id']
    quantity = request.POST['quantity']

    if item == '1001':
        request.session['one_time'] = 14.99 * int(quantity)
        request.session['all_time'] += request.session['one_time']
        request.session['count'] += 1
        return redirect('/amadon/checkout')
    elif item == '1002':
        request.session['one_time'] = 24.99 * int(quantity)
        request.session['all_time'] += request.session['one_time']
        request.session['count'] += 1
        return redirect('/amadon/checkout')
    elif item == '1003':
        request.session['one_time'] = 4.99 * int(quantity)
        request.session['all_time'] += request.session['one_time']
        request.session['count'] += 1
        return redirect('/amadon/checkout')
    elif item == '1004':
        request.session['one_time'] = 44.99 * int(quantity)
        request.session['all_time'] += request.session['one_time']
        request.session['count'] += 1
        return redirect('/amadon/checkout')
    else:
        return redirect('/amadon')

def checkout(request):
    return render(request, 'store/checkout.html')

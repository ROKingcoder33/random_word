from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    context = {
        "title" : "Random Word Generator",
        "random_string" : get_random_string(length=14),
        "counter" : request.session['counter'],
    }
    return render(request, 'main/index.html', context)

def generate(request):
    request.session['counter'] += 1
    request.session.modified = True
    return redirect('/')

def reset(request):
    request.session.clear()
    request.session.modified = True
    return redirect('/')

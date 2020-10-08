from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.

def index (request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['history']=''
    return render(request, 'index.html')

def count(request):
    min = int(request.POST['gold_min'])
    max = int(request.POST['gold_max'])
    place = request.POST['location']
    rand = random.randint(min,max)
    request.session['winloss'] = rand
    request.session['gold']+=rand
    if rand > -1:
        str = (f"Earned {rand} gold from the {place}!\n")
        request.session['history']  +=str
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['history'] =' '
    return redirect('/')
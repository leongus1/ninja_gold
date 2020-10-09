from django.shortcuts import render, HttpResponse, redirect
import random
from time import strftime, localtime

# Create your views here.
def index (request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        hist=[]
        request.session['history'] = hist
    return render(request, 'index.html')

def count(request, location):
    min = int(request.POST['gold_min'])
    max = int(request.POST['gold_max'])
    place = location
    rand = random.randint(min,max)
    request.session['winloss'] = rand
    request.session['gold']+=rand
    if rand > -1:
        str = (f"Earned {rand} gold from the {place}!      ("+ strftime("%Y/%m/%d  %I:%M", localtime())+")")
    else: 
        str = (f"Entered a Casino and lost {rand} golds... Ouch!      ("+ strftime("%Y/%m/%d  %I:%M", localtime())+")")
    
    hist = request.session['history']
    hist.append(str)
    request.session['history'] = hist
    return redirect('/')

def reset(request):
    del request.session['gold']
    # hist=[]
    del request.session['history']
    return redirect('/')
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def count (request):
    return render(request, 'index.html')
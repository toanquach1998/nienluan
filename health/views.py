from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'health/index.html')

def about(request):
    return render(request, 'about.html')


def element(request):
    return render(request, 'elements.html')

def new(request):
    return render(request, 'news.html')

def service(request):
    return render(request, 'services.html')
    

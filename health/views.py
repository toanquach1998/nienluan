from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationFrom

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
    
def register(request):
    form = RegistrationFrom()
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'register.html',{'form':form})


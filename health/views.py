from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationFrom
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'health/index.html',{
        'nav': 'index',
    })
    

def about(request):
    return render(request, 'about.html', {
        'nav': 'about_us',
    })

def element(request):
    return render(request, 'elements.html',{
        'nav': 'element',
    })

def service(request):
    return render(request, 'services.html',{
        'nav': 'services',
    })
    


    
def register(request):
    form = RegistrationFrom()
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'registration/register.html',{'form':form})



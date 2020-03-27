from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Khoa, Bacsi

def contact(request):
    list_khoa = Khoa.objects.all()
    list_bacsi = Bacsi.objects.all()
    context = {"dskhoa": list_khoa, "dsbacsi": list_bacsi}
    return render(request, "contact/contact.html", context)




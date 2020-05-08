from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Khoa, Bacsi

from django.views.generic import TemplateView
from django.views.generic.list import View
from django.contrib.auth.mixins import LoginRequiredMixin

class contact(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'contact/contact.html'



from django.shortcuts import render
from .models import News

def new(request):
    object_list = News.objects.filter()
    return render(request, 'news.html', {
        'object_list':object_list,
        'nav': 'news'
    })
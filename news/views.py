from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator



def new(request):
    object_list = News.objects.order_by('-date_time')
    paginator = Paginator(object_list, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news.html', {
        'page_obj':page_obj,
        'nav': 'news',
               
    })

def new_list(request):
    object_list = News.objects.order_by('-date_time')
    paginator = Paginator(object_list, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'new_list.html', {
        'page_obj':page_obj,
        'nav': 'new_list',
    })
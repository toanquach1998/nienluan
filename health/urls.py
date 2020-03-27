from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('index/', views.index, name ='index'),
   path('about/', views.about, name='about_us'),
 
   path('elements/', views.element, name = 'elements'),
   path('news/', views.new, name = 'news'),
   path('services/', views.service, name = 'services'),

]

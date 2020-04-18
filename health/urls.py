from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index),
   path('index/', views.index, name ='index'),
   path('about/', views.about, name='about_us'),
 
   path('elements/', views.element, name = 'elements'),
   path('news/', views.new, name = 'news'),
   path('services/', views.service, name = 'services'),

   path('register/', views.register,name='register'),
   path('index/register/', views.register,name='register'),
   
   path( 'login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path( 'index/login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
   path('index/logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]

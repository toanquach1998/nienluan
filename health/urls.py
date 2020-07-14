from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_forms
urlpatterns = [
   path('', views.index),
   path('index/', views.index, name ='index'),
   path('about/', views.about, name='about_us'),
 
   path('elements/', views.element, name = 'elements'),
   path('services/', views.service, name = 'services'),

   path('dangky/', views.register,name='register'),
   path('base/register/', views.register,name='register'),
   
   path( 'login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path( 'base/login/',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
   path('index/logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('contact/logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('services/logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('about/logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('news/logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
       
   
]

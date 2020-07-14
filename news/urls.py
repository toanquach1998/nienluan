from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('news/', views.new, name = 'news'),
   path('new_list/', views.new_list, name = 'new_list'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


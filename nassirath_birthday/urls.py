from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'nassi'
urlpatterns = [
  
        
    path('index/', views.Index, name='index'),
  
    #path('details/', views.Details, name='details'),
    #path('', views.Account, name='account'),
  

 
]
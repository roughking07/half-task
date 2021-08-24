from django.urls import path, include
from app import views

urlpatterns = [
   path('', views.index, name='index'),    
   path('products/', views.products, name='products'),    
   path('blogs/', views.blogs, name='blogs'),    
]
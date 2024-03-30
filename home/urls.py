from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('pizza',views.pizza, name='pizza'),
    path('burger',views.pizza, name='burger'),
    path('drinks', views.drinks, name='drinks')
]
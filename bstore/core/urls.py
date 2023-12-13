from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('floor/', views.floor, name='floor'),
    path('design/', views.design , name='design'),
    path('interior/', views.interior, name='interior'),
    path('pop/', views.pop, name='pop'),
    path('real/', views.real, name='real'),
    path('contact/', views.contact, name='contact'),
]

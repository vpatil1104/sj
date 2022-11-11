from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from core import views
urlpatterns = [
     path('',views.index, name='home'),
     
      path('contact',views.contact,name='contact'),
]     
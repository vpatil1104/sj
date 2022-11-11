from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from core import views
urlpatterns = [
     path('',views.index, name='home'),
      path('contact',views.contact,name='contact'),
       path('home',views.Home,name='Home'),
        path('wallect',views.wallect,name='wallect'),
         path('send_money',views.send_money,name='send_money'),
          path('request_money',views.request_money,name='request_money'),
           path('request_recived',views.request_recived,name='request_recived'),
             path('logout',views.logout,name='logout'),
       
]     
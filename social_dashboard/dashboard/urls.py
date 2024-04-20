
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.register, name='register' ),
    path('login', views.Login, name='login'),
    path('home', views.Home, name='home'),
]


           

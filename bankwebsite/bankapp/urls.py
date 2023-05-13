from django.urls import path, include

from bankapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('info', views.info, name='info'),
    path('personel', views.personel, name='personel'),
    path('logout',views.logout,name='logout'),


]
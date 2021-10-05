from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('logoutview', views.logoutview, name="logoutview"),
    path('addblog', views.addblog, name="addblog"),
    path('blogdetail/<slug>', views.blogdetail, name="blogdetail"),
    path('seeblog', views.seeblog, name="seeblog"),
    path('blogdelete/<id>', views.blogdelete, name="blogdelete"),
    path('blogupdate/<slug>', views.blogupdate, name="blogupdate"),
    path('register/', views.register, name="register"),
    path('register/login', views.login, name="login"),
]

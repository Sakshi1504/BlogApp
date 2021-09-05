from django.urls import path, include
from .views_api import *

urlpatterns = [
    path('login', LoginViewobj),
    path('register', RegisterViewobj)
]

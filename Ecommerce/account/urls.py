from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('user_profile', views.user_profile),
]
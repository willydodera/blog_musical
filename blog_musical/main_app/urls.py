from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.sobre_nosotros, name="sobre_nosotros"),
]
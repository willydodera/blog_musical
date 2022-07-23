from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    #path('register/', views.home, name="register"),
    #path('edit/', views.home, name="edit"),
]
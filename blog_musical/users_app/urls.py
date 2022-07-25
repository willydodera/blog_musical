from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/<str:username>', views.edit_profile, name="edit_profile"),
]
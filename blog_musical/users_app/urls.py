from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='main_app/home.html'), name='logout'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/<str:id>', views.edit_profile, name="edit_profile"),
    path('create_avatar/<str:username>', views.create_avatar, name="create_avatar"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
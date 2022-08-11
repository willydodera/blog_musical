from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')

    class Meta:
        model = User
        fields = ['username', 'email', "first_name", 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields} #Saca los mensajes de ayuda


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    avatar = forms.ImageField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', "first_name", 'last_name', "avatar", 'password1', 'password2']
        help_texts = {k:"" for k in fields} #Saca los mensajes de ayuda



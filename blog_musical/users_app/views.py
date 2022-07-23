from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request, "users_app/home2.html", {"form":form, "mensaje":f"Bienvenido {usuario}", "login":True})

            else:
                return render(request, "users_app/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})

        else:
            return render(request, "users_app/login.html", {"form":form, "mensaje":"Formulario invalido"})

    form = AuthenticationForm()

    return render(request, "users_app/login.html", {"form":form})
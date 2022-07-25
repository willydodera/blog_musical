from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog_app.models import Post


# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                posts = Post.objects.all()
                return render(request, "blog_app/blog.html", {"form":form, "mensaje":f"Bienvenido {usuario}", "posts":posts})

            else:
                return render(request, "users_app/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})

        else:
            return render(request, "users_app/login.html", {"form":form, "mensaje":"Formulario invalido"})

    form = AuthenticationForm()

    return render(request, "users_app/login.html", {"form":form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            msj = f"Usuario {username} creado con éxito"
            context = {"form": form, "msj":msj}
            return render(request, "users_app/register.html", context)
    else:
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "users_app/register.html", context)


def profile(request):
    current_user = request.user
    user = User.objects.get(username=current_user)
    context = {"user":user}
    return render(request, "users_app/profile.html", context)


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.username = info["username"]
            user.password = info["password1"]
            user.save()
            msj = f"Usuario {username} editado con éxito"
            context = {"msj":msj, "user":user}
            return render(request, "users_app/profile.html", context)
    else:
        form = UserCreationForm(initial=({"username":user.username}))
        context = {"form": form}
        return render(request, "users_app/edit_profile.html", context)

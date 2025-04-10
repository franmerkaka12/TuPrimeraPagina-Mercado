from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import EditUserForm, AvatarForm, UserUpdateForm  # Añadido UserUpdateForm
from .models import Avatar

@login_required(login_url='Main:login')
def index(request):
    return render(request, "Main/index.html")

def about(request):
    return render(request, "Main/about.html")

def perfil(request):
    return render(request, "Main/perfil.html")

@login_required(login_url='Main:login')
def editar_perfil(request):
    if request.method == "POST":
        # Aquí se usa UserUpdateForm en vez de EditUserForm
        form = UserUpdateForm(request.POST, instance=request.user)
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect("Main:perfil")
    else:
        form = UserUpdateForm(instance=request.user)  # Aquí también cambiamos a UserUpdateForm
        avatar = getattr(request.user, "avatar", None)
        avatar_form = AvatarForm(instance=avatar) if avatar else AvatarForm()

    return render(
        request, "Main/editar_perfil.html", {"form": form, "avatar_form": avatar_form}
    )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("Main:index")
    else:
        form = AuthenticationForm()
    return render(request, "Main/login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Main:index")
    else:
        form = UserCreationForm()
    return render(request, "Main/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("Main:login")

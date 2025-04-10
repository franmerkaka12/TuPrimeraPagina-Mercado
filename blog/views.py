from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, InformacionPersonal
from .forms import PostForm, InformacionPersonalForm

# Lista de publicaciones con búsqueda
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        busqueda = self.request.GET.get("busqueda", "")
        return Post.objects.filter(titulo__icontains=busqueda) if busqueda else Post.objects.all()

# Crear una nueva publicación
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Editar publicación existente
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

# Ver detalle de publicación
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# Eliminar publicación
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

# Crear o editar información personal
@login_required
def informacion_personal(request):
    try:
        info = InformacionPersonal.objects.get(usuario=request.user)
    except InformacionPersonal.DoesNotExist:
        info = None

    if request.method == 'POST':
        form = InformacionPersonalForm(request.POST, instance=info)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('blog:post_list')
    else:
        form = InformacionPersonalForm(instance=info)

    return render(request, 'blog/informacion_personal.html', {'form': form})

# ---------- LOGIN / REGISTER / LOGOUT -----------

def login_view(request):
    if request.user.is_authenticated:
        return redirect("Main:index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("Main:index")
    else:
        form = AuthenticationForm()

    return render(request, "main/login.html", {"form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("Main:index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Main:index")
    else:
        form = UserCreationForm()

    return render(request, "main/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("Main:login")

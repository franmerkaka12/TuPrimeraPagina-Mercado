from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("perfil/", views.perfil, name="perfil"),
    path("editar-perfil/", views.editar_perfil, name="editar_perfil"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

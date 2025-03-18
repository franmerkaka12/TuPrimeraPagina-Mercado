from django.urls import path
from . import views

app_name = 'blog'  # Nombre de la app para evitar conflictos

urlpatterns = [
    path('post/list/', views.post_list, name='post_list'),  # <-- IMPORTANTE: la barra después de "list/"
    path('post/create/', views.post_create, name='post_create'),
]
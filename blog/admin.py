from django.contrib import admin

from .models import Post  # Importa el modelo que quieres registrar

# Registra el modelo en el admin de Django


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_de_publicacion')  # Corrección aquí
    ordering = ('fecha_de_publicacion',)
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# --- MODELO POST ---
class Post(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)

    def __str__(self):
        return self.titulo


# --- MODELO CATEGORÍA ---
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


# --- MODELO COMENTARIO ---
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.post.titulo}"

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-fecha_publicacion']


# --- MODELO INFORMACIÓN PERSONAL ---
class InformacionPersonal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="informacion_personal")
    biografia = models.TextField("Biografía", blank=True, null=True)

    def __str__(self):
        return f"Información de {self.usuario.username}"

    class Meta:
        verbose_name = "Información personal"
        verbose_name_plural = "Informaciones personales"

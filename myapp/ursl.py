# Proyecto10/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),   # Ruta para la aplicación Main
    path('blog/', include('blog.urls')),  # Ruta para la aplicación Blog
    path('saludo/', include('myapp.urls')),  # Ruta para la aplicación MyApp
]

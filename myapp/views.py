from django.shortcuts import render

def saludo(request):
    mensaje = "Bienvenido a mi sitio web"
    return render(request, 'myapp/saludo.html', {'mensaje': mensaje})
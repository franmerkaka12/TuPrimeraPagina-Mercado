from django import forms
from .models import Post, InformacionPersonal

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "estado"]
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'estado': 'Estado',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post',
                'autofocus': True
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribí el contenido del post...',
                'rows': 6
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class InformacionPersonalForm(forms.ModelForm):
    class Meta:
        model = InformacionPersonal
        fields = ['biografia']
        labels = {
            'biografia': 'Biografía personal',
        }
        widgets = {
            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribí algo sobre vos...',
                'rows': 6,
                'style': 'resize: vertical;'  
            }),
        }

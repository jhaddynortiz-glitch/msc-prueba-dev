from django import forms
from .models import Task, Comentario
from django.utils import timezone
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'estado', 'prioridad', 'fecha_limite']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el título de la tarea...',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe detalladamente la tarea...',
                'rows': 4,
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select',
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-select',
            }),
            'fecha_limite': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get('fecha_limite')
        if fecha_limite and fecha_limite < timezone.localdate():
            raise ValidationError('La fecha límite no puede ser menor a la fecha actual.')
        return fecha_limite


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe un comentario o actualización...',
                'rows': 3,
            }),
        }

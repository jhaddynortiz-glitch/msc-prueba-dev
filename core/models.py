from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

def validar_fecha_limite(value):
    if value and value < timezone.localdate():
        raise ValidationError('La fecha límite no puede ser menor a la fecha actual.')

class Task(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    titulo = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5, message="El título debe tener mínimo 5 caracteres.")],
        verbose_name="Título"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Pendiente',
        verbose_name="Estado"
    )
    prioridad = models.CharField(
        max_length=15,
        choices=PRIORIDAD_CHOICES,
        default='Media',
        verbose_name="Prioridad"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )
    fecha_limite = models.DateField(
        validators=[validar_fecha_limite],
        verbose_name="Fecha Límite"
    )

    def clean(self):
        super().clean()
        if self.fecha_limite and self.fecha_limite < timezone.localdate():
            raise ValidationError({'fecha_limite': 'La fecha límite no puede ser menor a la fecha actual.'})

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"


class Comentario(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comentarios',
        verbose_name="Tarea"
    )
    comentario = models.TextField(
        verbose_name="Comentario"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return f"Comentario en '{self.task.titulo}' ({self.id})"

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

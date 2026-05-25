from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task, Comentario
from .forms import TaskForm, ComentarioForm

def task_list(request):
    tasks = Task.objects.all()
    
    # Obtener parámetros de filtro
    estado_filter = request.GET.get('estado', '').strip()
    search_query = request.GET.get('q', '').strip()
    
    if estado_filter:
        tasks = tasks.filter(estado=estado_filter)
        
    if search_query:
        tasks = tasks.filter(titulo__icontains=search_query)
        
    # Obtener las opciones de estado para mostrarlas en la interfaz
    estado_choices = Task.ESTADO_CHOICES
    
    context = {
        'tasks': tasks,
        'estado_choices': estado_choices,
        'selected_estado': estado_filter,
        'search_query': search_query,
    }
    return render(request, 'core/task_list.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comentarios = task.comentarios.all().order_by('-fecha_creacion')
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.task = task
            comentario.save()
            messages.success(request, 'Comentario agregado exitosamente.')
            return redirect('task_detail', pk=task.pk)
    else:
        form = ComentarioForm()
        
    context = {
        'task': task,
        'comentarios': comentarios,
        'comment_form': form,
    }
    return render(request, 'core/task_detail.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'Tarea creada exitosamente.')
            return redirect('task_list')
    else:
        form = TaskForm()
        
    context = {
        'form': form,
        'title': 'Crear Tarea',
        'submit_text': 'Crear Tarea',
    }
    return render(request, 'core/task_form.html', context)

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada exitosamente.')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
        
    context = {
        'form': form,
        'task': task,
        'title': 'Editar Tarea',
        'submit_text': 'Guardar Cambios',
    }
    return render(request, 'core/task_form.html', context)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarea eliminada exitosamente.')
        return redirect('task_list')
    
    context = {
        'task': task,
    }
    return render(request, 'core/task_confirm_delete.html', context)

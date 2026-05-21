# msc-prueba-dev
prueba tecnica desarrolladores

# ETAPA 2 – PRUEBA PRÁCTICA

## Duración: 1 hora
## Puntaje: 60 puntos

---

# ENUNCIADO

## Sistema de Gestión de Tareas y Comentarios

La empresa necesita un sistema interno para administrar tareas asignadas a un equipo de trabajo.

El postulante deberá desarrollar una aplicación básica utilizando Django 5 y MySQL.

---

# REQUERIMIENTOS FUNCIONALES

## 1. Gestión de tareas

Crear un módulo llamado:

```bash
core
```

Debe existir un modelo llamado:

```python
Task
```

con los siguientes campos:

| Campo | Tipo |
|---|---|
| titulo | CharField |
| descripcion | TextField |
| estado | ChoiceField |
| prioridad | ChoiceField |
| fecha_creacion | DateTimeField |
| fecha_limite | DateField |

---

## 2. Valores de estado

- Pendiente
- En Proceso
- Finalizado

---

## 3. Valores de prioridad

- Baja
- Media
- Alta

---

# FUNCIONALIDADES OBLIGATORIAS

## Debe permitir:

- Crear tareas
- Listar tareas
- Editar tareas
- Eliminar tareas
- Ver detalle de una tarea

---

# VALIDACIONES

## Validaciones mínimas

- El título es obligatorio
- El título debe tener mínimo 5 caracteres
- La fecha límite no puede ser menor a la fecha actual

---

# LISTADO DE TAREAS

La pantalla principal debe:

- Mostrar todas las tareas
- Mostrar estado y prioridad
- Mostrar fecha límite
- Permitir filtrar por estado
- Permitir buscar tareas por título

---

# REQUERIMIENTO ADICIONAL

## Comentarios

Crear un segundo modelo:

```python
Comentario
```

con:

| Campo | Tipo |
|---|---|
| task | ForeignKey(Task) |
| comentario | TextField |
| fecha_creacion | DateTimeField |

---

## Funcionalidad requerida

Desde el detalle de una tarea debe poder:

- Agregar comentarios
- Listar comentarios asociados a la tarea

---

# REQUERIMIENTOS TÉCNICOS

## Backend

- Django 5
- ORM de Django
- MySQL

---

## Frontend

Puede utilizar:

- Templates Django
- Bootstrap (opcional)

---

# GIT

Durante el desarrollo debe:

- Inicializar repositorio Git
- Realizar commits descriptivos

Ejemplos:

```bash
git commit -m "Creacion modelo Task"
git commit -m "Implementacion CRUD tareas"
```

---

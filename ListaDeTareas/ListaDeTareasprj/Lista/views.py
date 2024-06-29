from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tarea
from django.urls import reverse_lazy


class ListaDeTareas(ListView):
    model = Tarea  
    context_object_name = 'task'

class Descripcion(DetailView):
    model = Tarea
context_object_name = 'task'

class CrearTarea(CreateView):
    model = Tarea
    fields = "__all__"
    success_url = reverse_lazy('task')
    context_object_name = 'create'

class EditarTarea(UpdateView):
    model = Tarea
    fields = "__all__"
    success_url = reverse_lazy('task')

class Borrar(DeleteView):
    model = Tarea
    context_object_name = 'task'
    success_url = reverse_lazy('task')





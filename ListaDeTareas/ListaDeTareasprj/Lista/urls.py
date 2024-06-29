from django.urls import path 
from .views import ListaDeTareas, Descripcion, CrearTarea, EditarTarea, Borrar

urlpatterns = [
    path('', ListaDeTareas.as_view(), name="task"),  
    path('task-create/', CrearTarea.as_view(), name="task-create"),
    path('task/<int:pk>/', Descripcion.as_view(), name = "descripcion"),
    path('task-update/<int:pk>/', EditarTarea.as_view(), name = "task-update"),
    path('task-delete/<int:pk>/', Borrar.as_view(), name="task-delete")

]
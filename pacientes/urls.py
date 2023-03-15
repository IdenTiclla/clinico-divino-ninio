from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('pacientes', views.pacientes),
    path("pacientes/update/<int:id_paciente>", views.actualizar_paciente),
    path("pacientes/delete/<int:id_paciente>", views.eliminar_paciente)
    
]

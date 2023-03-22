from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('reservas', views.reservas),
    
    # path("pacientes/update/<int:id_paciente>", views.actualizar_paciente),
    # path("pacientes/delete/<int:id_paciente>", views.eliminar_paciente)
    
    # reportes
    path('reporte_dinero_dia_especifico', views.reporte_dinero_dia_especifico),
    path('reporte_consultas_doctor_especifico', views.reporte_consultas_doctor_especifico),


]

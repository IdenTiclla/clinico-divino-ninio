from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('especialidades', views.especialidades),
    path("especialidades/update/<int:id_especialidad>", views.actualizar_especialidad),
    path("especialidades/delete/<int:id_especialidad>", views.eliminar_especialidad),
    #
    path('especialidad_doctor', views.especialidad_doctor),
    
    
]
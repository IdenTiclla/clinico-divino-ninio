from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('doctores', views.doctores),
    path("doctores/update/<int:id_doctor>", views.actualizar_doctor),
    path("doctores/delete/<int:id_doctor>", views.eliminar_doctor)
    
]

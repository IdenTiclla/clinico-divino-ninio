from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('consultorios', views.consultorios),
    #
    # path('horarios', views.horarios),

    
    # path("doctores/update/<int:id_doctor>", views.actualizar_doctor),
    # path("doctores/delete/<int:id_doctor>", views.eliminar_doctor)
    
    path('consultorios/agregar/especialidad/<int:consultorio_id>', views.consultorios_agregar_especialidad),
    
    path('consultorios/agregar/doctor/<int:consultorio_id>', views.consultorios_agregar_doctor),

    path('consultorios/agregar/horarios/<int:consultorio_id>', views.consultorios_agregar_horario),


    path('consultorios/agregar/equipos/<int:consultorio_id>', views.consultorios_agregar_equipo),

    

]

from django.db import models

from especialidades.models import Especialidad
from doctores.models import Doctor
# Create your models here.


class Consultorio(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"<{self.nombre} - {self.especialidad.nombre}> - {self.doctor.nombre}"
    
    class Meta:
        db_table = "Consultorio"


class Horario(models.Model):
    inicio = models.TimeField()
    fin = models.TimeField()
    turno = models.CharField(max_length=20)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)


    def __str__(self):
        return f"<{self.consultorio.nombre} {self.inicio}  {self.fin}>"
    
    class Meta:
        db_table = "Horario"


class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)



    def __str__(self):
        return f"<{self.consultorio.nombre} {self.nombre} >"
    
    class Meta:
        db_table = "Equipo"
from django.db import models

from doctores.models import Doctor
# Create your models here.


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)


    def __str__(self) -> str:
        return f"<{self.nombre}>"
    

    class Meta:
        db_table = "Especialidad"



class EspecialidadDoctor(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.especialidad.nombre} - {self.doctor.nombre}"
    
    class Meta:
        db_table = "EspecialidadDoctor"
from django.db import models

from pacientes.models import Paciente
from consultorios.models import Consultorio
# Create your models here.


class Reserva(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, blank=True, null=True)

    inicio = models.TimeField()
    fin = models.TimeField()
    fecha_reserva = models.DateField()

    precio = models.FloatField()

    def __str__(self):
        return f"<{self.paciente} {self.consultorio}>"
    

    class Meta:
        db_table = "Reserva"
from django.db import models

# Create your models here.


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.nombre}-{self.apellido}>"
    

    class Meta:
        db_table = "Paciente"
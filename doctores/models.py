from django.db import models

# Create your models here.

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)


    def __str__(self) -> str:
        return f"<{self.nombre} - {self.apellido}>"

    class Meta:
        db_table = "Doctor"
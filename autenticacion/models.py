from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ci = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=8)
    rol = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return f"<User: {self.username}>"

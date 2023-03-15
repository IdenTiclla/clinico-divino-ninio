from django.contrib import admin

from .models import Consultorio, Horario, Equipo
# Register your models here.

admin.site.register(Consultorio)
admin.site.register(Horario)
admin.site.register(Equipo)

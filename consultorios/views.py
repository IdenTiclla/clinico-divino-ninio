from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages


from .models import Consultorio, Horario, Equipo

from especialidades.models import Especialidad, EspecialidadDoctor
from doctores.models import Doctor
# Create your views here.


def consultorios(request):
    if request.method == "GET":
        consultorios = Consultorio.objects.all()
        return render(request, "consultorios/consultorios.html", {
            'consultorios': consultorios
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        consultorio = Consultorio.objects.filter(nombre=nombre)
        if consultorio:
            messages.add_message(request=request, level=messages.SUCCESS, message="Consulorio ya existe")    
            return redirect('/consultorios')
        else:
            consultorio = Consultorio(nombre=nombre)
            consultorio.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Consultorio agregado correctamente!")
            return redirect('/consultorios')





def consultorios_agregar_especialidad(request, consultorio_id):
    consultorio = Consultorio.objects.get(id=consultorio_id)
    if request.method == "GET":
        especialidades = Especialidad.objects.all()
        return render(request, "consultorios/agregar_especialidad.html", {
            'consultorio': consultorio,
            'especialidades': especialidades
        })
    elif request.method == "POST":
        print(request.POST)
        especialidad_id = request.POST['especialidad_id']
        especialidad = Especialidad.objects.get(id=especialidad_id)
        consultorio.especialidad = especialidad
        consultorio.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Epecialidad Agregada correctamente!")
        return redirect('/consultorios')



def consultorios_agregar_doctor(request, consultorio_id):
    consultorio = Consultorio.objects.get(id=consultorio_id)
    if request.method == "GET":
        especialidad = consultorio.especialidad
        especialidades_doctores = EspecialidadDoctor.objects.filter(especialidad=especialidad)
        doctores = []
        for especialidad_doctor in especialidades_doctores:
            doctores.append(especialidad_doctor.doctor)
        print(doctores)
        # traer todos los doctores con esa especialidad

        
        return render(request, "consultorios/agregar_doctor.html", {
            'consultorio': consultorio,
            'especialidad': especialidad,
            'doctores': doctores
        })
    elif request.method == "POST":
        print(request.POST)
        doctor_id = request.POST['doctor_id']

        doctor = Doctor.objects.get(id=doctor_id)
        consultorio.doctor = doctor
        consultorio.save()

        messages.add_message(request=request, level=messages.SUCCESS, message="Doctor Agregado Correctamente!")
        return redirect('/consultorios')




def consultorios_agregar_horario(request, consultorio_id):
    consultorio = Consultorio.objects.get(id=consultorio_id)
    horarios = consultorio.horario_set.all()
    print("mostrando horarios")
    print(horarios)
    if request.method == "GET":
        return render(request, "consultorios/agregar_horarios.html", {
            'horarios': horarios,
            'consultorio': consultorio
        })
    
    elif request.method == "POST":
        print(request.POST)
        inicio = request.POST['inicio']
        fin = request.POST['fin']
        turno = request.POST['turno']

        horario = Horario.objects.filter(inicio=inicio, fin=fin, turno=turno, consultorio=consultorio)
        if horario:
            messages.add_message(request=request, level=messages.SUCCESS, message="Horario ya existe")    
            return redirect('/consultorios')
        else:
            horario = Horario(inicio=inicio, fin=fin, turno=turno, consultorio=consultorio)
            horario.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Horario agregado correctamente!")
            return redirect('/consultorios')
        


# todo
def consultorios_agregar_equipo(request, consultorio_id):
    consultorio = Consultorio.objects.get(id=consultorio_id)
    equipos = consultorio.equipo_set.all()
    print("mostrando equipos")
    print(equipos)
    if request.method == "GET":
        return render(request, "consultorios/agregar_equipos.html", {
            'equipos': equipos,
            'consultorio': consultorio
        })
    
    elif request.method == "POST":
        print(request.POST)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']

        equipo = Equipo.objects.filter(nombre=nombre, descripcion=descripcion, consultorio=consultorio)
        if equipo:
            messages.add_message(request=request, level=messages.SUCCESS, message="equipo ya existe")    
            return redirect('/consultorios')
        else:
            equipo = Equipo(nombre=nombre, descripcion=descripcion, consultorio=consultorio)
            equipo.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="equipo agregado correctamente!")
            return redirect('/consultorios')
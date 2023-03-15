from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages

from .models import Especialidad, EspecialidadDoctor
from doctores.models import Doctor

# Create your views here.


def especialidades(request):
    if request.method == 'GET':
        especialidades = Especialidad.objects.all()
        return render(request, "especialidades/especialidades.html", {
            'especialidades': especialidades
        })
    elif request.method == 'POST':
        print(request.POST)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']


        especialidad = Especialidad(nombre=nombre, descripcion=descripcion)
        especialidad.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Especialidad registrado exitosamente!")
        return redirect("/especialidades")
    


def actualizar_especialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    if request.method == "GET":
        return render(request, "especialidades/actualizar_especialidad.html", {
            'especialidad': especialidad
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']

        especialidad.nombre = nombre
        especialidad.descripcion = descripcion

        especialidad.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Especialidad Actualizada exitosamente!")
        return redirect('/especialidades')


def eliminar_especialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(id=id_especialidad)
    especialidad.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Especialidad Eliminada exitosamente!")

    return redirect("/especialidades")

def especialidad_doctor(request):
    if request.method == "GET":
        especialidades = Especialidad.objects.all()
        doctores = Doctor.objects.all()
        especialidades_doctores = EspecialidadDoctor.objects.all()
        return render(request, "especialidad_doctor/especialidad_doctor.html", {
                'especialidades': especialidades,
                'doctores': doctores,
                'especialidades_doctores': especialidades_doctores
            })
    
    elif request.method == "POST":
        print(request.POST)
        doctor_id = request.POST['doctor_id']
        especialidad_id = request.POST['especialidad_id']
        print(doctor_id)
        print(especialidad_id)

        doctor = Doctor.objects.get(id=doctor_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)

        especialidad_doctor = EspecialidadDoctor.objects.filter(especialidad=especialidad, doctor=doctor)
        if especialidad_doctor:
            print("existe")
            messages.add_message(request=request, level=messages.SUCCESS, message="Especialidad y Doctor ya estan registrados")
            return redirect('/especialidad_doctor')
        else:
            print("No existe")
            e_d = EspecialidadDoctor(especialidad=especialidad, doctor=doctor)
            e_d.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Especialidad y Doctor Registrados correctamente")
            return redirect('/especialidad_doctor')
from django.shortcuts import render, redirect


from django.contrib import messages
from .models import Paciente
# Create your views here.


def pacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        return render(request, "pacientes/pacientes.html", {
            'pacientes': pacientes
        })
    elif request.method == 'POST':
        print(request.POST)
        nombre = request.POST['nombre']
        apellido = request.POST['apellidoPaterno']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']


        paciente = Paciente(nombre=nombre, apellido=apellido, ci=ci, telefono=telefono, domicilio=domicilio)
        paciente.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Paciente registrado exitosamente!")
        return redirect("/pacientes")
    


def actualizar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    if request.method == "GET":
        return render(request, "pacientes/actualizar_paciente.html", {
            'paciente': paciente
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        apellido = request.POST['apellidoPaterno']
        ci = request.POST['ci']
        telefono = request.POST['telefono']
        domicilio = request.POST['domicilio']

        paciente.nombre = nombre
        paciente.apellido = apellido
        paciente.ci = ci
        paciente.telefono = telefono
        paciente.domicilio = domicilio

        paciente.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Paciente Actualizado exitosamente!")
        return redirect('/pacientes')


def eliminar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    paciente.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Paciente Eliminado exitosamente!")

    return redirect("/pacientes")
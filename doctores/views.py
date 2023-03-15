from django.shortcuts import render, redirect


from django.contrib import messages


from .models import Doctor
# Create your views here.


def doctores(request):
    if request.method == 'GET':
        doctores = Doctor.objects.all()
        return render(request, "doctores/doctores.html", {
            'doctores': doctores
        })
    elif request.method == 'POST':
        print(request.POST)
        nombre = request.POST['nombre']
        apellido = request.POST['apellidoPaterno']
        ci = request.POST['ci']
        telefono = request.POST['telefono']

        doctor = Doctor(nombre=nombre, apellido=apellido, ci=ci, telefono=telefono)
        doctor.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Doctor registrado exitosamente!")
        return redirect("/doctores")
    


def actualizar_doctor(request, id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    if request.method == "GET":
        return render(request, "doctores/actualizar_doctor.html", {
            'doctor': doctor
        })
    
    elif request.method == "POST":

        nombre = request.POST['nombre']
        apellido = request.POST['apellidoPaterno']
        ci = request.POST['ci']
        telefono = request.POST['telefono']

        doctor.nombre = nombre
        doctor.apellido = apellido
        doctor.ci = ci
        doctor.telefono = telefono

        doctor.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Doctor Actualizado exitosamente!")
        return redirect('/doctores')


def eliminar_doctor(request, id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    doctor.delete()

    messages.add_message(request=request, level=messages.SUCCESS, message="Doctor Eliminado exitosamente!")

    return redirect("/doctores")

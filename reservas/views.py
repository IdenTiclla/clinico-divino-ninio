from django.shortcuts import render, redirect
from django.contrib import messages

from consultorios.models import Consultorio, Horario
from pacientes.models import Paciente
from reservas.models import Reserva
from doctores.models import Doctor

# Create your views here.


def reservas(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        aux_consultorios = Consultorio.objects.all()
        consultorios = []
        
        reservas = Reserva.objects.all()
        
        for aux_consultorio in aux_consultorios:
            if aux_consultorio.especialidad and aux_consultorio.doctor and len(aux_consultorio.horario_set.all()) > 0 and len(aux_consultorio.equipo_set.all()) > 0:
                consultorios.append(aux_consultorio)
        return render(request, "reservas/reservas.html", {
            'pacientes': pacientes,
            'consultorios' : consultorios,
            'reservas': reservas
        })
    
    elif request.method == "POST":
        print(request.POST)
        paciente_id = request.POST['paciente_id']
        paciente = Paciente.objects.get(id=paciente_id)

        consultorio_horario = request.POST['consultorio_horario']
        consultorio_id = consultorio_horario.split(' ')[0]
        
        consultorio = Consultorio.objects.get(id=consultorio_id)

        horario_id = consultorio_horario.split(' ')[1]

        horario = Horario.objects.get(id=horario_id)

        fecha_reserva = request.POST['fecha_reserva']

        precio = request.POST['precio']

        print(paciente)
        print(consultorio)
        print(horario)
        print(horario.inicio)
        print(horario.fin)
        inicio = horario.inicio
        fin = horario.fin
        # CAMBIANDO EL FORMATO PARA LA FECHA
        print(f"fecha_reserva: {fecha_reserva}")
        print(f"{precio}")

        arr = fecha_reserva.split('/')
        fecha_reserva = f"{arr[2]}-{arr[0]}-{arr[1]}"

        # haciendo la reserva
        reserva = Reserva.objects.filter(consultorio=consultorio, inicio=inicio, fin=fin, fecha_reserva=fecha_reserva)
        if reserva:
            print("existe")
            messages.add_message(request=request, level=messages.SUCCESS, message="Ya existe una reserva para ese consultorio en la fecha seleccionada")
            return redirect('/reservas')
        else:
            print("No existe")
            r = Reserva(paciente=paciente, consultorio=consultorio, inicio=inicio, fin=fin, fecha_reserva=fecha_reserva, precio=precio)
            r.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Reserva Registrada correctamente!")
            return redirect('/reservas')



def reporte_dinero_dia_especifico(request):
    if request.method == "GET":
        return render(request, "reportes/reporte_dinero_dia_especifico.html")
    elif request.method == "POST":
        print(request.POST)
        fecha_reserva = request.POST['fecha_reserva']


        arr = fecha_reserva.split('/')
        fecha_reserva = f"{arr[2]}-{arr[0]}-{arr[1]}"
        print(f"fecha_reserva: {fecha_reserva}")

        reservas = Reserva.objects.filter(fecha_reserva=fecha_reserva)
        print(reservas)
        return render(request, "reportes/reporte_dinero_dia_especifico.html", {
            'reservas': reservas
        })
    

def reporte_consultas_doctor_especifico(request):
    doctores = Doctor.objects.all()
    if request.method == "GET":
        return render(request, "reportes/reporte_consultas_doctor_especifico.html", {
            'doctores': doctores
        })
    elif request.method == "POST":
        print(request.POST)
        doctor_id = request.POST['doctor_id']
        doctor = Doctor.objects.get(id=doctor_id)

        reservas = Reserva.objects.filter(consultorio__doctor=doctor)
        print(reservas)
        return render(request, "reportes/reporte_consultas_doctor_especifico.html", {
            'doctores': doctores,
            'reservas': reservas
        })
        
    
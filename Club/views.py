from django.shortcuts import render
from Club.models import *
from django.http import HttpResponse
from Club.forms import *

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def jugadores(request):
    if request.method == 'POST':
        miformulario = Jugadoresformulario(request.POST)

        print(miformulario)
        
        if miformulario.is_valid:
            
            informacion= miformulario.cleaned_data

            jugador = Jugadores(nombre=informacion['nombre'], apellido=informacion['apellido'], categoria= informacion['categoria'], numerocarnet= informacion['numerocarnet'])
            jugador.save() 
            return render(request, 'Inicio.html')
    else:
        miformulario= Jugadoresformulario

    return render(request, 'jugadores.html', {'miformulario': miformulario})

def buscar(request):
    if request.GET['apellido']:
        apellido= request.GET['apellido']
        nombre= Jugadores.objects.filter(apellido__icontains=apellido)
        
        
        return render(request,'Inicio.html', {"nombre": nombre, "apellido": apellido,})
    else:
        respuesta='No enviaste datos.'
    return render(request, 'Inicio.html', {"respuesta": respuesta})




def entrenadores(request):
    if request.method == 'POST':
        miformulario = Entrenadoresformulario(request.POST)

        print(miformulario)
        
        if miformulario.is_valid:
            
            informacion= miformulario.cleaned_data

            jugador = Entrenadores(nombre=informacion['nombre'], apellido=informacion['apellido'], categoria_cargo= informacion['categoria_cargo'])
            jugador.save() 
            return render(request, 'Inicio.html')
    else:
       miformulario= Entrenadoresformulario
        
    return render(request, 'entrenadores.html', {'miformulario': miformulario})


def comisiondirectiva(request):
    if request.method == 'POST':
        miformulario = Comisionformulario(request.POST)

        print(miformulario)
        
        if miformulario.is_valid:
            
            informacion= miformulario.cleaned_data

            jugador = Comisiondirectiva(nombre=informacion['nombre'], 
                                        apellido=informacion['apellido'], 
                                        email=informacion['email'], 
                                        telefono= informacion['telefono'], 
                                        cargo=informacion['cargo'])
            jugador.save() 
            return render(request, 'Inicio.html')
    else:
        miformulario= Comisionformulario

    return render(request, 'comisiondirectiva.html', {'miformulario': miformulario})
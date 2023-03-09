from django.shortcuts import render
from Club.models import Jugadores
from django.http import HttpResponse

# Create your views here.

def jugador(sefl):

    jugador= Jugadores(nombre='Gaston', apellido= 'Ledesma', categoria='Primera', numerocarnet= 12345)
    jugador.save()
    documentodetexto = f'nombre: {jugador.nombre} apellido: {jugador.apellido} categoria: {jugador.categoria} numero de carnet: {jugador.numerocarnet} '

    return HttpResponse(documentodetexto)
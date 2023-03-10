from django.urls import path
from Club import views

urlpatterns = [
    path('',views.inicio, name= 'Inicio'),
    path('Jugadores',views.jugadores, name= 'Jugadores'),
    path('entrenadores', views.entrenadores, name= 'Entrenadores'),
    path('comisiondirectiva', views.comisiondirectiva, name= 'Comision'),
    path('buscar/', views.buscar)
]
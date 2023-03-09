from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    numerocarnet = models.IntegerField()

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    categoria_cargo = models.CharField(max_length=40)

class Comisiondirectiva(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField() 
    cargo = models.CharField(max_length=40)

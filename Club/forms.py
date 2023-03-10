from django import forms

class Jugadoresformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    categoria=forms.CharField(max_length=40)
    numerocarnet=forms.IntegerField()

class Entrenadoresformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    categoria_cargo=forms.CharField(max_length=40)

class Comisionformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    telefono=forms.IntegerField()
    cargo=forms.CharField(max_length=40)

from tkinter import CASCADE
from django.db import models
from tabnanny import verbose

from DireccionApp.models import *
from ConfiguracionApp.models import*

# Create your models here.

class Perfil(models.Model):
    id= models.AutoField(primary_key=True)
    nombres= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    dui= models.CharField(max_length=12)
    telefono= models.CharField(max_length=10)
    nacionalidad=models.CharField(max_length=50)
    fechan=models.DateField(null=False)
    edad= models.IntegerField()
    idocu= models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    salario= models.FloatField(max_length=10) 
    municipio= models.ForeignKey(Distrito,on_delete=models.CASCADE)
    direccion= models.CharField(max_length=100)
    correo= models.CharField(max_length=40)
    contrasena= models.CharField(max_length=500)
    rcontrasena= models.CharField(max_length=500)
    estado= models.CharField(max_length=10)
    Agencia=models.ForeignKey(Agencia, on_delete=models.CASCADE)
    fechaR=models.DateField(auto_now_add=True)
    estadosoli= models.IntegerField()

    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfils'
        db_table= 'perfil'

    def __str__(self) :
        return self.nombres

class Perfilna(models.Model):
    id= models.AutoField(primary_key=True)
    nombres= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    dui= models.CharField(max_length=12)
    telefono= models.CharField(max_length=10)
    nacionalidad=models.CharField(max_length=50)
    fecha=models.DateField()
    edad= models.IntegerField()
    salario= models.FloatField(max_length=7)
    direccion= models.CharField(max_length=100)
    Agencia=models.ForeignKey(Agencia, on_delete=models.CASCADE)
    observaciones=models.CharField(max_length=300, null=True)
    fechaR=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='perfilna'
        verbose_name_plural='perfilnas'
        db_table= 'Perfilna'
    
class perfildetalle(models.Model):
    iddetalle=models.AutoField(primary_key=True)
    fecharegistro = models.DateTimeField(auto_now_add=True)
    perfil=models.ForeignKey(Perfil, on_delete=models.CASCADE)
    comunidad=models.CharField(max_length=60)
    area=models.CharField(max_length=10)
    tipo=models.IntegerField()
    estado=models.IntegerField()
    class Meta:
        verbose_name='perfildetalle'
        verbose_name_plural='perfildetalles'
        db_table= 'perfildetalle'




    
    
    
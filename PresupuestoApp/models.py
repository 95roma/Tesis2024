from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.

class Presupuestodg(models.Model):
    id= models.AutoField(primary_key=True)
    fecha= models.DateField(null=False)
    mejorarea= models.CharField(max_length=200)
    diasestimadosc= models.CharField(max_length=10)
    ids=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='presupuestodg'
        verbose_name_plural='presupuestodgs'
        db_table= 'presupuestodg'
        

class PresupuestoMateriales(models.Model):
    id= models.AutoField(primary_key=True)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idm=models.ForeignKey(Materiales, on_delete=models.CASCADE)
    idp=models.ForeignKey(Presupuestodg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestomateriales'
        verbose_name_plural='presupuestomaterialess'
        db_table= 'presupuestomateriales'
        
class PresupuestoManoObra(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=100)
    unidad= models.CharField(max_length=10)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idp=models.ForeignKey(Presupuestodg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestomanoobra'
        verbose_name_plural='presupuestomanoobras'
        db_table= 'presupuestomanoobra'

class PresupuestoOtros(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=100)
    unidad= models.CharField(max_length=10)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idp=models.ForeignKey(Presupuestodg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestootros'
        verbose_name_plural='presupuestootross'
        db_table= 'presupuestootros'

class Presupuesto(models.Model):
    id= models.AutoField(primary_key=True)
    subtotal= models.DecimalField(decimal_places=2, max_digits=15)
    asistenciatecn= models.DecimalField(decimal_places=2, max_digits=15)
    comisionporot= models.DecimalField(decimal_places=2, max_digits=15)
    consultabcredoto= models.DecimalField(decimal_places=2, max_digits=15)
    cansaldopend= models.DecimalField(decimal_places=2, max_digits=15)
    pcuota= models.DecimalField(decimal_places=2, max_digits=15)
    total= models.DecimalField(decimal_places=2, max_digits=20)
    notas= models.CharField(max_length=500)
    idp=models.ForeignKey(Presupuestodg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuesto'
        verbose_name_plural='presupuestos'
        db_table= 'presupuesto'



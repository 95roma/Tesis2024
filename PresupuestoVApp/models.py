from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.

class Presupuestovdg(models.Model):
    id= models.AutoField(primary_key=True)
    fecha= models.DateField(null=False)
    tiempoconstruccion= models.CharField(max_length=10)
    modelo= models.CharField(max_length=30)
    dimensionviv= models.CharField(max_length=50)
    cantidadvivienda= models.IntegerField()
    costototalv= models.DecimalField(decimal_places=2, max_digits=15)
    ids=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='presupuestovdg'
        verbose_name_plural='presupuestovdgs'
        db_table= 'presupuestovdg'
        

class PresupuestovMateriales(models.Model):
    id= models.AutoField(primary_key=True)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idm=models.ForeignKey(Materiales, on_delete=models.CASCADE)
    idp=models.ForeignKey(Presupuestovdg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestovmateriales'
        verbose_name_plural='presupuestovmaterialess'
        db_table= 'presupuestovmateriales'

class PresupuestovManoObra(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=100)
    unidad= models.CharField(max_length=10)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idp=models.ForeignKey(Presupuestovdg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestovmanoobra'
        verbose_name_plural='presupuestovmanoobras'
        db_table= 'presupuestovmanoobra'

class PresupuestovTotal(models.Model):
    id= models.AutoField(primary_key=True)
    materiales= models.DecimalField(decimal_places=2, max_digits=15)
    manoobra= models.DecimalField(decimal_places=2, max_digits=15)
    transporte= models.DecimalField(decimal_places=2, max_digits=15)
    solucionsanit= models.DecimalField(decimal_places=2, max_digits=15)
    kitemerg= models.DecimalField(decimal_places=2, max_digits=15)
    herramientas= models.DecimalField(decimal_places=2, max_digits=15)
    totalcostosd= models.DecimalField(decimal_places=2, max_digits=15)
    idp=models.ForeignKey(Presupuestovdg, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestovtotal'
        verbose_name_plural='presupuestovtotals'
        db_table= 'presupuestovtotal'


# para obras adicionales 
class Presupuestovdgobra(models.Model):
    id= models.AutoField(primary_key=True)
    fecha= models.DateField(null=False)
    tipoobra= models.CharField(max_length=100)
    costoobra= models.DecimalField(decimal_places=2, max_digits=15)
    solucionsa= models.DecimalField(decimal_places=2, max_digits=15)
    totalobraa= models.DecimalField(decimal_places=2, max_digits=15)
    idpdg=models.ForeignKey(Presupuestovdg, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='presupuestovdgobra'
        verbose_name_plural='presupuestovdgobras'
        db_table= 'presupuestovdgobra'
        

class PresupuestovMaterialesobra(models.Model):
    id= models.AutoField(primary_key=True)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idm=models.ForeignKey(Materiales, on_delete=models.CASCADE)
    idpo=models.ForeignKey(Presupuestovdgobra, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestovmaterialesobra'
        verbose_name_plural='presupuestovmaterialesobras'
        db_table= 'presupuestovmaterialesobra'

class PresupuestovManoObraobra(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=100)
    unidad= models.CharField(max_length=10)
    preciouni= models.DecimalField(decimal_places=2, max_digits=15)
    cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    subtotal= models.DecimalField(decimal_places=2, max_digits=20)
    idpo=models.ForeignKey(Presupuestovdgobra, on_delete=models.CASCADE)

    class Meta:
        verbose_name='presupuestovmanoobraobra'
        verbose_name_plural='presupuestovmanoobraobras'
        db_table= 'presupuestovmanoobraobra'


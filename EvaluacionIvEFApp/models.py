from django.db import models
from ClienteApp.models import *

# Create your models here.

class Egresosf(models.Model):
    id= models.AutoField(primary_key=True)
    alimentacion= models.DecimalField(decimal_places=2, max_digits=15)
    educacion= models.DecimalField(decimal_places=2, max_digits=15)
    transporte= models.DecimalField(decimal_places=2, max_digits=15)
    salud= models.DecimalField(decimal_places=2, max_digits=15)
    AFP=models.DecimalField(decimal_places=2, max_digits=15)
    servicios= models.DecimalField(decimal_places=2, max_digits=15)
    alquiler= models.DecimalField(decimal_places=2, max_digits=15)
    pplanilla=models.DecimalField(decimal_places=2, max_digits=15)
    pventanilla=models.DecimalField(decimal_places=2, max_digits=15)
    phplhes=models.DecimalField(decimal_places=2, max_digits=15)
    otrosdesc=models.DecimalField(decimal_places=2, max_digits=15)
    recreacion=models.DecimalField(decimal_places=2, max_digits=15)
    imprevistos=models.DecimalField(decimal_places=2, max_digits=15)
    total=models.DecimalField(decimal_places=2, max_digits=15)
    estado=models.IntegerField()
    idp= models.ForeignKey(Perfil, on_delete=models.CASCADE)    
    
    class Meta:
        verbose_name='egresosf'
        verbose_name_plural='egresosfs'
        db_table= 'egresosf'

class Ingresosf(models.Model):
    id= models.AutoField(primary_key=True)
    familiar= models.DecimalField(decimal_places=2, max_digits=15)
    otrosingres= models.DecimalField(decimal_places=2, max_digits=15)
    totali=models.DecimalField(decimal_places=2, max_digits=15)
    ide= models.ForeignKey(Egresosf, on_delete=models.CASCADE)
      
    class Meta:
        verbose_name='ingresosf'
        verbose_name_plural='ingresosfs'
        db_table= 'ingresosf'

class Capacidadpagof(models.Model):
    id= models.AutoField(primary_key=True)
    porcentajee= models.CharField(max_length=10)
    disponible= models.DecimalField(decimal_places=2, max_digits=15)
    porcentajedis= models.CharField(max_length=10)
    cuota=models.DecimalField(decimal_places=2, max_digits=15)
    porcentajecuot= models.CharField(max_length=10)
    superavit= models.DecimalField(decimal_places=2, max_digits=15)
    deficit=models.DecimalField(decimal_places=2, max_digits=15)
    estado= models.CharField(max_length=10)
    ide= models.ForeignKey(Egresosf, on_delete=models.CASCADE)   
    
    class Meta:
        verbose_name='capacidadpagof'
        verbose_name_plural='capacidadpagofs'
        db_table= 'capacidadpagof'

class Bienesh(models.Model):
    id= models.AutoField(primary_key=True)
    numero= models.CharField(max_length=10,null=True)
    descripcionbien= models.CharField(max_length=100,null=True)
    preciocompra= models.DecimalField(decimal_places=2, max_digits=10,null=True)
    cuotamensual=models.DecimalField(decimal_places=2, max_digits=10,null=True)
    ide= models.ForeignKey(Egresosf, on_delete=models.CASCADE)   
    
    class Meta:
        verbose_name='bienesh'
        verbose_name_plural='bieneshs'
        db_table= 'bienesh'


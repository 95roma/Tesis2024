from django.db import models
from SolicitudesApp.models import *
from ConfiguracionApp.models import *


# Create your models here.
class Declaracionjc(models.Model):
    iddj= models.AutoField(primary_key=True)  
    nombrepna=models.CharField(max_length=60)
    duipna=models.CharField(max_length=12)  
    toperacion= models.ForeignKey(TipoOperacion, on_delete=models.CASCADE)  
    ncredito= models.CharField(max_length=20)
    monto= models.CharField(max_length=30)
    plazo= models.CharField(max_length=20)
    cuota= models.CharField(max_length=30)
    formapago= models.CharField(max_length=20)
    cancelacionda= models.CharField(max_length=5)
    rpagosa= models.CharField(max_length=5)
    procedenciafond= models.CharField(max_length=40, null=True)
    ids= models.ForeignKey(solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='declaracionjc'
        verbose_name_plural='declaracionjcs'
        db_table= 'declaracionjc'

class Declaracionjcaern(models.Model):
    idae= models.AutoField(primary_key=True)
    empleadoen= models.CharField(max_length=50)
    profecinalind=models.CharField(max_length=50, null=True)
    conocimientoen= models.CharField(max_length=50, null=True)
    empresarioen= models.CharField(max_length=50, null=True)
    especificaro= models.CharField(max_length=50, null=True)
    iddj= models.ForeignKey(Declaracionjc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='declaracionjcaern'
        verbose_name_plural='declaracionjcaerns'
        db_table= 'declaracionjcaern'

class Declaracionjcjnm(models.Model):
    idjn= models.AutoField(primary_key=True)
    empresa= models.CharField(max_length=50, null=True)
    industriade=models.CharField(max_length=50, null=True)
    comercio= models.CharField(max_length=50, null=True)
    especificarot= models.CharField(max_length=40, null=True)
    iddj= models.ForeignKey(Declaracionjc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='declaracionjcjnm'
        verbose_name_plural='declaracionjcjnms'
        db_table= 'declaracionjcjnm'




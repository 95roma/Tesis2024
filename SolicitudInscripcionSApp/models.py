from django.db import models
from SolicitudesApp.models import *
from ConfiguracionApp.models import *

# Create your models here.
class Solicitudis(models.Model):
    id= models.AutoField(primary_key=True)
    montoaa= models.DecimalField(decimal_places=2, max_digits=15)
    nuevoma= models.DecimalField(decimal_places=2, max_digits=15)
    montot= models.DecimalField(decimal_places=2, max_digits=15)
    plazo= models.CharField(max_length=10)
    garantia=models.CharField(max_length=50)
    estatura= models.CharField(max_length=15)
    peso= models.CharField(max_length=15)
    dbeneficiario= models.CharField(max_length=30)
    ids= models.ForeignKey(solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='solicitudis'
        verbose_name_plural='solicitudiss'
        db_table= 'solicitudis'

class SolicitudisPadecimiento(models.Model):
    id= models.AutoField(primary_key=True)
    idsisenf= models.ForeignKey(SolicitudisEnfermedad, on_delete=models.CASCADE)
    idp= models.ForeignKey(Perfil, on_delete=models.CASCADE)
    fechap=models.DateField(null=True, blank=True)
    tratamientor=models.CharField(max_length=200)
    situaciona=models.CharField(max_length=100)
    estado= models.CharField(max_length=10)
      
    class Meta:
        verbose_name='solicitudispadecimiento'
        verbose_name_plural='solicitudispadecimientos'
        db_table= 'solicitudispadecimiento'

class Solicitudisdadf(models.Model):
    id= models.AutoField(primary_key=True)
    tienedadf=models.CharField(max_length=5)
    detallesdadf=models.CharField(max_length=50)
    fumacp=models.CharField(max_length=5)
    cuantosd=models.CharField(max_length=15)
    bebidadalc=models.CharField(max_length=5)
    frecuenciaalc=models.CharField(max_length=25)
    tratamientomd=models.CharField(max_length=5)
    detalletmd=models.CharField(max_length=50)
    practicaad=models.CharField(max_length=5)
    clasead=models.CharField(max_length=25)
    frecuenciaad=models.CharField(max_length=25)
    segurodd=models.CharField(max_length=5)
    idsis= models.ForeignKey(Solicitudis, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='solicitudisdadf'
        verbose_name_plural='solicitudisdadfs'
        db_table= 'solicitudisdadf'


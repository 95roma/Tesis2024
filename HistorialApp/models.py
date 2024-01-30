from django.db import models
from django.db import connections
from ClienteApp.models import *
from SolicitudesApp.models import solicitud

# Create your models here.


class RangoHis(models.Model):
    id= models.AutoField(primary_key=True)
    minimo= models.FloatField(max_length=10)
    maximo= models.FloatField(max_length=10)
    tipo= models.CharField(max_length=30)
    porcentaje= models.DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        verbose_name='RangoHis'
        verbose_name_plural='RangoHis'
        db_table= 'rangohis'


class RegHis(models.Model):
    id= models.AutoField(primary_key=True)
    puntaje= models.FloatField(max_length=5)
    fecha= models.DateField(null=False)
    idRango= models.ForeignKey(RangoHis, on_delete=models.CASCADE)
    idsolicitud= models.ForeignKey(solicitud, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name='RegHis'
        verbose_name_plural='RegHis'
        db_table= 'reghis'

from django.db import models
from SolicitudesApp.models import *


# Create your models here. 
class DocumentosCliente(models.Model):
    id= models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now = True)
    archivo= models.FileField(upload_to = "documentos/")
    nombreD = models.CharField(max_length=200)  
    ids=models.ForeignKey(solicitud, on_delete=models.CASCADE)

    class Meta:
        verbose_name='DocumentosCliente'
        verbose_name_plural='DocumentosClientes'
        db_table= 'DocumentosCliente'




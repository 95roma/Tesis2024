from django.db import models
from SolicitudesApp.models import*

# Create your models here.

# para la lista de chequeo
# para la lista de chequeo
class listaChequeo(models.Model):
    id= models.AutoField(primary_key=True)
    fecha=models.DateField(null=False) # la fecha no debe ir vacia
    solicitudc= models.CharField(max_length=5, null=True)
    fotocdui= models.CharField(max_length=5, null=True)
    recibosagua= models.CharField(max_length=5, null=True)
    recibosluz= models.CharField(max_length=5, null=True)
    recibostelef= models.CharField(max_length=5, null=True)
    refercs= models.CharField(max_length=5, null=True)
    constemp= models.CharField(max_length=5, null=True)
    tacoisss= models.CharField(max_length=5, null=True)
    analisisec= models.CharField(max_length=5, null=True)
    balance= models.CharField(max_length=5, null=True)
    balanceres= models.CharField(max_length=5, null=True)
    copiaduifia= models.CharField(max_length=5, null=True)
    recibosfiaagua= models.CharField(max_length=5, null=True)
    recibosfialuz= models.CharField(max_length=5, null=True)
    constempfia= models.CharField(max_length=5, null=True)
    refercsfia= models.CharField(max_length=5, null=True)
    inspecciontec= models.CharField(max_length=5, null=True)
    presupuestocons= models.CharField(max_length=5, null=True)
    certifext= models.CharField(max_length=5, null=True)
    carenciabien= models.CharField(max_length=5, null=True)
    fotocescrit= models.CharField(max_length=5, null=True)
    declaracions= models.CharField(max_length=5, null=True)
    infdicom= models.CharField(max_length=5, null=True)
    docsing= models.CharField(max_length=5, null=True)
    docrem= models.CharField(max_length=5, null=True)
    cancelpec= models.CharField(max_length=5, null=True)
    finiquitos= models.CharField(max_length=5, null=True)
    hojaaprovc= models.CharField(max_length=5, null=True)
    cartaelbmutuo= models.CharField(max_length=5, null=True)
    recibpagp= models.CharField(max_length=5, null=True)
    ordendesi= models.CharField(max_length=5, null=True)
    permisocons= models.CharField(max_length=5, null=True)
    cartaentcd= models.CharField(max_length=5, null=True)
    fotocmutuo= models.CharField(max_length=5, null=True)
    gestioncobro= models.CharField(max_length=5, null=True)
    estado= models.CharField(max_length=10)
    ids=models.ForeignKey(solicitud, on_delete=models.CASCADE)

    class Meta:
        verbose_name='listaChequeo'
        verbose_name_plural='listaChequeos'
        db_table= 'listaChequeo'



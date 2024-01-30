from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.
class Inspeccionl(models.Model):
    id= models.AutoField(primary_key=True)
    fecha= models.DateField(null=False)
    hora= models.CharField(max_length=15)
    telefonop= models.CharField(max_length=10)
    telefonos= models.CharField(max_length=10)
    terceraedad= models.CharField(max_length=15)
    adultos= models.CharField(max_length=15)
    ninos= models.CharField(max_length=15)
    personadisc= models.CharField(max_length=15)
    propietarioter= models.CharField(max_length=100)
    latitud= models.CharField(max_length=100)
    longitud= models.CharField(max_length=100)
    inmueble= models.CharField(max_length=10)
    existeotraviv= models.CharField(max_length=5)
    terrenoagricola= models.CharField(max_length=5)
    anchocv= models.CharField(max_length=15)
    largocv= models.CharField(max_length=15)
    areacv= models.CharField(max_length=15)
    anchoaf= models.CharField(max_length=15)
    largoaf= models.CharField(max_length=15)
    areaaf= models.CharField(max_length=15)
    ids= models.ForeignKey(solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='inspeccionl'
        verbose_name_plural='inspeccionls'
        db_table= 'inspeccionl'


class Inspeccionlcisr(models.Model):
    id= models.AutoField(primary_key=True)
    idif=models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    existe= models.CharField(max_length=5)
    idip=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='inspeccionlcisr'
        verbose_name_plural='inspeccionlcisrs'
        db_table= 'inspeccionlcisr'

class Riesgosipl(models.Model):
    id= models.AutoField(primary_key=True)
    distaludes= models.CharField(max_length=15)
    disriosc= models.CharField(max_length=15)
    disladerasc= models.CharField(max_length=15)
    distorresantenas= models.CharField(max_length=15)
    idipl=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='riesgosipl'
        verbose_name_plural='priesgosipls'
        db_table= 'riesgosipl'
    
class ComentariosObsipl(models.Model):
    id= models.AutoField(primary_key=True)
    comentario= models.CharField(max_length=400)
    observaciones= models.CharField(max_length=400)
    idipl=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='comentariosobsip'
        verbose_name_plural='comentariosobsips'
        db_table= 'comentariosobsipl'

class ViasAccesoipl(models.Model):
    id= models.AutoField(primary_key=True)
    tipovia= models.CharField(max_length=35)
    idipl=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='viasaccesoipl'
        verbose_name_plural='viasaccesoipls'
        db_table= 'viasaccesoipl'  
        
class Factibilidadipl(models.Model):
    id= models.AutoField(primary_key=True)
    detalle= models.CharField(max_length=300)
    idipl=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='factibilidadipl'
        verbose_name_plural='factibilidadipls'
        db_table= 'factibilidadipl'

class DescripcionProyectoipl(models.Model):
    id= models.AutoField(primary_key=True)
    modeloviviedac= models.CharField(max_length=30)
    solucionsanitariap= models.CharField(max_length=300)
    obrasadicionalesconst= models.CharField(max_length=300)
    observtecnicas= models.CharField(max_length=400)
    actividadbrfp= models.CharField(max_length=500)
    idipl=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='descripcionproyectoipl'
        verbose_name_plural='descripcionproyectoipls'
        db_table= 'descripcionproyectoipl'

class ResponSolicitanteipl(models.Model):
    id= models.AutoField(primary_key=True)
    mojoneslote= models.CharField(max_length=5)
    linderoslote= models.CharField(max_length=5)
    resguardomather= models.CharField(max_length=5)
    auxiliaresconst= models.CharField(max_length=5)
    aguapotable= models.CharField(max_length=5)
    energiaelectrica= models.CharField(max_length=5)
    idipl=models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='responsolicitanteipl'
        verbose_name_plural='responsolicitanteipls'
        db_table= 'responsolicitanteipl'

# para primera inspección
class pInspeccionl(models.Model):
    id= models.AutoField(primary_key=True)
    ninspeccion= models.CharField(max_length=25)
    fecha= models.DateField(null=False)
    esquema= models.FileField(upload_to = "documentos/", blank=True)
    ubicacion = models.FileField(upload_to="documentos/", blank=True)
    idil= models.ForeignKey(Inspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='pInspeccionl'
        verbose_name_plural='pInspeccionls'
        db_table= 'pInspeccionl'

class ImagenPInspeccionl(models.Model):
    id= models.AutoField(primary_key=True)
    reportef= models.FileField(upload_to="documentos/", blank=True) 
    idpil= models.ForeignKey(pInspeccionl, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='imagenpInspeccionl'
        verbose_name_plural='imagenpInspeccionls'
        db_table= 'imagenpInspeccionl'


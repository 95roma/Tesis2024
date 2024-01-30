from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.
class InspeccionM(models.Model):
    id= models.AutoField(primary_key=True)
    fecha= models.DateField(null=False)
    hora= models.CharField(max_length=15)
    telefonop= models.CharField(max_length=10)
    telefonos= models.CharField(max_length=10)
    terceraedad= models.CharField(max_length=15)
    adultos= models.CharField(max_length=15)
    ninos= models.CharField(max_length=15)
    personadisc= models.CharField(max_length=15)
    propietarioinm= models.CharField(max_length=100)
    parentescosol= models.CharField(max_length=50)
    latitud= models.CharField(max_length=100)
    longitud= models.CharField(max_length=100)
    inmueble= models.CharField(max_length=10)
    usoactual= models.CharField(max_length=15)
    existeotraviv= models.CharField(max_length=5)
    usoactualotv= models.CharField(max_length=15)
    comentariosrelv= models.CharField(max_length=200)
    ids= models.ForeignKey(solicitud, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name='inspeccionm'
        verbose_name_plural='inspeccionms'
        db_table= 'inspeccionm'

class InfraestructuraInmuebleipm(models.Model):
    id= models.AutoField(primary_key=True)
    existe= models.CharField(max_length=50)
    estado= models.CharField(max_length=100)
    tiposistema= models.CharField(max_length=100)
    idif=models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    idip=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='infraestructurainmuebleipm'
        verbose_name_plural='infraestructurainmuebleipms'
        db_table= 'infraestructurainmuebleipm'


class Inspeccionesirm(models.Model):
    id= models.AutoField(primary_key=True)
    existe= models.CharField(max_length=50)
    idif=models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    idip=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='inspeccionesirm'
        verbose_name_plural='inspeccionesirms'
        db_table= 'inspeccionesirm'

class Riesgosipm(models.Model):
    id= models.AutoField(primary_key=True)
    distaludes= models.CharField(max_length=15)
    disriosc= models.CharField(max_length=15)
    disladerasc= models.CharField(max_length=15)
    distorresantenas= models.CharField(max_length=15)
    idipl=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='riesgosipm'
        verbose_name_plural='priesgosipms'
        db_table= 'riesgosipm'

class ViasAccesoipm(models.Model):
    id= models.AutoField(primary_key=True)
    tipovia= models.CharField(max_length=35)
    idipl=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='viasaccesoipm'
        verbose_name_plural='viasaccesoipms'
        db_table= 'viasaccesoipm'

class PlanMejoramientoipm(models.Model):
    id= models.AutoField(primary_key=True)
    etapas= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=300)
    idip=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='planmejoramientoipm'
        verbose_name_plural='planmejoramientoipms'
        db_table= 'planmejoramientoipm'
    
class Factibilidadipm(models.Model):
    id= models.AutoField(primary_key=True)
    detalle= models.CharField(max_length=300)
    idip=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='factibilidadipm'
        verbose_name_plural='factibilidadipms'
        db_table= 'factibilidadipm'

class DMejoramientoipm(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=300)
    diasestimados= models.CharField(max_length=10)
    idip=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='dmejoramientoipm'
        verbose_name_plural='dmejoramientoipms'
        db_table= 'dmejoramientoipm'  

class Esquemasipm(models.Model):
    id= models.AutoField(primary_key=True)
    esquemasitio= models.FileField(upload_to = "documentos/", blank=True)
    esquemamejora= models.FileField(upload_to = "documentos/", blank=True)
    idip=models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='esquemasipm'
        verbose_name_plural='esquemasipms'
        db_table= 'esquemasipm'  

# para primera inspección
class pInspeccionm(models.Model):
    id= models.AutoField(primary_key=True)
    ninspeccion= models.CharField(max_length=25)
    fecha= models.DateField(null=False)
    mejoraar= models.CharField(max_length=50)
    esquema= models.FileField(upload_to = "documentos/", blank=True)
    idim= models.ForeignKey(InspeccionM, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='pInspeccionm'
        verbose_name_plural='pInspeccionms'
        db_table= 'pInspeccionm'

class ImagenPInspeccionm(models.Model):
    id= models.AutoField(primary_key=True)
    imagen = models.FileField(upload_to="documentos/", blank=True)
    idpim= models.ForeignKey(pInspeccionm, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='imagenpInspeccionm'
        verbose_name_plural='imagenpInspeccionms'
        db_table= 'imagenpInspeccionm'


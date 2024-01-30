from django.db import models
from ClienteApp.models import *
from SolicitudesApp.models import *

# Create your models here.

class Clientedg(models.Model):
    iddg= models.AutoField(primary_key=True)
    fecha= models.DateField(null=False)        
    codigo= models.CharField(max_length=10)  
    calidadactua= models.CharField(max_length=10)
    nombrecc= models.CharField(max_length=60)
    conocidocomo= models.CharField(max_length=60)
    profesiondui= models.CharField(max_length=15)
    nacionalidad=models.CharField(max_length=50)
    docidentidad= models.CharField(max_length=5)
    numerodoc= models.CharField(max_length=40)
    fechavdoc= models.DateField(null=True, blank=True)   
    ocupacionaa= models.CharField(max_length=50)
    direcciondomic= models.CharField(max_length=100)
    correoe= models.CharField(max_length=30)     
    telcelular=models.CharField(max_length=10)
    telfijo=models.CharField(max_length=10)
    estatuspropiedad= models.CharField(max_length=60)
    nombreconyuge= models.CharField(max_length=60) 
    estado= models.CharField(max_length=10) 
    ids= models.ForeignKey(solicitud, on_delete=models.CASCADE)

    class Meta:
        verbose_name='clientedg'
        verbose_name_plural='clientedgs'
        db_table= 'clientedg'

class Clienteaec(models.Model):
    idaec= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    tipoact= models.CharField(max_length=20)
    lugartrab= models.CharField(max_length=50)
    cargodes= models.CharField(max_length=50)    
    tiempolaborar= models.CharField(max_length=20)
    procedenciafod= models.CharField(max_length=30)
    rangoingresosemp=models.CharField(max_length=20)
    otrosingresos= models.CharField(max_length=15)
    procedenciaoi= models.CharField(max_length=30,null=True)
    estado= models.CharField(max_length=10) 

    class Meta:
        verbose_name='clienteaec'
        verbose_name_plural='clienteaecs'
        db_table= 'clienteaec'

class Clientedn(models.Model):
    iddn= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    nombreneg= models.CharField(max_length=50)
    prodserv= models.CharField(max_length=200)
    direccionneg= models.CharField(max_length=20)
    fechaia= models.DateField(null=True, blank=True) #  permitirá que el campo sea nulo en la base de datos y también permitirá que se deje en blanco en los formularios.
    rangoingresos=models.CharField(max_length=20)
    otrosingresos= models.CharField(max_length=15)
    procedenciaoi= models.CharField(max_length=30,null=True)
    estado= models.CharField(max_length=10) 

    class Meta:
        verbose_name='clientedn'
        verbose_name_plural='clientedns'
        db_table= 'clientedn'

        
class Clienterrf(models.Model):
    idrrf= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    rremesa= models.CharField(max_length=5) 
    nombreremitente= models.CharField(max_length=40,null=True)
    parentesco= models.CharField(max_length=15,null=True)
    paisorigenr= models.CharField(max_length=15,null=True)
    monto= models.CharField(max_length=20,null=True) 
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='clienterrf'
        verbose_name_plural='clienterrfs'
        db_table= 'clienterrf'

class Clientedc(models.Model):
    iddc= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    clasifcredito= models.CharField(max_length=30)
    montodc= models.CharField(max_length=30)
    cuotadc= models.CharField(max_length=30)
    rpagosadic= models.CharField(max_length=5)
    procpagosadic=models.CharField(max_length=50,null=True)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='clientedc'
        verbose_name_plural='clientedcs'
        db_table= 'clientedc'

class Clientepbo(models.Model):
    idpbo= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    noaplica= models.CharField(max_length=10,null=True)
    nombrecomp= models.CharField(max_length=60,null=True)
    direccionp= models.CharField(max_length=50,null=True)
    tdocumento= models.CharField(max_length=10,null=True)
    ndocumento= models.CharField(max_length=20,null=True)
    benefpeps= models.CharField(max_length=5,null=True)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='clientepbo'
        verbose_name_plural='clientepbos'
        db_table= 'clientepbo'

class Clientept(models.Model):
    idpt= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    prestamos= models.CharField(max_length=50,null=True)
    espotros= models.CharField(max_length=50,null=True)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='clientept'
        verbose_name_plural='clientepts'
        db_table= 'clientept'

class Clientepeps(models.Model):
    idpeps= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    ustedpeps= models.CharField(max_length=5)
    relacionpeps= models.CharField(max_length=20)
    nombrep= models.CharField(max_length=60,null=True)
    puestdesemp= models.CharField(max_length=50,null=True)
    pergestiondesde= models.CharField(max_length=20,null=True)
    pergestionhasta= models.CharField(max_length=20,null=True)
    grado=models.CharField(max_length=10,null=True)
    parentesco=models.CharField(max_length=30,null=True)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='clientepeps'
        verbose_name_plural='clientepepss'
        db_table= 'clientepeps'

class Clientepus(models.Model):
    idpus= models.AutoField(primary_key=True)
    iddg= models.ForeignKey (Clientedg, on_delete=models.CASCADE) 
    valedefnf= models.CharField(max_length=5)
    veridireccion= models.CharField(max_length=5)
    verificadopor= models.CharField(max_length=60)
    codigoe= models.CharField(max_length=30)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='clientepus'
        verbose_name_plural='clientepuss'
        db_table= 'clientepus'  
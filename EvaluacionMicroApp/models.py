from django.db import models
from ClienteApp.models import *

# Create your models here.
class Balancesm(models.Model):
    id= models.AutoField(primary_key=True)
    tiponegocio= models.CharField(max_length=100)
    estado = models.IntegerField()## Estado para saber que proceso lleva y si se desabilita por dicom
    idp= models.ForeignKey(Perfil, on_delete=models.CASCADE)    
    
    class Meta:
        verbose_name='balancesm'
        verbose_name_plural='balancesms'
        db_table= 'balancesm'

class Activobsm(models.Model):
    id= models.AutoField(primary_key=True)
    tcirculantea= models.DecimalField(decimal_places=2, max_digits=15)
    caja= models.DecimalField(decimal_places=2, max_digits=15)
    bancos= models.DecimalField(decimal_places=2, max_digits=15)
    cuentaspc= models.DecimalField(decimal_places=2, max_digits=15)
    inventarios=models.DecimalField(decimal_places=2, max_digits=15)
    tfijoa= models.DecimalField(decimal_places=2, max_digits=15)
    mobiliario= models.DecimalField(decimal_places=2, max_digits=15)
    terrenos=models.DecimalField(decimal_places=2, max_digits=15)
    vehiculos=models.DecimalField(decimal_places=2, max_digits=15)
    totalactivo=models.DecimalField(decimal_places=2, max_digits=15)
    idbs= models.ForeignKey(Balancesm, on_delete=models.CASCADE)    
    
    class Meta:
        verbose_name='activobsm'
        verbose_name_plural='bactivobms'
        db_table= 'activobsm'

class Pasivobsm(models.Model):
    id= models.AutoField(primary_key=True)
    tcirculantep=models.DecimalField(decimal_places=2, max_digits=15)
    proveedores=models.DecimalField(decimal_places=2, max_digits=15)
    cuentaspp=models.DecimalField(decimal_places=2, max_digits=15)
    prestamoscp=models.DecimalField(decimal_places=2, max_digits=15)
    fijop=models.DecimalField(decimal_places=2, max_digits=15)
    prestamoslp=models.DecimalField(decimal_places=2, max_digits=15)
    totalpasivo=models.DecimalField(decimal_places=2, max_digits=15)
    patrimonio=models.DecimalField(decimal_places=2, max_digits=15)
    capital=models.DecimalField(decimal_places=2, max_digits=15) #  decimal_places=2, lo cual indica que queremos que se guarden dos decimales después del punto. También hemos establecido max_digits=8, lo cual indica que el campo puede tener hasta 8 dígitos en total
    pasivompatrim=models.DecimalField(decimal_places=2, max_digits=15)
    idbs= models.ForeignKey(Balancesm, on_delete=models.CASCADE)     
    
    class Meta:
        verbose_name='pasivobsm'
        verbose_name_plural='pasivobsms'
        db_table= 'pasivobsm'

class Estadorm(models.Model):
    id= models.AutoField(primary_key=True)
    ventast= models.DecimalField(decimal_places=2, max_digits=15)
    costovent= models.DecimalField(decimal_places=2, max_digits=15)
    utilidadbt= models.DecimalField(decimal_places=2, max_digits=15)
    gastosgral=models.DecimalField(decimal_places=2, max_digits=15)
    transporte= models.DecimalField(decimal_places=2, max_digits=15)
    servicios= models.DecimalField(decimal_places=2, max_digits=15)
    impuestos=models.DecimalField(decimal_places=2, max_digits=15)
    alquiler=models.DecimalField(decimal_places=2, max_digits=15)
    cuotaprest=models.DecimalField(decimal_places=2, max_digits=15)
    imprevistoser=models.DecimalField(decimal_places=2, max_digits=15)
    utilidadneta=models.DecimalField(decimal_places=2, max_digits=15)
    mensual=models.DecimalField(decimal_places=2, max_digits=15)
    idb= models.ForeignKey(Balancesm, on_delete=models.CASCADE)    
    
    class Meta:
        verbose_name='estadorm'
        verbose_name_plural='estadorms'
        db_table= 'estadorm'

class Egresosm(models.Model):
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
    idb= models.ForeignKey(Balancesm, on_delete=models.CASCADE)    
    
    class Meta:
        verbose_name='egresosm'
        verbose_name_plural='egresosms'
        db_table= 'egresosm'

class Ingresosm(models.Model):
    id= models.AutoField(primary_key=True)
    negocio= models.DecimalField(decimal_places=2, max_digits=15)
    remesas= models.DecimalField(decimal_places=2, max_digits=15)
    totali=models.DecimalField(decimal_places=2, max_digits=15)
    ide= models.ForeignKey(Egresosm, on_delete=models.CASCADE)
      
    class Meta:
        verbose_name='ingresosm'
        verbose_name_plural='ingresosms'
        db_table= 'ingresosm'

class Capacidadpagom(models.Model):
    id= models.AutoField(primary_key=True)
    porcentajee= models.CharField(max_length=10)
    disponible= models.DecimalField(decimal_places=2, max_digits=15)
    porcentajedis= models.CharField(max_length=10)
    cuota=models.DecimalField(decimal_places=2, max_digits=15)
    porcentajecuot= models.CharField(max_length=10)
    superavit= models.DecimalField(decimal_places=2, max_digits=15)
    deficit=models.DecimalField(decimal_places=2, max_digits=15)
    estado= models.CharField(max_length=10)
    ide= models.ForeignKey(Egresosm, on_delete=models.CASCADE)   
    
    class Meta:
        verbose_name='capacidadpagom'
        verbose_name_plural='capacidadpagoms'
        db_table= 'capacidadpagom'




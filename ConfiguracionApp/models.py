from django.db import connections
from django.db import models
from DireccionApp.models import *

# Create your models here.
class Agencia(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=100)
    telefono= models.CharField(max_length=9)
    telefono2= models.CharField(max_length=9)
    departamento= models.CharField(max_length=20)
    municipio= models.CharField(max_length=30)
    distrito=models.CharField(max_length=20)
    estado=models.IntegerField()

    class Meta:
        verbose_name='agencia'
        verbose_name_plural='agencias'
        db_table= 'agencia'

class Salario(models.Model):
    id= models.AutoField(primary_key=True)
    tiposalario=models.CharField(max_length=100)
    salariomaximo= models.DecimalField(decimal_places=2, max_digits=10)
    salariominimo= models.DecimalField(decimal_places=2, max_digits=10)
    fechai=models.DateField(null=False)
    fechaf= models.DateField(null=True, blank=True) #permite q la fecha quede vacia
    estado= models.CharField(max_length=10)

    

    class Meta:
        verbose_name='salario'
        verbose_name_plural='salarios'
        db_table= 'salario'



class Ocupacion(models.Model):
    id= models.AutoField(primary_key=True)
    ocupacion= models.CharField(max_length=50)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='ocupacion'
        verbose_name_plural='ocupacions'
        db_table= 'ocupacion'

class ZonaAgencia(models.Model):
    idzona_agencia=models.AutoField(primary_key=True)
    nombrezona=models.CharField(max_length=60)
    agencia=models.ForeignKey(Agencia, on_delete=models.CASCADE)

    class Meta:
        verbose_name='ZonaAgencia'
        verbose_name_plural='ZonaAgencias'
        db_table= 'ZonaAgencia'

    def __str__(self) :
        return self.nombrezona

#es tabla pueba  
class Zona(models.Model):
    idzona=models.AutoField(primary_key=True)
    zona=models.ForeignKey(ZonaAgencia, on_delete=models.CASCADE)
    distri=models.ForeignKey(Distrito, on_delete=models.CASCADE)


    class Meta:
        verbose_name='zona'
        verbose_name_plural='zonas'
        db_table= 'zona'

class TipoDocumento(models.Model):
    idtipo = models.AutoField(primary_key=True)
    nombreD = models.CharField(max_length=100)
    estado = models.IntegerField()


    class Meta:
        verbose_name='TipoDocumento'
        verbose_name_plural='TipoDocumentos'
        db_table= 'TipoDocumento'


class SolicitudisEnfermedad(models.Model):
    id= models.AutoField(primary_key=True)
    nombreenf= models.CharField(max_length=50)
    estado= models.CharField(max_length=10)
    personal= models.CharField(max_length=15) # para difernciar la enfermedad adicional que agrego el cliente

    
    class Meta:
        verbose_name='solicitudisenfermedad'
        verbose_name_plural='solicitudisenfermedads'
        db_table= 'solicitudisenfermedad'


class Materiales(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=100)
    unidad= models.CharField(max_length=10)
    estado= models.CharField(max_length=10)
    
    class Meta:
        verbose_name='material'
        verbose_name_plural='materials'
        db_table= 'material'



class Infraestructura(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    tipo= models.CharField(max_length=100)
    tipolm= models.CharField(max_length=100)
    estado= models.CharField(max_length=10)

    class Meta:
        verbose_name='infraestructura'
        verbose_name_plural='infraestructuras'
        db_table= 'infraestructura'

class TipoOperacion(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100)
    estado= models.CharField(max_length=10)
  
    class Meta:
        verbose_name='tipooperacion'
        verbose_name_plural='tipooperacions'
        db_table= 'tipooperacion'

class TasaInteres(models.Model):
     id=models.AutoField(primary_key=True)
     numerocredito=models.CharField(max_length=60)
     interes=models.IntegerField()
     estado=models.IntegerField()
     class Meta:
        verbose_name='TasaInteres'
        verbose_name_plural='TasaInteres'
        db_table= 'TasaInteres'


class Alternativa(models.Model):
      id=models.AutoField(primary_key=True)
      alternativa=models.CharField(max_length=100)
      montominimo=models.FloatField(max_length=8)
      montomaximo=models.FloatField(max_length=8)
      plazo=models.IntegerField()
      plazomese=models.IntegerField()
      interes=models.ForeignKey(TasaInteres, on_delete=models.CASCADE)
      estado=models.IntegerField()
      class Meta:
         verbose_name='Alternativa'
         verbose_name_plural='Alternativas'
         db_table= 'Alternativa'

class RangoFinan(models.Model):#Rango de financiamiento
    id=models.AutoField(primary_key=True)
    vecesfinan=models.DecimalField(max_digits=5, decimal_places=2)
    montominimo=models.DecimalField(max_digits=8, decimal_places=2)
    montomaximo=models.DecimalField(max_digits=8, decimal_places=2)
    idalter=models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    idsal=models.ForeignKey(Salario, on_delete=models.CASCADE)
    class Meta:
         verbose_name='RangoFinan'
         verbose_name_plural='RangoFinan'
         db_table= 'RangoFinan'

class ModeloVivienda(models.Model): 
    id= models.AutoField(primary_key=True)
    topovivienda = models.CharField(max_length=200)  
    modelo= models.FileField(upload_to = "documentos/")
    montoc= models.DecimalField(decimal_places=2, max_digits=20)
    descripcion=models.CharField(max_length=500)
    class Meta:
        verbose_name='ModeloVivienda'
        verbose_name_plural='ModeloViviendas'
        db_table= 'ModeloVivienda'
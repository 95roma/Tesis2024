from django.db import models
from ConfiguracionApp.models import *
from ClienteApp.models import Perfil

# Create your models here.
class solicitud(models.Model):
    id= models.AutoField(primary_key=True)
    tipoobra=models.CharField(max_length=10)
    fecha=models.DateField(null=False)
    numero=models.CharField(max_length=12)
    comunidad=models.CharField(max_length=50)
    area=models.CharField(max_length=15)
    tipo=models.CharField(max_length=10) # si la solicitud es micro o natural
    tipoingreso=models.CharField(max_length=10,null=True)# solo para natural, tipo empleo o remesa
    estado=models.CharField(max_length=15)
    observaciones=models.CharField(max_length=300, null=True)
    estadosoli=models.IntegerField(null=True)
    perfil=models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        verbose_name='solicitud'
        verbose_name_plural='solicitudes'
        db_table= 'solicitud'

class datosPersonales(models.Model): # para cliente
      id= models.AutoField(primary_key=True)      
      lugarduiC=models.CharField(max_length=100)
      fechaduiC=models.DateField()
      lugarnaciC=models.CharField(max_length=100)
      estadocivilC=models.CharField(max_length=30)
      generoC=models.CharField(max_length=12)
      profesion=models.CharField(max_length=40)
      estadoC= models.CharField(max_length=10)
      idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
      estadosoli=models.IntegerField(null=True)
      class Meta:
            verbose_name='datosPersonales'
            verbose_name_plural='datosPersonales'
            db_table= 'datosPersonales'

class DatosPersonalesF(models.Model): # para tipo conyuge o codeudor
       id= models.AutoField(primary_key=True)
       tipo=models.CharField(max_length=12)
       nombrefia= models.CharField(max_length=50)
       apellidofia= models.CharField(max_length=50)
       duifia= models.CharField(max_length=12)
       lugarduifia= models.CharField(max_length=30)
       fechaduifia=models.DateField(null=False)
       fechanacifia=models.DateField(null=False)
       lugarnacifia= models.CharField(max_length=30)
       edadfia= models.IntegerField()      
       estadocivilfia=models.CharField(max_length=30)
       generofia=models.CharField(max_length=12)
       profefia=models.CharField(max_length=30)
       estadofia= models.IntegerField()
       idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
       estadosoli=models.IntegerField(null=True)
       class Meta:
            verbose_name='DatosPersonalesF'
            verbose_name_plural='DatosPersonalesFs'
            db_table= 'DatosPersonalesF'

class grupoFamiliar(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    edad= models.CharField(max_length=10)
    salario= models.FloatField()
    trabajo=models.CharField(max_length=50)
    parentesco=models.CharField(max_length=50)
    estado= models.IntegerField()
    estadosoli=models.IntegerField(null=True)
    class Meta:
        verbose_name='grupoFamiliar'
        verbose_name_plural='grupoFamiliar'
        db_table= 'grupoFamiliar'

class domicilio(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=100)
    referencia=models.CharField(max_length=50) 
    telefono=models.CharField(max_length=15)
    resideDesde=models.CharField(max_length=50)
    condVivienda=models.CharField(max_length=50)
    lugarTrabajo=models.CharField(max_length=100)
    actividadMicro=models.CharField(max_length=50, null=True)# para micro
    jefeInm=models.CharField(max_length=50, null=True)#para natural
    tiempEmptiempFun=models.CharField(max_length=50)
    salarioIngreso=models.FloatField()
    direccionTrabMicro=models.CharField(max_length=100)
    telefonoTrabMicro=models.CharField(max_length=15)
    tipo= models.CharField(max_length=15)
    estado=models.IntegerField()
    estadosoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='domicilio'
        verbose_name_plural='domicilio'
        db_table= 'domicilio'

class datosObra(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    destino=models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    dueno=models.CharField(max_length=50)
    parentesco=models.CharField(max_length=50)
    direExacta=models.CharField(max_length=100)
    detalle=models.ForeignKey(ModeloVivienda, on_delete=models.CASCADE)
    detalleadic=models.CharField(max_length=50, null=True)
    presupuesto=models.FloatField(max_length=15)
    estado=models.IntegerField()
    estadosoli=models.IntegerField(null=True)
    class Meta:
        verbose_name='datosObra'
        verbose_name_plural='datosObra'
        db_table= 'datosObra'

class detalle(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    monto=models.FloatField()
    plazo=models.CharField(max_length=50)
    cuota=models.FloatField()
    formaPago=models.CharField(max_length=15)
    fechaPago=models.CharField(max_length=30)
    estado=models.IntegerField()
    estadosoli=models.IntegerField(null=True)
    class Meta:
        verbose_name='detalle'
        verbose_name_plural='detalle'
        db_table= 'detalle'

class experienciCrediticia(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    lugar=models.CharField(max_length=30,null=True)
    monto=models.FloatField(null=True)
    fechaOtorgamiento=models.DateField(null=True)
    estado=models.CharField(max_length=12,null=True)
    cuota=models.FloatField(null=True)
    posee=models.BooleanField()
    estadoE=models.IntegerField()
    estadosoli=models.IntegerField(null=True)
    class Meta:
        verbose_name='experienciCrediticia'
        verbose_name_plural='experienciCrediticia'
        db_table= 'experienciCrediticia'

class referencias(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    parentesco=models.CharField(max_length=15)
    domicilio=models.CharField(max_length=100)
    telefono=models.CharField(max_length=12)
    estado=models.IntegerField(null=True)
    estadosoli=models.IntegerField(null=True)
    class Meta:
        verbose_name='referencias'
        verbose_name_plural='referencias'
        db_table= 'referencias'

class comentarios(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    CSN=models.CharField(max_length=200)
    CEE=models.CharField(max_length=200)
    CGO=models.CharField(max_length=200)
    estado=models.IntegerField()
    estadosoli=models.IntegerField(null=True)
    class Meta:
        verbose_name='comentarios'
        verbose_name_plural='comentarios'
        db_table= 'comentarios'

class Medio(models.Model):
    id= models.AutoField(primary_key=True)
    idSolicitud=models.ForeignKey(solicitud, on_delete=models.CASCADE)
    redes=models.CharField(max_length=25)
    pvv=models.CharField(max_length=25)
    referenciado=models.CharField(max_length=25)
    perifoneo=models.CharField(max_length=25)
    radio=models.CharField(max_length=25)
    feriav=models.CharField(max_length=25)
    campanap=models.CharField(max_length=25)
    otros=models.CharField(max_length=25)
    especifique=models.CharField(max_length=80)
    estado=models.IntegerField()
    estadosoli=models.IntegerField(null=True)
    
    class Meta:
        verbose_name='medio'
        verbose_name_plural='medio'
        db_table= 'medio'


import json
from django.shortcuts import render, HttpResponse

# Create your views here.
from email import message
from pyexpat import model
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q


from ConfiguracionApp.models import *
from DireccionApp.models import *
from DeclaracionJurClienteApp.models import *
from DireccionApp.models import *
from InspeccionLoteApp.models import *
from InspeccionMejViviendaApp.models import *
from SolicitudInscripcionSApp.models import *
from PresupuestoApp.models import *
from PresupuestoVApp.models import *
from TesisApp.views import registroBit
from TesisApp.models import *

from django.utils import timezone # para fecha


########################
#  salario
def salario(request):
    return render(request,"ConfiguracionApp/salario.html")


def registrarSalario(request):
    tiposalario = request.POST['tiposalario']
    salariomaximo = request.POST['salariomaximo']
    salariominimo = request.POST['salariominimo']
    fechai = request.POST['fechaI']

    esta = "activo"

    # Verificar si ya existe un salario con el mismo tipo de salario
    vsalario = Salario.objects.filter(tiposalario=tiposalario, estado=esta).exists()

    if vsalario:
        mensaje = "El tipo de salario ya está registrado"
        messages.warning(request, mensaje)
    else:
        # Verificar si el rango de salario se superpone con otro rango existente
        superpuesto = Salario.objects.filter(
            Q(estado=esta),
            Q(salariominimo__lte=salariomaximo, salariomaximo__gte=salariominimo) |
            Q(salariominimo__gte=salariominimo, salariomaximo__lte=salariomaximo) |
            Q(salariominimo__lte=salariomaximo, salariomaximo__gte=salariominimo)
        ).exists()

        if superpuesto:
            mensaje = "El rango de salario pertenece a otro rango existente"
            messages.warning(request, mensaje)
        else:
            salario=Salario.objects.create(tiposalario=tiposalario,salariomaximo=salariomaximo, salariominimo=salariominimo,fechai=fechai, estado=esta) 
            
    mensaje="Salario registrado"
    registroBit(request, actividad=mensaje+" "+ tiposalario, nivel="Registro")
    messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/salario')


def listaSalario(request):
    listas=Salario.objects.all()
    return render(request, "ConfiguracionApp/listasalario.html", {"salarios":listas})

def salarioB(request, id):

    fecha_actual = timezone.now().date()
    print(fecha_actual)
   
    estad="inactivo"
    # cambia el estado del salario a inactivo
    idsal= Salario.objects.get(id=id,estado="activo")
    salv= Salario.objects.get(id= idsal.id)
    salv.fechaf = fecha_actual
    salv.estado =estad
    salv.save()

    mensaje="El Salario a sido dado de baja"
    registroBit(request, actividad=mensaje + " "+ salario.tiposalario, nivel="Desactivacion")
    messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaSalario')

def editarSalario(request, id):
    salario = Salario.objects.get(id=id)    
    
    return render(request, "ConfiguracionApp/editarSalario.html", {"s":salario})

def modificarSalario(request):
    id = request.POST['ids']
    tiposalario = request.POST['tiposalario']
    salariomaximo = request.POST['salariomaximo']
    salariominimo = request.POST['salariominimo']

    esta = "activo"

    # Obtener el salario actual
    salario_actual = Salario.objects.get(id=id)

    # Verificar si el tipo de salario se repite, excluyendo el salario actual
    vsalario = Salario.objects.filter(tiposalario=tiposalario, estado=esta).exclude(id=id).exists()

    # Verificar si el rango a modificar se superpone con otro rango existente
    superpuesto = Salario.objects.filter(
        Q(estado=esta),
        ~Q(id=id),  # Excluye el salario actual
        Q(salariominimo__lte=salariominimo, salariomaximo__gte=salariomaximo) |
        Q(salariominimo__gte=salariominimo, salariomaximo__lte=salariomaximo) |
        Q(salariominimo__lte=salariomaximo, salariomaximo__gte=salariominimo)
    ).exists()

    if vsalario or superpuesto:
        mensaje = "Ese rango de Salario ya existe o pertenece a otro rango"
        messages.warning(request, mensaje)
    else:
        # Actualizar el salario si no hay superposición ni duplicados
        salario_actual.tiposalario = tiposalario
        salario_actual.salariomaximo = salariomaximo
        salario_actual.salariominimo = salariominimo
        salario_actual.save()
        mensaje = "Salario actualizado"
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaSalario')

################################
 # Ocupacion

def ocupacion(request):
    return render(request,"ConfiguracionApp/ocupacion.html")

def registrarOcupacion(request):
    esta="activo"  
    ocupacion=request.POST['ocupacion'].upper() 
   
    oc=Ocupacion.objects.filter(ocupacion=ocupacion,estado=esta).exists()
    
    if oc == True:
            mensaje="la ocupación ya existe"
            messages.success(request, mensaje)
    else:
        ocupacio=Ocupacion.objects.create(ocupacion=ocupacion,estado=esta)
        mensaje="Ocupacion registrada"
        registroBit(request, actividad=mensaje + " "+ ocupacion, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/ocupacion/')

def listaOcupacion(request):
    listao=Ocupacion.objects.all()
    return render(request, "ConfiguracionApp/listaocupacion.html", {"ocupaciones":listao})

def eliminarO(request, id):
    estad="inactivo" 
    p=Perfil.objects.filter(idocu=id).exists()
    ocupacion= Ocupacion.objects.get(id=id)
    if p == True and ocupacion.estado=="activo":
        ocupacion.estado =estad
        ocupacion.save()
        mensaje="La ocupación fue dada de baja"
        registroBit(request, actividad=mensaje + " " + ocupacion.ocupacion, nivel="Desactivar")
        messages.success(request, mensaje)
    else:             
        ocupacion.delete()
        mensaje="Ocupacion eliminada"
        registroBit(request, actividad=mensaje, nivel="Eliminacion")
        messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaOcupacion')

def editarOcupacion(request, id):
    linfo=Ocupacion.objects.get(id=id)  
    return render(request,"ConfiguracionApp/editarOcupacion.html", {"o":linfo})

def ModificarOcupacion(request):
    ido=request.POST['ido']
    ocupacion=request.POST['ocupacion'].upper() 
   
    oc=Ocupacion.objects.filter(ocupacion=ocupacion).exists()
    
    if oc == True:
            mensaje="La ocupación ya existe"
            messages.success(request, mensaje)
    else:
        moc=Ocupacion.objects.get(id=ido)
        moc.ocupacion=ocupacion
        moc.save()
        mensaje="Datos actualizados "
        registroBit(request, actividad=mensaje +" "+ ocupacion, nivel="Actualizacion")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaOcupacion/')

######################################################
# asignar agencia # 

def zonaAgencia(request):
    listaragencia=Agencia.objects.filter(estado=1)
    return render(request,"ConfiguracionApp/zonaAgencia.html",{ "Agencia":listaragencia})

def registrarZona(request):
    nombrezona=request.POST['nombrezona']
    agencia=request.POST['agencia']
    estado=2
    age=Agencia.objects.get(id=agencia)
    age.id=agencia
    age.estado=estado
    age.save()
    consulta=ZonaAgencia.objects.filter(nombrezona=nombrezona).exists()
    
    if consulta==True:
        mensaje="El nombrezona ya existe"
        messages.warning(request, mensaje)
        return redirect('zonaAgencia')
    else:
        ocupa= ZonaAgencia.objects.create(nombrezona=nombrezona,agencia=age)
        mensaje="Se ha guardado la zona"
        registroBit(request, actividad=mensaje +" " + nombrezona, nivel="Registro")
        messages.success(request, mensaje)
        return redirect('zonaAgencia')
    
def mu(request):
    id=request.GET['departamento']
    depto=Departamento.objects.get(id=id)
    
    muni=Muni.objects.filter(depto=depto, estado=1)
    return render(request,"ConfiguracionApp/mu.html", {"muni":muni})

def dist(request):    
    idmuni=request.GET['municipio']
    
    idmuni=Muni.objects.get(idmuni=idmuni)
    destri=Distrito.objects.filter(muni=idmuni, estado=1)
    
    return render(request,"ConfiguracionApp/dis.html", {"Distrito":destri})
  
## espacio para agragar municipios para cada zona y agencia
def asignarZona(request):
     listarzona=ZonaAgencia.objects.all()
     muni=Zona.objects.all()
     listarmuni=Departamento.objects.all()
     #listarmuni=Muni.objects.filter(estado=1)
     listamuni=Muni.objects.all()
     ran_json = json.dumps(list(listamuni.values()))  # Convertir la lista a JSON

     return render(request,"ConfiguracionApp/asignarZona.html", {"ZonaAgencia":listarzona, "Departamento":listarmuni, "ran_json": ran_json,})
    
 
def registrarZona1(request): 
    idzona=request.POST['zona']
    iddistrito=request.POST['distrito']
    estado=2
    zona=ZonaAgencia.objects.get( idzona_agencia=idzona)
    zona.idzona_agencia=idzona
    distrito=Distrito.objects.get( id=iddistrito)
    distrito.id=iddistrito  
    distrito.estado=estado
    distrito.save()
    zon= Zona.objects.create(zona=zona,distri=distrito)
    mensaje="Se ha asignado la zona"
    registroBit(request, actividad=mensaje, nivel="Registro")
    messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/asignarZona')

#######################################################
# agencia#

# vista del formulario para registrar agencia
def registroAgencias(request):
    dire = Agencia.objects.only('municipio','direccion','telefono','telefono2')
    try:
        listarDepto=Departamento.objects.all()
    except Departamento.DoesNotExist:
        listarDepto=""  
    return render(request,"ConfiguracionApp/registroAgencia.html",{"dire":dire,"Departamento":listarDepto})

def municipio(request):
    id=request.GET['departamento']
    depto=Departamento.objects.get(nombre_depto=id)
    
    muni=Muni.objects.filter(depto=depto.id, estado=1)
    return render(request,"ConfiguracionApp/municipio.html", {"Muni":muni})

def distri(request):   
    idmuni=request.GET['municipio']
    idmuni=Muni.objects.get(idmuni=idmuni)
    destri=Distrito.objects.filter(muni=idmuni, estado=1)
    
    return render(request,"ConfiguracionApp/distrito.html", {"MuniDistrito":destri})


def listarAgencias(request):
    
    return render(request,"ConfiguracionApp/listaAgencias.html")

def registrarAgencia(request):
    
    nombre=request.POST['nombre'].upper() 
    direccion=request.POST['direccion']
    telefono=request.POST['telefono']
    telefonodos=request.POST['telefonodos']
    departamento=request.POST['departamento']
    municipio=request.POST['municipio']
    distrito=request.POST['distrito']
    estado=1
    mun=Muni.objects.get(idmuni=municipio)
    
    agencia = Agencia.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, 
    telefono2=telefonodos, departamento=departamento, municipio=mun.nombre_muni, distrito=distrito, estado=estado)
    mensaje="Agencia registrada"
    registroBit(request, actividad=mensaje, nivel="Registro")
    messages.success(request, mensaje)
    
    return redirect('listarAgencias')

def listaAgencias(request):
    listAgencias=Agencia.objects.exclude(direccion='Central')
    return render(request, "ConfiguracionApp/listaAgencias.html", {"agencias":listAgencias})

def editarAgencia(request, idAgencia):
    agencia = Agencia.objects.get(id=idAgencia)
    dire = Agencia.objects.only('municipio','direccion','telefono','telefono2')
    try:
        listarDepto=Departamento.objects.all()
    except Departamento.DoesNotExist:
        listarDepto=""  

    return render(request, "ConfiguracionApp/editarAgencia.html", {"agencia":agencia,"dire":dire,"Departamento":listarDepto})

def modificarAgencia(request):
    depas=("Ahuachapán","Cabañas","Chalatenango","Cuscatlán","La Libertad","La Paz","La Unión","Morazán","San Miguel","San Salvador","San Vicente","Santa Ana","Sonsonate","Usulután")
    idAg=request.POST['idAg']
    nombre=request.POST['nombre']
    direccion=request.POST['direccion']
    telefono=request.POST['telefono']
    telefonodos=request.POST['telefonodos']
    departamento=request.POST['departamento']
    municipio=request.POST['municipioe']    

    agencia = Agencia.objects.get(id=idAg)
    agencia.nombre=nombre
    agencia.direccion=direccion
    agencia.telefono=telefono
    agencia.telefono2=telefonodos
    agencia.departamento=departamento
    agencia.municipio=municipio
    agencia.save()
    mensaje="Datos de agencia actualizados"
    registroBit(request, actividad=mensaje, nivel="Actualizacion")
    messages.success(request, mensaje)
    return redirect('listarAgencias')


def con(request):
    dire = Agencia.objects.only('municipio','direccion')
    return render(request,"ConfiguracionApp/consulta.html",{"dire":dire})

##################################################################
#####Documentos

def Documento(request):
    return render(request,"ConfiguracionApp/documento.html")


def registrarD(request):
     nombreD=request.POST['nombreD']
     estado=1
     consulta=TipoDocumento.objects.filter(nombreD=nombreD).exists()
     if consulta==True :
        mensaje="El Doumento ya existe"
        messages.warning(request, mensaje)
        return redirect('/DireccionApp/listarDepto')
     else:
        depto= TipoDocumento.objects.create(nombreD=nombreD,estado=estado)
        mensaje="se ha guardado el nombre del Documento", depto
        messages.success(request, mensaje)
        return redirect('Documento')
     
##################################################################

##################################################################
# paara registrar enfermedades
def enfermedad(request):
    return render(request,"ConfiguracionApp/registrarEnfermedadesSIS.html")

def registrarEnfermedad(request):
    
    enfermedad=request.POST['enfermedadop'].upper() 
    estadoenf="activo"
    estadop="No"
   
    enf=SolicitudisEnfermedad.objects.filter(nombreenf=enfermedad).exists()
    
    if enf == True:
            mensaje="la enfermedad o padecimiento ya existe"
            messages.warning(request, mensaje)
    else:
        enfermedades=SolicitudisEnfermedad.objects.create(nombreenf=enfermedad,estado=estadoenf,personal=estadop)
        mensaje="Enfermedad registrada"
        registroBit(request, actividad=mensaje, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/enfermedad/')

def listaEnfermedades(request):
    listae=SolicitudisEnfermedad.objects.all()
    return render(request, "ConfiguracionApp/listaEnfermedades.html", {"enfermedades":listae})

def eliminarE(request, id):
    estad="inactivo" 
    sp=SolicitudisPadecimiento.objects.filter(idsisenf=id).exists()
    solEnf= SolicitudisEnfermedad.objects.get(id=id)
    if sp == True and solEnf.estado=="activo":
        solEnf.estado =estad
        solEnf.save()
        mensaje="La Enfermedad fue dada de baja"
        registroBit(request, actividad=mensaje, nivel="Desactivacion")
        messages.success(request, mensaje)
    else:             
        solEnf.delete()
        mensaje="Enfermedad eliminada"
        messages.success(request, mensaje)
        registroBit(request, actividad=mensaje, nivel="Eliminacion")
    return redirect('/ConfiguracionApp/listaEnfermedades')

def editarEnf(request, id):
    enf=SolicitudisEnfermedad.objects.get(id=id)  
    return render(request,"ConfiguracionApp/editarEnfermedadesSIS.html", {"enfermedad":enf})

def ModificarE(request):   
    ide=request.POST['ide']
    enfermedad=request.POST['enfermedadop'].upper() 
 
    menf=SolicitudisEnfermedad.objects.get(id=ide)
    menf.nombreenf=enfermedad
    menf.save()
    mensaje="Registro de enfermedad actualizados"
    registroBit(request, actividad=mensaje + enfermedad, nivel="Actualizacion")
    messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaEnfermedades/')
###################################################################
###################################################################
# Materiales

def materiales(request):
    return render(request,"ConfiguracionApp/materiales.html")

def registrarMaterial(request):
    nombre=request.POST['nombremt']
    descripcion=request.POST['descripcionmt']
    unidad=request.POST['unidadmt']

    estadomt="activo"
    mat=Materiales.objects.filter(nombre=nombre,descripcion=descripcion).exists()
    
    if mat == True:
            mensaje="El material ya existe"
            messages.success(request, mensaje)
    else:
        material=Materiales.objects.create(nombre=nombre,descripcion=descripcion,unidad=unidad,estado=estadomt)
        mensaje="Material registrado"
        registroBit(request, actividad=mensaje + material.nombre, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/materiales/')

def listaMateriales(request):
    listam=Materiales.objects.all()
    return render(request, "ConfiguracionApp/listaMateriales.html", {"materiales":listam})

def eliminarM(request, id):
    estad="inactivo" 
    pre =PresupuestoMateriales.objects.filter(idm=id).exists()
    prev =PresupuestovMateriales.objects.filter(idm=id).exists()
    mater= Materiales.objects.get(id=id)
    nomb=mater.nombre
    if pre == True or prev == True and mater.estado=="activo":
        mater.estado =estad
        mater.save()
        mensaje="El material fue dado de baja"
        registroBit(request, actividad=mensaje +nomb, nivel="Desactivacion")
        messages.success(request, mensaje)
    else:             
        mater.delete()
        mensaje="Material eliminado"
        registroBit(request, actividad=mensaje + nomb, nivel="Eliminacion")
        messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaMateriales')

def editarMat(request, id):
    lmat=Materiales.objects.get(id=id)  
    return render(request,"ConfiguracionApp/editarMateriales.html", {"material":lmat})

def ModificarMat(request):   
    idm=request.POST['idm']
    nombre=request.POST['nombremt']
    descripcion=request.POST['descripcionmt']
    unidad=request.POST['unidadmt']
    estadomt="activo"

    mat=Materiales.objects.filter(nombre=nombre,descripcion=descripcion).exists()
    
    if mat == True:
            mensaje="El material ya existe"
            messages.success(request, mensaje)
    else:
        mmat=Materiales.objects.get(id=idm)
        mmat.nombre=nombre
        mmat.descripcion=descripcion
        mmat.unidad=unidad
        mmat.estado=estadomt
        mmat.save()
        mensaje="Datos Actualizados"
        registroBit(request, actividad=mensaje + mmat.nombre, nivel="Actualizacion")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaMateriales/')


###################################################################
# Infraestructura Lote

def infraestructura(request):
    return render(request,"ConfiguracionApp/infraestructura.html")

def registrarInfraestructura(request):  
    nombre=request.POST['nombreif']
    tipo=request.POST['tipoif']
    estadoif="activo"
   
    inf=Infraestructura.objects.filter(nombre=nombre,tipo=tipo,tipolm="Lote").exists()
    
    if inf == True:
            mensaje="La infraestructura ya existe"
            messages.success(request, mensaje)
    else:
        infraestructura=Infraestructura.objects.create(nombre=nombre,tipo=tipo,tipolm="Lote",estado=estadoif)
        mensaje="Infraestructura registrada"
        registroBit(request, actividad=mensaje, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/infraestructura/')

def listaInfraestructura(request):
    listaif=Infraestructura.objects.filter(tipolm="Lote",estado="activo")
    return render(request, "ConfiguracionApp/listaInfraestructura.html", {"infraestructura":listaif})

def eliminarInf(request, id):
    estad="inactivo" 
    inp =Inspeccionlcisr.objects.filter(idif=id).exists()
    inf= Infraestructura.objects.get(id=id)
    if inp == True and inf.estado=="activo":
        inf.estado =estad
        inf.save()
        mensaje="La Infraestructura fue dada de baja"
        messages.success(request, mensaje)
    else:             
        inf.delete()
        mensaje="Infraestructura eliminada"
        messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaInfraestructura')

def editarInf(request, id):
    linf=Infraestructura.objects.get(id=id)  
    return render(request,"ConfiguracionApp/editarInfraestructura.html", {"inf":linf})


def ModificarInf(request):  
    idif=request.POST['idif']
    nombre=request.POST['nombreif']
    tipo=request.POST['tipoif']

    inf=Infraestructura.objects.filter(nombre=nombre,tipo=tipo,tipolm="Lote").exists()
    
    if inf == True:
            mensaje="La infraestructura ya existe"
            messages.success(request, mensaje)
    else:  
        minf=Infraestructura.objects.get(id=idif)
        minf.nombre=nombre
        minf.tipo=tipo
        minf.tipolm="Lote"
        minf.save()
        mensaje="Datos Actualizados"
        registroBit(request, actividad=mensaje, nivel="Actualizacion")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaInfraestructura/')


###################################################################
# Infraestructura Mejora

def infraestructuram(request):
    return render(request,"ConfiguracionApp/infraestructuraMej.html")

def registrarInfraestructuram(request):
    
    nombre=request.POST['nombreifm']
    tipo=request.POST['tipoifm']
    estadoifm="activo"
   
    inf=Infraestructura.objects.filter(nombre=nombre,tipo=tipo,tipolm="Mejora").exists()
    
    if inf == True:
            mensaje="La infraestructura ya existe"
            messages.success(request, mensaje)
    else:
        infraestructura=Infraestructura.objects.create(nombre=nombre,tipo=tipo,tipolm="Mejora",estado=estadoifm)
        mensaje="Infraestructura registrada"
        registroBit(request, actividad=mensaje, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/infraestructuram/')

def listaInfraestructuram(request):
    listaif=Infraestructura.objects.filter(tipolm="Mejora",estado="activo")
    return render(request, "ConfiguracionApp/listaInfraestructuram.html", {"infraestructura":listaif})

def eliminarInfm(request, id):
    estad="inactivo" 
    inpm =Inspeccionesirm.objects.filter(idif=id).exists()
    inf= Infraestructura.objects.get(id=id)
    if inpm == True and inf.estado=="activo":
        inf.estado =estad
        inf.save()
        mensaje="La Infraestructura fue dada de baja"
        messages.success(request, mensaje)
    else:             
        inf.delete()
        mensaje="Infraestructura eliminada"
        messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaInfraestructuram')

def editarInfm(request, id):
    linf=Infraestructura.objects.get(id=id)  
    return render(request,"ConfiguracionApp/editarInfraestructuram.html", {"infm":linf})


def ModificarInfm(request):  
    idif=request.POST['idifm']
    nombre=request.POST['nombreifm']
    tipo=request.POST['tipoifm']
    
    inf=Infraestructura.objects.filter(nombre=nombre,tipo=tipo,tipolm="Mejora").exists()
    
    if inf == True:
            mensaje="La infraestructura ya existe"
            messages.success(request, mensaje)
    else:
        minf=Infraestructura.objects.get(id=idif)
        minf.nombre=nombre
        minf.tipo=tipo
        minf.tipolm="Mejora"
        minf.save()
        mensaje="Datos Actualizados"
        registroBit(request, actividad=mensaje, nivel="Actualizacion")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaInfraestructuram/')

###################################################################
# Tipo de Operacion

def toperacion(request):
       return render(request,"ConfiguracionApp/tipooperacion.html")

def registrarTOperacion(request):
    
    tipooperacion=request.POST['toperacion'].upper()     
   
    tip=TipoOperacion.objects.filter(nombre=tipooperacion).exists()
    
    if tip == True:
            mensaje="El Tipo de Operación ya existe"
            messages.success(request, mensaje)
    else:
        tipoOperacion=TipoOperacion.objects.create(nombre=tipooperacion,estado="activo")
        mensaje="Tipo de operación registrada"
        registroBit(request, actividad=mensaje, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/toperacion/')

def listaToperaciones(request):
    listato=TipoOperacion.objects.all()
    return render(request, "ConfiguracionApp/listaToperaciones.html", {"toperaciones":listato})

def eliminarTO(request, id):
    estad="inactivo" 
    d=Declaracionjc.objects.filter(toperacion=id).exists()
    top= TipoOperacion.objects.get(id=id)
    if d == True and top.estado=="activo":
        top.estado =estad
        top.save()
        mensaje="El Tipo de Operacion fue dada de baja"
        messages.success(request, mensaje)
    else:             
        top.delete()
        mensaje="Tipo Operación eliminado"
        messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaToperaciones')

def editarTO(request, id):
       linfto=TipoOperacion.objects.get(id=id) 
       return render(request,"ConfiguracionApp/editarTipooperacion.html", {"to":linfto})

def ModificarTO(request): 
    idto=request.POST['idt']
    tipooperacion=request.POST['toperacion'].upper()     
   
    tip=TipoOperacion.objects.filter(nombre=tipooperacion).exists()
    
    if tip == True:
        mensaje="El Tipo de Operación ya existe"
        messages.success(request, mensaje)
    else:
        mto=TipoOperacion.objects.get(id=idto)
        mto.nombre=tipooperacion
        mto.save()
        mensaje="Datos Actualizados"
        registroBit(request, actividad=mensaje, nivel="Actualizacion")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaToperaciones/')

##########################   tasa
def tasa(request):
    return render(request, "ConfiguracionApp/tasa.html")
def registrartasa(request):
    numerocredito=request.POST['numerocredito'].upper()
    interes=request.POST['interes']
    estado=1
    tasa= TasaInteres.objects.create(numerocredito=numerocredito, interes=interes,estado=estado)
    mensaje="Se ha guardado los datos"
    registroBit(request, actividad=mensaje, nivel="Registro")
    messages.success(request, mensaje)
    return render(request, "ConfiguracionApp/tasa.html")

def listarTasa(request):
    tasa=TasaInteres.objects.all()
    return render(request, "ConfiguracionApp/listartasa.html",{"TasaInteres":tasa})

def alternativa(request):
    tasa=TasaInteres.objects.all()
    return render(request, "ConfiguracionApp/alternativas.html",{"TasaInteres":tasa})

def registraral(request):
    alternativa=request.POST['alternativa'].upper()
    montominimo=request.POST['montominimo']
    montomaximo=request.POST['montomaximo']
    plazo=request.POST['plazo']
    pla=int(plazo)
    plazomese=pla*12
    id=request.POST['interes']
    interes=TasaInteres.objects.get(id=id)
    interes.id=id
    estado=1

    consulta=Alternativa.objects.filter(alternativa=alternativa,interes=interes).exists()

    
    if consulta==True :
        mensaje="El nombre de la linea de financiamiento ya existe"
        messages.warning(request, mensaje)
        return redirect('/ConfiguracionApp/listarAl')
    else:
        tasa= Alternativa.objects.create(alternativa=alternativa,montominimo=montominimo,montomaximo=montomaximo,
                                    plazo=plazo,plazomese=plazomese,interes=interes,estado=estado)
        mensaje="Se ha registro la alternativa "
        registroBit(request, actividad=mensaje + alternativa, nivel="Registro")
        messages.success(request, mensaje)
    return redirect('alternativa')
    

def listarAl(request):
    tasa=Alternativa.objects.all()
    return render(request, "ConfiguracionApp/listarAl.html",{"Alternativa":tasa})

###########################
def rangoFinanciamiento(request):
    salario=Salario.objects.filter(estado="activo")
    alter=Alternativa.objects.all()
    ran_alter = json.dumps(list(alter.values()))
    ran_data = list(salario.values())
     # Serializa el campo Decimal usando la función personalizada y el DjangoJSONEncoder
    for item in ran_data:
        if 'salariominimo' in item:
            item['salariominimo'] = float(item['salariominimo'])
        if 'salariomaximo' in item:
            item['salariomaximo'] = float(item['salariomaximo'])
        if 'fechai' in item and item['fechai'] is not None:
            item['fechai'] = item['fechai'].strftime('%Y-%m-%d')
        if 'fechaf' in item and item['fechaf'] is not None:
            item['fechaf'] = item['fechaf'].strftime('%Y-%m-%d')
    ran_json = json.dumps(ran_data)# Convertir la lista a JSON
         
    return render(request, "ConfiguracionApp/rangoFinan.html",{"salario":salario, "alternativa":alter, "sal":ran_json, "alter":ran_alter})

def registrarRanFin(request):

    idalter=request.POST['alternativas'] # id alternativa
    idsal=request.POST['salario'] # id salario
    montominimo=request.POST['montominimo']
    montomaximo=request.POST['montomaximo']
    vecesfinan=float(request.POST['vecesFin'])
    
    alter=Alternativa.objects.get(id=idalter)
    alter.id=idalter

    salar=Salario.objects.get(id=idsal)
    salar.id=idsal

    rangoFinan=RangoFinan.objects.create(vecesfinan=vecesfinan,montominimo=montominimo,montomaximo=montomaximo,idalter=alter,idsal=salar)

    mensaje="Se ha registrado rango de financiamiento "
    registroBit(request, actividad=mensaje + str(rangoFinan.montominimo) +" - " + str(rangoFinan.montomaximo), nivel="Registro")
    messages.success(request, mensaje)
    return redirect("../rangoFinanciamiento")#rangoFinan
#Lista de rangos de financiamiento

def listarRanFin(request):
    lisRanF=RangoFinan.objects.all()
    lisAlt=Alternativa.objects.all()
    listarmuni=Departamento.objects.all()
    return render(request,"ConfiguracionApp/listarRanFin.html", {"LisFinan":lisRanF, "alternativa":lisAlt})

def lisAltRan(request):
    id=request.GET['id']
    lista_rangos=[]
    rangos=""
    if request.is_ajax():
        try:
            rangos=RangoFinan.objects.filter(idalter=id)
            for item in rangos:
                lista_rangos.append({"id":item.id, "salario":item.idsal.tiposalario, "minimo":item.montominimo, "maximo":item.montomaximo, "vecesF":item.vecesfinan})
        except Exception:
            None
        print("pasoo"+str(rangos))
        serialized_data = json.dumps(lista_rangos,default=str)
        #serialized_data = serialize("safe",[lista_muni])
        return HttpResponse(serialized_data, content_type="application/json")



def modRanFin(request, id):
    rango= RangoFinan.objects.get(id=id)
    alter= Alternativa.objects.all()
    sala= Salario.objects.filter(estado="activo")
    ran_alter = json.dumps(list(alter.values()))
    ran_data = list(sala.values())
     # Serializa el campo Decimal usando la función personalizada y el DjangoJSONEncoder
    for item in ran_data:
        if 'salariominimo' in item:
            item['salariominimo'] = float(item['salariominimo'])
        if 'salariomaximo' in item:
            item['salariomaximo'] = float(item['salariomaximo'])
        if 'fechai' in item and item['fechai'] is not None:
            item['fechai'] = item['fechai'].strftime('%Y-%m-%d')
        if 'fechaf' in item and item['fechaf'] is not None:
            item['fechaf'] = item['fechaf'].strftime('%Y-%m-%d')
    ran_json = json.dumps(ran_data)# Convertir la lista a JSON
    return render (request, "ConfiguracionApp/rangoFinanedit.html", {"rangosF":rango, "alternativa":alter, "salario":sala, "sal":ran_json, "alter":ran_alter})


def editRanFin(request):
    id=request.POST['id']
    idalter=request.POST['alternativas'] # id alternativa
    idsal=request.POST['salario'] # id salario
    montominimo=request.POST['montominimo']
    montomaximo=request.POST['montomaximo']
    vecesfinan=float(request.POST['vecesFin'])
    
    alter=Alternativa.objects.get(id=idalter)
    sal= Salario.objects.get(id=idsal)
    
    ranFin=RangoFinan.objects.filter(idalter=alter.id, idsal=sal.id).exists
    if ranFin == True:
            mensaje="El rango para esa alternativa y salario ya existe"
            messages.warning(request, mensaje)
    else:
            ranF = RangoFinan.objects.get(id=id)
            ranF.vecesfinan=vecesfinan
            ranF.montomaximo=montomaximo
            ranF.montominimo=montominimo
            ranF.idalter=alter
            ranF.idsal=sal
            ranF.save()
            mensaje="Rango de financiamiento actualizado"
            registroBit(request, actividad=mensaje, nivel="Actualizacion")
            messages.success(request, mensaje)
    return redirect('/ConfiguracionApp/listaRanFin')

def modiMuni(request, idmuni):
    muni = Muni.objects.get(idmuni=idmuni)
    listarde=Departamento.objects.all()
    return render(request, "DireccionApp/modiMuni.html", {"Muni":muni,"Departamento":listarde})

#######################################################
# tipos de viviendas
def tvivienda(request):
    return render(request,"ConfiguracionApp/modeloVivienda.html")

def registrarModeloV(request):
       
    topovivienda=request.POST['tipovivienda']
    modelo=request.FILES['modelov']
    montoc=request.POST['montov']
    descripcion =request.POST['descripcion']
   
    mod=ModeloVivienda.objects.filter(topovivienda=topovivienda,montoc=montoc).exists()
    
    if mod == True:
            mensaje="El modelo de vivienda ya existe"
            messages.warning(request, mensaje)
    else:
        modelovivienda=ModeloVivienda.objects.create(topovivienda=topovivienda,modelo=modelo,montoc=montoc,descripcion=descripcion)
        mensaje="Modelo de vivienda registrada "
        registroBit(request, actividad=mensaje + topovivienda, nivel="Registro")
        messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/tvivienda/')

def listarModeloV(request):
    modelosv=ModeloVivienda.objects.all()  
    return render(request,"ConfiguracionApp/listaModeloVivienda.html", {"modelos":modelosv})

def editarMV(request, id):
       mmodelosv=ModeloVivienda.objects.get(id=id) 
       return render(request,"ConfiguracionApp/editarModeloVivienda.html", {"mmv":mmodelosv})

def modificarMV(request): 
    idmv=request.POST['idmv']
    montoc=request.POST['montov']
    descripcion =request.POST['descripcion']

    dmodelov=request.POST['dmodelov']
    try:
        modelo=request.FILES['modelov']
    except :
        modelo=""

    mmod=ModeloVivienda.objects.get(id=idmv)     

    if dmodelov == "" :
        mmod.modelo=modelo

    if dmodelov != "" and modelo !="":
        mmod.modelo=modelo

    mmod.montoc=montoc
    mmod.descripcion=descripcion
    mmod.save()
   
    mensaje="Datos Actualizados"
    registroBit(request, actividad=mensaje, nivel="Actualizacion")
    messages.success(request, mensaje)

    return redirect('/ConfiguracionApp/listaModeloV/')

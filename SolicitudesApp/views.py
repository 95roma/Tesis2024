from datetime import date
import json
from django.db import IntegrityError
from django.http import FileResponse
from django.core.serializers import serialize
from django.shortcuts import render,redirect, HttpResponse
from django.http.response import JsonResponse
from django.contrib import messages
from fpdf import FPDF
from django.contrib.auth.decorators import login_required
from SolicitudesApp.models import *
from ClienteApp.models import Perfil
from TesisApp.models import Usuario
from EvaluacionMicroApp.models import *
from ConfiguracionApp.models import Alternativa
from django.db.models import Q
from ListaChequeoApp.models import *
from TesisApp.views import registroBit


# Create your views here.
def registroSolicitudMicro(request):    
    return render(request,"SolicitudesApp/solicitudMicro.html")

def registrarSolicitud(request, idCliente):
   #try:
        cliente = Perfil.objects.get(id=idCliente)
        balance = Balancesm.objects.get(estado="1", idp = idCliente )
        estado = Estadorm.objects.get(idb = balance.id)
        capacidad = Capacidadpagom.objects.get(ide=estado.id)
        alternativas = Alternativa.objects.all()
        modelos = ModeloVivienda.objects.all()
        return render(request, "SolicitudesApp/solicitudMicro.html", {
            "cliente":cliente, "balance":balance, "estado":estado, "alternativas":alternativas,"modelos":modelos, "capacidaPago":capacidad})
    #except Exception:
     #   return None


def modificarSolicitud(request, idSolicitud):
   
    try:
        solici = solicitud.objects.get(id=idSolicitud)
    except solicitud.DoesNotExist:
        solici=""

    try:
        gpf=grupoFamiliar.objects.filter(idSolicitud=idSolicitud)
    except grupoFamiliar.DoesNotExist:
        gpf=""

    try:
        dps=datosPersonales.objects.get(idSolicitud=idSolicitud)
        if(dps.fechaduiC.strftime("%Y-%m-%d") == "9999-01-01"):
            dps.fechaduiC=""           
         
    except datosPersonales.DoesNotExist:
        dps=""

    try:
        dpc=DatosPersonalesF.objects.get( Q(idSolicitud=idSolicitud) & Q(Q(tipo="codeudor") | Q(tipo="conyuge")))
        if(dpc.fechaduifia.strftime("%Y-%m-%d") == "9999-01-01"):
            dpc.fechaduifia=""
        if(dpc.fechanacifia.strftime("%Y-%m-%d") == "9999-01-01"):
            dpc.fechanacifia=""
        if(dpc.edadfia == "0"):
            dpc.edadfia  =""
    except DatosPersonalesF.DoesNotExist:
       dpc=""   
   
    try:
        mdl=domicilio.objects.get(idSolicitud=idSolicitud, tipo="Solicitante")
    except domicilio.DoesNotExist:
        mdl=""
    try:
        mdlc=domicilio.objects.get(Q(idSolicitud=idSolicitud)  & Q(Q(tipo="codeudor") | Q(tipo="conyuge")))
    except domicilio.DoesNotExist:
        mdlc=""

    try:
        dob=datosObra.objects.get(idSolicitud=idSolicitud)
    except datosObra.DoesNotExist:
        dob=""

    try:
        ds=detalle.objects.get(idSolicitud=idSolicitud)
    except detalle.DoesNotExist:
        ds=""

    try:
        ec=experienciCrediticia.objects.filter(idSolicitud=idSolicitud)
    except experienciCrediticia.DoesNotExist:
        ec=""
    try:
        rp=referencias.objects.filter(idSolicitud=idSolicitud)
    except referencias.DoesNotExist:
        rp=""

    try:
        cmt=comentarios.objects.get(idSolicitud=idSolicitud)
    except comentarios.DoesNotExist:
        cmt=""

    try: 
        med=Medio.objects.get(idSolicitud=idSolicitud)
    except Medio.DoesNotExist:
        med=""

    id_cliente = solici.perfil.id
    try:
         balance = Balancesm.objects.get(idp = id_cliente, estado=1)
         try:
             estado = Estadorm.objects.get(idb = balance.id)
         except Estadorm.DoesNotExist:
             None
    except Balancesm.DoesNotExist:
          balance = ""   
          estado =  ""
          
    
    alternativas = Alternativa.objects.all()
    modelos = ModeloVivienda.objects.all()

    soli = [solici, dps, dpc, gpf, mdl, mdlc, dob, ds, ec, rp, cmt,med]
    return render(request, "SolicitudesApp/modificarSolicitudMicro.html", {
        "soli":soli,
        "alternativas":alternativas,
        "modelos":modelos,
        "balance":balance, 
        "estado":estado
        })

def listaSC(request):
    listSoli = solicitud.objects.filter(estado="Completado", tipo="micro")
    return render(request, "SolicitudesApp/listaSCompleta.html", {"solicitudes":listSoli})


def listaSCA(request, id):
    
    #print("usuaro:"+ id)
    per=Perfil.objects.filter(Agencia=id)
    listSoli = solicitud.objects.filter(Q(estado="Completado") & Q(tipo="micro")& Q(perfil__in=per))
    
    return render(request, "SolicitudesApp/listaSCompleta.html", {"solicitudes":listSoli})

def listaSolicitud(request):    
    listSoli = solicitud.objects.filter(estado="Incompleto", tipo="micro")
    return render(request, "SolicitudesApp/listSolicitudes.html", {"solicitudes":listSoli})
    
def registroSolicitud(request):
    tipoobra=request.POST['tipoobra']
    fecha= request.POST['fechaSM']
    #agencia= Agencia.objects.get(id= request.POST['agenciaM'])
    cliente=Perfil.objects.get(id= request.POST['idCliente'])
    n= request.POST['n']
    comunidad= request.POST['comunidadM'].upper()
   # muni= request.POST['municipioM']
    area= request.POST['areaM']
    estado= request.POST['estadoM']
    estado_soli=1
    if(estado=="Completado"):
        estado_soli=2

    soli= solicitud.objects.create(tipoobra=tipoobra,fecha=fecha, numero=n, comunidad=comunidad, area=area, tipo="micro", estado=estado,perfil=cliente, estadosoli=estado_soli )
    
    cliente.estadosoli=4
    cliente.save()


    idSoli= solicitud.objects.get(fecha=fecha,tipo="micro",perfil=cliente)
   
   # soli.perfil.add(cliente)        para guardar en la tabla solicitud_perfil

    #idSoli= solicitud.objects.all().last() #obtengo la ultima solicitud registrada   
       #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.create(fecha=fecha,solicitudc="Si",estado="incompleto",ids=idSoli)


    bandera= request.POST['passDPM']  # guarda datos personales
    if(bandera == '1'):        
        
        lugarExp=request.POST['lugExS']        
        fechaExp=request.POST['fechExS']        
        lugarNac=request.POST['lugNaS']
        fechaNac=request.POST['fechNaS']
        edad= request.POST['edadS']
        aestadoCivil=request.POST['estadoCivilS']
        Genero= request.POST['generoS']
        Profecion= request.POST['profecionS']
        estadoC=1
        if(fechaExp==""):
            fechaExp="9999-01-01"
        
        datos = datosPersonales.objects.create(lugarduiC=lugarExp, fechaduiC=fechaExp, lugarnaciC=lugarNac,estadocivilC=aestadoCivil,
        generoC=Genero , profesion= Profecion,estadoC=estadoC,idSolicitud=idSoli )
        
   
    bandera= request.POST['passDPMC']  # guarda datos personales
    if(bandera == '1'):   
        sinFE=0                 #sin fecha de expiracion
        sinFN=0                 #sin fecha de nacimiento
        tipo=request.POST['tipoSM']
        nombre= request.POST['nombreC']     #para el conyuge o codeudor
        apellido= request.POST['apellidoC']
        dui= request.POST['duiC']
        lugarExp=request.POST['lugExC']
        fechaExp=request.POST['fechExC']
        if(fechaExp==""):
            fechaExp="9999-01-01"
            
        lugarNac=request.POST['lugNaC']
        fechaNac=request.POST['fechNaC']
        if(fechaNac==""):  
            fechaNac="9999-01-01"
            
        edad= request.POST['edadC']
        if(edad==""):
            edad="0"
        aestadoCivil=request.POST['estadoCivilC']
        Genero= request.POST['generoC']
        try:
            Profecion= request.POST['profecionC']
        except :
           Profecion= " "
       
        estadoF=1

        
        datos1 = DatosPersonalesF.objects.create(tipo=tipo, nombrefia=nombre, apellidofia=apellido, duifia=dui,lugarduifia=lugarExp,
        fechaduifia=fechaExp, fechanacifia=fechaNac,lugarnacifia=lugarNac,edadfia=edad ,estadocivilfia=aestadoCivil,
        generofia=Genero , profefia= Profecion,estadofia=estadoF, idSolicitud=idSoli )
    #fin datos personales


    bandera= request.POST['passGP'] #inicia guardar grupo familiar
    if(bandera == '1'):
       nombreGP =request.POST.getlist('nombreGP') 
       edadGP =request.POST.getlist('edadGP')
       salarioGP =request.POST.getlist('salarioGP')
       
       trabajoGP=request.POST.getlist('trabajoGP')
       parentescoGP =request.POST.getlist('parentescoGP')
       estadog=1
       
       for i in range(len(nombreGP)):
        if (nombreGP[i] != ""):
            if(salarioGP[i] ==""):
                salarioGP[i] ="0"
            grupo = grupoFamiliar.objects.create(nombre=nombreGP[i], edad=edadGP[i], salario=salarioGP[i], trabajo=trabajoGP[i],
            parentesco=parentescoGP[i],estado=estadog, idSolicitud=idSoli)

    #fin grupo familiar

    bandera= request.POST['passDLM'] #inicia guardar domicilio y lugar de microempresa
    if(bandera == '1'):
       direActS =request.POST['direActS']# guarda direccion del solicitante
       puntoRefS =request.POST['puntoRefS']
       telefonoS =request.POST['telefonoS']
       condicionS =request.POST['condicionS']       
       resideS=request.POST['resideS']
       lugrTrabS =request.POST['lugrMicroS']
       actividadMicro =request.POST['actividadS']
       tiempoS =request.POST['tiempoS']       
       salarioS =request.POST['salarioS']
       if(salarioS==""):
            salarioS='0'
       direccionMS =request.POST['direccionMS']
       telefonoMS =request.POST['telefonoMS']
       tipo="Solicitante"
       estadoSS=1
       domicilioS = domicilio.objects.create(direccion=direActS, referencia=puntoRefS,telefono=telefonoS, resideDesde=resideS, 
       condVivienda=condicionS, lugarTrabajo=lugrTrabS,  actividadMicro=actividadMicro, tiempEmptiempFun=tiempoS, salarioIngreso=salarioS, 
       direccionTrabMicro=direccionMS, telefonoTrabMicro=telefonoMS, tipo=tipo,estado=estadoSS, idSolicitud=idSoli) 
       
    bandera= request.POST['passDLMC'] #inicia guardar domicilio y lugar de microempresa
    if(bandera == '1'):
       
       direActC =request.POST['direActC']# guarda direccion del conyuge o codeudor     
       puntoRefC =request.POST['puntoRefC']
       telefonoC =request.POST['telefonoC']
       condicionC =request.POST['condicionC'] 
       resideC=request.POST['resideC']
       lugrTrabC =request.POST['lugrMicroC']
       actividadMicroC =request.POST['actividadC']
       tiempoC =request.POST['tiempoC']
       salarioC =request.POST['salarioC']
       if(salarioC==""):
            salarioC='0'
       direccionMC =request.POST['direccionMC']
       telefonoMC =request.POST['telefonoMC']
       tipo=request.POST['tipoSM']
       estadoSC=1

       domicilioS = domicilio.objects.create(direccion=direActC, referencia=puntoRefC,telefono=telefonoC, resideDesde=resideC, 
       condVivienda=condicionC, lugarTrabajo=lugrTrabC, actividadMicro=actividadMicroC, tiempEmptiempFun=tiempoC, salarioIngreso=salarioC, 
       direccionTrabMicro=direccionMC,telefonoTrabMicro=telefonoMC, tipo=tipo,estado=estadoSC, idSolicitud=idSoli)
    #fin domicilio y lugar de microempresa 

    bandera= request.POST['passDOR'] #inicia guardar datos de la obra a realizar
    if(bandera == '1'):
       destinoME =request.POST['destinoME']
       duenoME =request.POST['duenoME']
       parentescoME =request.POST['parentescoME']
       direExacta=request.POST['direccionE'] 
       detalleObra =request.POST['detalleObra'] 
       detalleadic =request.POST['detalleAD']  
       PresupuestoME =request.POST['PresupuestoME']
       if(PresupuestoME==""):
            PresupuestoME='0'
       estadoO=1
       detalleObra=Alternativa.objects.get(id=destinoME)
       modeloVivienda= ModeloVivienda.objects.get(id=detalleObra.id)
       modeloVivienda.id=detalleObra.id
       
       dor = datosObra.objects.create(destino=detalleObra, dueno= duenoME, parentesco=parentescoME,direExacta=direExacta ,
      detalle=modeloVivienda,detalleadic=detalleadic, presupuesto=PresupuestoME,estado=estadoO, idSolicitud=idSoli) 
    #fin datos de la obra a realizar


    bandera= request.POST['passDS'] #inicia guardar detalle de la solicitud
    if(bandera == '1'):
       montoME =request.POST['montoME']
       if(montoME==""):
            montoME='0'
       plazoME =request.POST['plazoME']
       cuotaME =request.POST['cuotaME']
       if(cuotaME==""):
            cuotaME='0'
       formaPagoME =request.POST['formaPagoME']   
       FechaPagoME =request.POST['FechaPagoME']
       estadoD=1
       ds = detalle.objects.create(monto=montoME, plazo= plazoME, cuota=cuotaME, 
      formaPago=formaPagoME, fechaPago= FechaPagoME,estado=estadoD, idSolicitud=idSoli) 
    #fin detalle de la solicitud

    bandera= request.POST['passEC'] #inicia experiencia crediticia
    if(bandera == '1'):
       lugarEC =request.POST.getlist('lugarEC') 
       montoEC =request.POST.getlist('montoEC')       
       fechaEC =request.POST.getlist('fechaEC')       
       estadoEC=request.POST.getlist('estadoEC')
       cuotaEC =request.POST.getlist('cuotaEC')
      # posee =request.POST['sinEC'] 
       estadoE=1
      # print(posee)
      # if(posee != True):
       for i in range(len(lugarEC)):
         if (lugarEC[i] != ""):
            if(montoEC[i]==""):
                 montoEC[i]='0'            
            if(cuotaEC[i]==""):
                cuotaEC[i]='0'
            if(fechaEC[i]==""):
                experiencia = experienciCrediticia.objects.create(lugar=lugarEC[i], monto=montoEC[i],
             estado=estadoEC[i],  cuota=cuotaEC[i], posee=0,estadoE=estadoE, idSolicitud=idSoli)
            else:
                experiencia = experienciCrediticia.objects.create(lugar=lugarEC[i], monto=montoEC[i], fechaOtorgamiento=fechaEC[i],
             estado=estadoEC[i],  cuota=cuotaEC[i], posee=0,estadoE=estadoE, idSolicitud=idSoli)

        #else:
           # print("paso")
            #experiencia = experienciCrediticia.objects.create( posee=1,estadoE=estadoE, idSolicitud=idSoli)
    #fin experiencia crediticia  


    bandera= request.POST['passRPF'] #inicia referencias personales y familiares
    if(bandera == '1'):
       nombreRPF =request.POST.getlist('nombreRPF') 
       parentescoRPF =request.POST.getlist('parentescoRPF')
       domicilioRPF =request.POST.getlist('domicilioRPF')
       telefonoRPF=request.POST.getlist('telefonoRPF')
       estadoR=1
       
       for i in range(len(nombreRPF)):
        if (nombreRPF[i] != ""):
            refere = referencias.objects.create( nombre=nombreRPF[i], parentesco=parentescoRPF[i], 
            domicilio=domicilioRPF[i], telefono=telefonoRPF[i],estado=estadoR, idSolicitud=idSoli)
    #fin referencias personales y familiares  
    
    bandera= request.POST['passCM'] #inicia guardar comentarios
    if(bandera == '1'):
       
       try:
            comIniciativa =request.POST['comIniciativa']
       except :
            comIniciativa = " "
       try:
            comEvaluacion =request.POST['comEvaluacion']
       except :
            comEvaluacion= " "
       try:
            comGarantia =request.POST['comGarantia']
       except :
            comGarantia= " "
       estadoCM=1

       c = comentarios.objects.create(CSN=comIniciativa, CEE= comEvaluacion, CGO=comGarantia,estado=estadoCM, idSolicitud=idSoli) 
    #fin comentarios

     # inicio medio por el cual se informo
    try:
        redes =request.POST['redes']
    except :
        redes= " "
    try:
        pvv =request.POST['pvv']
    except :
        pvv= " "
    try:
        referenciado =request.POST['referenciado']
    except :
        referenciado= " "
    try:
        perifoneo =request.POST['perifoneo']
    except :
        perifoneo= " "
    try:
        radio =request.POST['radio']
    except :
        radio= " "
    try:
        feriav =request.POST['feriav']
    except :
        feriav= " "
    try:
        campanap =request.POST['campaprom']
    except :
        campanap= " "
    try:
        otros =request.POST['otros']
    except :
        otros= " "
    try:
        especifique =request.POST['espeotromed']
    except :
        especifique= " "

    estadom= 1

    medio = Medio.objects.create(redes=redes,pvv=pvv,referenciado=referenciado,perifoneo=perifoneo,radio=radio,feriav=feriav,campanap=campanap,otros=otros,especifique=especifique,estado=estadom, idSolicitud=idSoli)

    # fin medio"""

    registroBit(request, "Se registro  formulario Solicitud Microempresa" + soli.perfil.dui, "Registro")
    return redirect('administrarPerfil', id=soli.perfil.id)  # id de perfil 
    

def modSoli(request):
# Inicia modifcar solicitud
#datos generales de la solicitd   ------------------------
    idSoli=request.POST['idSoli']
    tipoobra=request.POST['tipoobra']
    #fecha= request.POST['fechaSMM']
    #agencia= Agencia.objects.get(id= request.POST['agenciaMod'])
    #cliente=Perfil.objects.get(id= request.POST['idCliente'])
    n= request.POST['nMod']
    comunidad= request.POST['comunidadMod']
    #muni= request.POST['municipioMod']
    area= request.POST['areaMM']
    estado= request.POST['estadoMod']
    estado_soli=1
    if(estado=="Completado"):
        estado_soli=2
    soli = solicitud.objects.get(id=idSoli)
    soli.tipoobra = tipoobra
    soli.numero = n
    soli.comunidad = comunidad
    soli.area = area
    soli.estado = estado
    soli.estadosoli = estado_soli
    soli.save()

#Inicia modificar datos personales del solicitande -----    
    #nombre= request.POST['nombreS']
    #apellido= request.POST['apellidoS']
    #dui= request.POST['duiS']
    lugarExp=request.POST['lugExS']
    fechaExp=request.POST['fechExS']
    if(fechaExp==""):                   #valido que la fecha no este vacia sino no guarda
            fechaExp="9999-01-01"
    lugarNac=request.POST['lugNaS']
    #fechaNac=request.POST['fechNaS']
    #edad= request.POST['edadS']
    aestadoCivil=request.POST['estadoCivilS']
    Genero= request.POST['generoS']
    Profecion= request.POST['profecionS']
    #tipo="Solicitante"    
    try:
        datos = datosPersonales.objects.get(idSolicitud=idSoli)
    except:
        datos=''

    datos = datosPersonales.objects.update_or_create(idSolicitud=idSoli,
            defaults={
            'lugarduiC':lugarExp,
            'fechaduiC':fechaExp,     
            'lugarnaciC':lugarNac,
            'estadocivilC':aestadoCivil,
            'generoC':Genero  ,
            'profesion': Profecion,    
            'estadoC':'1',    
            'idSolicitud':soli })
    

#Inicia modificar para el conyuge o codeudor
    bandera= request.POST['passDPMC']  # guarda datos personales
    if(bandera == '1'):  
        id= request.POST['idC']
        tipo=request.POST['tipoSM']
        nombre= request.POST['nombreC']     
        apellido= request.POST['apellidoC']
        dui= request.POST['duiC']
        lugarExp=request.POST['lugExC']
        fechaExp=request.POST['fechExC']
        if(fechaExp==""):
                fechaExp="9999-01-01"
        lugarNac=request.POST['lugNaC']
        fechaNac=request.POST['fechNaC']
        if(fechaNac==""):  
                fechaNac="9999-01-01"
        edad= request.POST['edadC']
        if(edad==""):
                edad="0"
        aestadoCivil=request.POST['estadoCivilC']
        Genero= request.POST['generoC']
        Profecion= request.POST['profecionC']
        
        if(id==""):
            datos = DatosPersonalesF.objects.update_or_create(idSolicitud=idSoli,
            defaults={'tipo' :tipo,
            'nombrefia':nombre,
            'apellidofia':apellido,
            'duifia':dui ,
            'lugarduifia':lugarExp,
            'fechaduifia':fechaExp,
            'fechanacifia':fechaNac,        
            'lugarnacifia':lugarNac,         
            'edadfia':edad,
            'estadocivilfia':aestadoCivil,
            'generofia':Genero  ,
            'profefia': Profecion,    
            'estadofia':'1',    
            'idSolicitud':soli })
        else:
            datos = DatosPersonalesF.objects.update_or_create(id=id,
                defaults={'tipo' :tipo,
                'nombrefia':nombre,
                'apellidofia':apellido,
                'duifia':dui ,
                'lugarduifia':lugarExp,
                'fechaduifia':fechaExp,
                'fechanacifia':fechaNac,        
                'lugarnacifia':lugarNac,         
                'edadfia':edad,
                'estadocivilfia':aestadoCivil,
                'generofia':Genero  ,
                'profefia': Profecion,   
                'estadofia':'1',      
                'idSolicitud':soli })
#Inicia modificar grupo familiar
    idGP=request.POST.getlist('idGP')
    nombreGP =request.POST.getlist('nombreGP') 
    edadGP =request.POST.getlist('edadGP')
    salarioGP =request.POST.getlist('salarioGP')
    trabajoGP=request.POST.getlist('trabajoGP')
    parentescoGP =request.POST.getlist('parentescoGP')
     
    for i in range(len(nombreGP)):
     if (nombreGP[i] != ""):        
        if(salarioGP[i] ==""):
                salarioGP[i] ="0.00"
        
        if(idGP[i]!=""):
            grupo = grupoFamiliar.objects.update_or_create(idSolicitud=idSoli,id=idGP[i],
            defaults={ 'nombre':nombreGP[i], 
            'edad':edadGP[i], 
            'salario':salarioGP[i], 
            'trabajo':trabajoGP[i],
            'parentesco':parentescoGP[i], 
            'estado':"1",
            'idSolicitud':soli})
            
        else: #si registro un nuevo familiar ejecuta la orden sin enviar id de la tabla ya que no existe ese campo
            grupo1 = grupoFamiliar.objects.update_or_create(idSolicitud=idSoli, nombre=nombreGP[i], parentesco=parentescoGP[i],
            defaults={ 'nombre':nombreGP[i], 
            'edad':edadGP[i], 
            'salario':salarioGP[i], 
            'trabajo':trabajoGP[i],
            'parentesco':parentescoGP[i], 
            'estado':"1",
            'idSolicitud':soli})

#Inicia modificar direccion del solicitante
    bandera= request.POST['passDLM'] 
    if(bandera == '1'):
        direActS =request.POST['direActS']
        puntoRefS =request.POST['puntoRefS']
        telefonoS =request.POST['telefonoS']
        condicionS =request.POST['condicionS']       
        resideS=request.POST['resideS']
        lugrTrabS =request.POST['lugrMicroS']
        actividadMicro =request.POST['actividadS']
        tiempoS =request.POST['tiempoS']
        
        salarioS =request.POST['salarioS']
        if(salarioS==""):
            salarioS=0.00
        direccionMS =request.POST['direccionMS']
        telefonoMS =request.POST['telefonoMS']
        tipo="Solicitante"
        domicilioS = domicilio.objects.update_or_create(idSolicitud=soli,tipo="Solicitante",
        defaults={ 'direccion':direActS,
            'referencia':puntoRefS,
            'telefono':telefonoS, 
            'resideDesde':resideS, 
            'condVivienda':condicionS,
            'lugarTrabajo':lugrTrabS,
            'actividadMicro':actividadMicro,
            'tiempEmptiempFun':tiempoS,
            'salarioIngreso':salarioS, 
            'direccionTrabMicro':direccionMS,       
            'telefonoTrabMicro':telefonoMS,
            'estado':"1",}) 

#inicia actualizaar doicilio conyuge o codeudor
    bandera= request.POST['passDLMC'] 
    if(bandera == '1'):
        idd=request.POST['idDomicilioCC']   
        direActC =request.POST['direActC']
        puntoRefC =request.POST['puntoRefC']
        telefonoC =request.POST['telefonoC']
        condicionC =request.POST['condicionC']       
        resideC=request.POST['resideC']
        lugrTrabC =request.POST['lugrMicroC']
        actividadMicro =request.POST['actividadC']
        tiempoC =request.POST['tiempoC']
        salarioC =request.POST['salarioC']
        if(salarioC==""):
            salarioC=0
        direccionMC =request.POST['direccionMC']
        telefonoMC =request.POST['telefonoMC']
        tipo=request.POST['tipoSM']
        if(idd==""):
                domicilioC = domicilio.objects.update_or_create(idSolicitud=idSoli, tipo=tipo,
            defaults={ 'direccion':direActC,
                'referencia':puntoRefC,
                'telefono':telefonoC, 
                'resideDesde':resideC, 
                'condVivienda':condicionC,
                'lugarTrabajo':lugrTrabC,
                'actividadMicro':actividadMicro,
                'tiempEmptiempFun':tiempoC,
                'salarioIngreso':salarioC, 
                'direccionTrabMicro':direccionMC,        
                'telefonoTrabMicro':telefonoMC,
                'tipo':tipo,
                'estado':"1",
                'idSolicitud':soli}) 

        else:
            domicilioC = domicilio.objects.update_or_create(idSolicitud=idSoli, id=idd,
            defaults={ 'direccion':direActC,
                'referencia':puntoRefC,
                'telefono':telefonoC, 
                'resideDesde':resideC, 
                'condVivienda':condicionC,
                'lugarTrabajo':lugrTrabC,
                'actividadMicro':actividadMicro,
                'tiempEmptiempFun':tiempoC,
                'salarioIngreso':salarioC, 
                'direccionTrabMicro':direccionMC,        
                'telefonoTrabMicro':telefonoMC,
                'tipo':tipo,
                'estado':"1",
                'idSolicitud':soli}) 

#Inicia modificar datos de la obre a realiar
    bandera= request.POST['passDOR'] 
    if(bandera == '1'):
        destinoME =request.POST['destinoME']
        duenoME =request.POST['duenoME']
        parentescoME =request.POST['parentescoME']
        direExacta=request.POST['direccionE'] 
        detalleObra =request.POST['detalleObra']   
        PresupuestoME =request.POST['PresupuestoME']
        if(PresupuestoME==""):
            PresupuestoME=0.00
        detalleAlt=Alternativa.objects.get(id=destinoME)
        detalleObra=ModeloVivienda.objects.get(id=detalleObra)
        dor = datosObra.objects.update_or_create(idSolicitud=idSoli,
        defaults={ 'destino':detalleAlt, 
        'dueno': duenoME, 
        'parentesco':parentescoME, 
        'direExacta':direExacta, 
        'detalle':detalleObra, 
        'presupuesto':PresupuestoME, 
        'estado':"1",
        'idSolicitud':soli}) 
    
#Inicia modificar detalle de la solicitud  
    bandera= request.POST['passDS'] 
    if(bandera == '1'):
        montoME =request.POST['montoME']
        if(montoME==""):
            montoME=0
        plazoME =request.POST['plazoME']
        cuotaME =request.POST['cuotaME']
        if(cuotaME==""):
            cuotaME=0
        formaPagoME =request.POST['formaPagoME']   
        FechaPagoME =request.POST['FechaPagoME']
        
        ds = detalle.objects.update_or_create(idSolicitud=idSoli, 
        defaults={ 'monto':montoME, 
        'plazo': plazoME, 
        'cuota':cuotaME, 
        'formaPago':formaPagoME, 
        'fechaPago': FechaPagoME, 
        'estado':'1',
        'idSolicitud':soli})

#Inicia modificar experiencia crediticia
    idExC=request.POST.getlist('idExC')
    lugarEC =request.POST.getlist('lugarEC') 
    montoEC =request.POST.getlist('montoEC')
    fechaEC =request.POST.getlist('fechaEC')
    estadoEC=request.POST.getlist('estadoEC')
    cuotaEC =request.POST.getlist('cuotaEC')       
       
    for i in range(len(lugarEC)):     
        
     if(lugarEC[i] != ""):
        if(montoEC[i]==""):
                 montoEC[i]='0.00'            
        if(cuotaEC[i]==""):
                cuotaEC[i]='0.00'
        if(idExC[i]!=""):    
                if(fechaEC[i]==""):  
                    experiencia = experienciCrediticia.objects.update_or_create(idSolicitud=idSoli, id=idExC[i],
                defaults={'lugar':lugarEC[i],
            'monto':montoEC[i], 
            'estado':estadoEC[i],  
            'cuota':cuotaEC[i], 
            'estadoE':1,
            'posee':False,
            'idSolicitud':soli})
                else:
                    experiencia = experienciCrediticia.objects.update_or_create(idSolicitud=idSoli, id=idExC[i],
                defaults={'lugar':lugarEC[i],
            'monto':montoEC[i], 
            'fechaOtorgamiento':fechaEC[i],
            'estado':estadoEC[i],  
            'cuota':cuotaEC[i], 
            'estadoE':1,
            'posee':False,
            'idSolicitud':soli})        
        else:
            if(fechaEC[i]==""):  
                    experiencia = experienciCrediticia.objects.update_or_create(idSolicitud=idSoli,lugar=lugarEC[i],monto=montoEC[i],estado=estadoEC[i], 
                defaults={'lugar':lugarEC[i],
            'monto':montoEC[i], 
            'estado':estadoEC[i],  
            'cuota':cuotaEC[i], 
            'posee':False,
            'estadoE':1,
            'idSolicitud':soli})
            else:
                    experiencia = experienciCrediticia.objects.update_or_create(idSolicitud=idSoli,fechaOtorgamiento=fechaEC[i], lugar=lugarEC[i],monto=montoEC[i],estado=estadoEC[i],
                defaults={'lugar':lugarEC[i],
            'monto':montoEC[i], 
            'fechaOtorgamiento':fechaEC[i],
            'estado':estadoEC[i],  
            'cuota':cuotaEC[i], 
            'estadoE':1,
            'posee':False,
            'idSolicitud':soli})  

#inicia modificar referencias personales
    idRF=request.POST.getlist('idRF')
    nombreRPF =request.POST.getlist('nombreRPF') 
    parentescoRPF =request.POST.getlist('parentescoRPF')
    domicilioRPF =request.POST.getlist('domicilioRPF')
    telefonoRPF=request.POST.getlist('telefonoRPF')

    for i in range(len(nombreRPF )):
     
      
      if(nombreRPF [i] != ""):
        if(idRF[i]==""):
            refer = referencias.objects.update_or_create(idSolicitud=idSoli, 
            defaults={'nombre':nombreRPF[i],
            'parentesco':parentescoRPF[i], 
            'domicilio':domicilioRPF[i],
            'telefono':telefonoRPF[i],  
            'estado':"1",
            'idSolicitud':soli})
        else: 
            refer = referencias.objects.update_or_create(idSolicitud=idSoli, id=idRF[i],
            defaults={'nombre':nombreRPF[i],
            'parentesco':parentescoRPF[i], 
            'domicilio':domicilioRPF[i],
            'telefono':telefonoRPF[i],  
            'estado':"1",
            'idSolicitud':soli})

#Inicia modificar comentarios
    bandera= request.POST['passCM'] #inicia guardar comentarios
    if(bandera == '1'):
        comIniciativa =request.POST['comIniciativa']
        comEvaluacion =request.POST['comEvaluacion']
        comGarantia =request.POST['comGarantia']
        print(comEvaluacion)
        comn = comentarios.objects.update_or_create(idSolicitud=idSoli,
            defaults={'CSN' :comIniciativa,
            'CEE':comEvaluacion,
            'CGO':comGarantia,
            'estado':"1",       
            'idSolicitud':soli })

    # inicio medio por el cual se informo
        try:
            redes =request.POST['redes']
        except :
            redes= " "
        try:
            pvv =request.POST['pvv']
        except :
            pvv= " "
        try:
            referenciado =request.POST['referenciado']
        except :
            referenciado= " "
        try:
            perifoneo =request.POST['perifoneo']
        except :
            perifoneo= " "
        try:
            radio =request.POST['radio']
        except :
            radio= " "
        try:
            feriav =request.POST['feriav']
        except :
            feriav= " "
        try:
            campanap =request.POST['campaprom']
        except :
            campanap= " "
        try:
            otros =request.POST['otros']
        except :
            otros= " "
        try:
            especifique =request.POST['espeotromed']
        except :
            especifique= " "

        estadom= 1

        medio = Medio.objects.update_or_create(idSolicitud=idSoli,
            defaults={'redes':redes,
                    'pvv':pvv,
                    'referenciado':referenciado,
                    'perifoneo':perifoneo,
                    'radio':radio,
                    'feriav':feriav,
                    'campanap':campanap,
                    'otros':otros,
                    'especifique':especifique,
                    'estado':estadom, 
                    'idSolicitud':soli
            })
        

    registroBit(request, "Se actualizo formularSolicitud Microempresa " + soli.perfil.dui, "Actualizacion")
    return redirect('administrarPerfil', id=soli.perfil.id)  # id de perfil 

def listaRF(request):
    listSoli = solicitud.objects.filter(estado="Completado", tipo="micro")
    #listapo=Presupuestovdg.objects.all()
    return render(request, "SolicitudesApp/listaReportesF.html", {"solicitudes":listSoli})


#########################################################
#lista de solicitudes pendientes de aprobacion 
def listaSolicitudesPA(request): 
    #listperpa=Perfil.objects.filter(estado="activo", estadosoli=11)
    # consulta las solicitudes que estan activas y pendientes de aprobacion
    listperpa = solicitud.objects.filter(tipo="micro",estadosoli=3, perfil__estadosoli=11, perfil__estado='activo')

    return render(request, "SolicitudesApp/listaSolicitudPA.html", {"solicitudes":listperpa})

def evaluarSol(request, id): 
    try:
        s = solicitud.objects.get(id=id)
    except solicitud.DoesNotExist:
        s=""
    try:
        dt=detalle.objects.get(idSolicitud=s.id)
    except detalle.DoesNotExist:
        dt=""

    return render(request, "SolicitudesApp/evaluarSolicitud.html", {"s":s,"dt":dt})


def registrarEvaluacion(request):
    id=request.POST['ids']
    eval=request.POST['evaluacion'] # si es 4 = aprobado, 5 = observado, 6= denegado
    try:
        obs=request.POST['observacion']
    except :
        obs=""
    #print(id)
    #print(eval)
    #print(obs)
    evaluar=""
    if eval==4:
        evaluar="Aprobo"
    elif eval==5:
        evaluar="Observo"
    else:
        evaluar="Denego"
    msol=solicitud.objects.get(id=id)
    msol.estadosoli=eval
    msol.observaciones=obs
    msol.save()

    mensaje="Datos guardados"
    registroBit(request, "Se "+ evaluar +" la solicitud " + msol.perfil.dui, "Evaluacion")
    messages.success(request, mensaje)

    return redirect('listaSolicitudesPA')

#lista de solicitudes observadas= 5
def listaSolicitudesObs(request): 
    listperpa = solicitud.objects.filter(tipo="micro",estadosoli=5, perfil__estado='activo')

    return render(request, "SolicitudesApp/listaSObservadas.html", {"solicitudes":listperpa})

#lista de solicitudes  denegadas=6
def listaSolicitudesDen(request): 
    listperpa = solicitud.objects.filter(tipo="micro",estadosoli=6, perfil__estado='activo')

    return render(request, "SolicitudesApp/listaSDenegadas.html", {"solicitudes":listperpa})

def obtenerRango(request):
    id = request.GET['id']   
    alternativa = "-0"
    if request.is_ajax():  
        try: 
            alternativa = Alternativa.objects.get(id=id) 
            serialized_data =  serialize("json", [ alternativa ])
        except Exception: 
            serialized_data = json.dumps( alternativa , default=str)
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})
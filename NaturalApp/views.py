import json
from django.http.response import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render,redirect, HttpResponse
from ClienteApp.models import *
from django.contrib import messages
from ListaChequeoApp.models import listaChequeo
from NaturalApp.models import *
from SolicitudesApp.models import *
from EvaluacionIvEFApp.models import *
from datetime import  datetime
from time import strftime, strptime
from django.db.models import Q

from TesisApp.views import registroBit


# Create your views here.
def registrarSolicitudNatu(request, idCliente):
   #try:
        cliente = Perfil.objects.get(id=idCliente)
        egresosf = Egresosf.objects.get(estado="1", idp = idCliente )
        ingresosf = Ingresosf.objects.get(ide = egresosf.id)
        capacidad = Capacidadpagof.objects.get(ide=egresosf.id)
        alternativas = Alternativa.objects.all()
        modelos = ModeloVivienda.objects.all()
        return render(request, "NaturalApp/solicitudNatural.html", {
            "cliente":cliente, "ingresosf":ingresosf, "alternativas":alternativas,"modelos":modelos, "capacidaPago":capacidad})

    
def registroSolicitudN(request):
    tipoobra=request.POST['tipoobra']
    fecha= request.POST['fechaSN']
    #agencia= Agencia.objects.get(id= request.POST['agenciaN'])
    cliente=Perfil.objects.get(id= request.POST['idCliente'])
    n= request.POST['n']
    comunidad= request.POST['comunidadN'].upper()
   # muni= request.POST['municipioN']
    area= request.POST['areaN']
    tipoingreso= request.POST['tipoingreso']
    estado= request.POST['estadoN']

    soli= solicitud.objects.create(tipoobra=tipoobra,fecha=fecha, numero=n, comunidad=comunidad, area=area, tipo="natural",tipoingreso=tipoingreso, estado=estado,perfil=cliente, estadosoli=3 )
    
    cliente.estadosoli=4
    cliente.save()


    idSoli= solicitud.objects.get(fecha=fecha,tipo="natural",perfil=cliente)
   
   # soli.perfil.add(cliente)        para guardar en la tabla solicitud_perfil

    #idSoli= solicitud.objects.all().last() #obtengo la ultima solicitud registrada  
    registroBit(request, "Se registro formulario Solicitud personal " + idSoli.perfil.dui, "Registro")
    
    #      #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.create(fecha=fecha,solicitudc="Si",estado="incompleto",ids=idSoli) 


    bandera= request.POST['passDPN']  # guarda datos personales
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
        
   
    bandera= request.POST['passDPNC']  # guarda datos personales
    if(bandera == '1'):   
        sinFE=0                 #sin fecha de expiracion
        sinFN=0                 #sin fecha de nacimiento
        tipo=request.POST['tipoSN']
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


    bandera= request.POST['passGPN'] #inicia guardar grupo familiar
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

    bandera= request.POST['passDLN'] #inicia guardar domicilio y lugar de trabajo
    if(bandera == '1'):
       direActS =request.POST['direActS']# guarda direccion del solicitante
       puntoRefS =request.POST['puntoRefS']
       telefonoS =request.POST['telefonoS']
       condicionS =request.POST['condicionS']       
       resideS=request.POST['resideS']
       lugrTrabS =request.POST['lugrTrabS']
       jefS =request.POST['jefeS']
       tiempoS =request.POST['tiempoS']       
       salarioS =request.POST['salarioS']
       if(salarioS==""):
            salarioS='0'
       direccionNS =request.POST['direccionNS']
       telefonoNS =request.POST['telefonoNS']
       tipo="Solicitante"
       estadoSS=1
       domicilioS = domicilio.objects.create(direccion=direActS, referencia=puntoRefS,telefono=telefonoS, resideDesde=resideS, 
       condVivienda=condicionS, lugarTrabajo=lugrTrabS,  jefeInm=jefS, tiempEmptiempFun=tiempoS, salarioIngreso=salarioS, 
       direccionTrabMicro=direccionNS, telefonoTrabMicro=telefonoNS, tipo=tipo,estado=estadoSS, idSolicitud=idSoli) 
       
    bandera= request.POST['passDLNC'] #inicia guardar domicilio y lugar de trabajo
    if(bandera == '1'):
       
       direActC =request.POST['direActC']# guarda direccion del conyuge o codeudor     
       puntoRefC =request.POST['puntoRefC']
       telefonoC =request.POST['telefonoC']
       condicionC =request.POST['condicionC'] 
       resideC=request.POST['resideC']
       lugrTrabC =request.POST['lugrTrabC']
       jefC =request.POST['jefeC']
       tiempoC =request.POST['tiempoC']
       salarioC =request.POST['salarioC']
       if(salarioC==""):
            salarioC='0'
       direccionNC =request.POST['direccionNC']
       telefonoNC =request.POST['telefonoNC']
       tipo=request.POST['tipoSN']
       estadoSC=1

       domicilioS = domicilio.objects.create(direccion=direActC, referencia=puntoRefC,telefono=telefonoC, resideDesde=resideC, 
       condVivienda=condicionC, lugarTrabajo=lugrTrabC, jefeInm=jefC, tiempEmptiempFun=tiempoC, salarioIngreso=salarioC, 
       direccionTrabMicro=direccionNC,telefonoTrabMicro=telefonoNC, tipo=tipo,estado=estadoSC, idSolicitud=idSoli)
    #fin domicilio y lugar de trabajo 

    bandera= request.POST['passDORN'] #inicia guardar datos de la obra a realizar
    if(bandera == '1'):
       destinoNE =request.POST['destinoNE']
       duenoNE =request.POST['duenoNE']
       parentescoNE =request.POST['parentescoNE']
       direExacta=request.POST['direccionE'] 
       detalleObra =request.POST['detalleObra'] 
       detalleadic =request.POST['detalleAD']  
       PresupuestoME =request.POST['PresupuestoNE']
       if(PresupuestoME==""):
            PresupuestoME='0'
       estadoO=1
       destinoAlt=Alternativa.objects.get(id=destinoNE)
       modeloVivienda= ModeloVivienda.objects.get(id=detalleObra)
       modeloVivienda.id=detalleObra
       
       dor = datosObra.objects.create(destino=destinoAlt, dueno= duenoNE, parentesco=parentescoNE,direExacta=direExacta ,
      detalle=modeloVivienda,detalleadic=detalleadic, presupuesto=PresupuestoME,estado=estadoO, idSolicitud=idSoli) 
    #fin datos de la obra a realizar


    bandera= request.POST['passDSN'] #inicia guardar detalle de la solicitud
    if(bandera == '1'):
       montoNE =request.POST['montoNE']
       if(montoNE==""):
            montoNE='0'
       plazoNE =request.POST['plazoNE']
       cuotaNE =request.POST['cuotaNE']
       if(cuotaNE==""):
            cuotaNE='0'
       formaPagoNE =request.POST['formaPagoNE']   
       FechaPagoNE =request.POST['FechaPagoNE']
       estadoD=1
       ds = detalle.objects.create(monto=montoNE, plazo= plazoNE, cuota=cuotaNE, 
      formaPago=formaPagoNE, fechaPago= FechaPagoNE,estado=estadoD, idSolicitud=idSoli) 
    #fin detalle de la solicitud

    bandera= request.POST['passECN'] #inicia experiencia crediticia
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


    bandera= request.POST['passRPFN'] #inicia referencias personales y familiares
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
    
    bandera= request.POST['passCMN'] #inicia guardar comentarios
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

    return redirect('administrarPerfil', id=soli.perfil.id)  # id de perfil 

def listarSNC(request): 
    listSolinc = solicitud.objects.filter(estado="Completado", tipo="natural")
    return render(request, "NaturalApp/listarSNC.html", {"solicitudes":listSolinc})

def listarSN(request): 
    listSolin = solicitud.objects.filter(estado="Incompleto",tipo="natural")
    return render(request, "NaturalApp/listarSN.html", {"solicitudes":listSolin})

def editarSolicitudN(request, idSolicitud):
   
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
         egresosf  = Egresosf.objects.get(idp = id_cliente, estado=1)
         try:
             ingresosf = Ingresosf.objects.get(ide=egresosf.id)
         except Ingresosf.DoesNotExist:
             None
         try:
             capacidad = Capacidadpagof.objects.get(ide=egresosf.id)
         except Capacidadpagof.DoesNotExist:
             None
    except Egresosf.DoesNotExist:
          egresosf = ""   
          ingresosf =  ""
          capacidad=  ""
          
    
    alternativas = Alternativa.objects.all()
    modelos = ModeloVivienda.objects.all()

    soli = [solici, dps, dpc, gpf, mdl, mdlc, dob, ds, ec, rp, cmt,med]
    return render(request, "NaturalApp/modificarSolicitudNatural.html", {
        "soli":soli,
        "alternativas":alternativas,
        "modelos":modelos,
        "ingresosf":ingresosf, 
        "capacidaPago":capacidad
        })



def modSoliNatural(request):
# Inicia modifcar solicitud
#datos generales de la solicitd   
    idSoli=request.POST['idSoliN']
    tipoobra=request.POST['tipoobraModN']
    #fecha= request.POST['fechaSMM']
    #agencia= Agencia.objects.get(id= request.POST['agenciaMod'])
    #cliente=Perfil.objects.get(id= request.POST['idCliente'])
    n= request.POST['nModN']
    comunidad= request.POST['comunidadModN']
    #muni= request.POST['municipioMod']
    area= request.POST['areaMN']
    tipoing = request.POST['tipoingresoModN']
    estado= request.POST['estadoMod']
    print(idSoli)
    print(tipoobra)
    print(n)
    print(comunidad)
    print(area)
    print(tipoing)
    print(estado)

    soli = solicitud.objects.get(id=idSoli)
    soli.tipoobra = tipoobra
    soli.numero = n
    soli.comunidad = comunidad
    soli.area = area
    soli.tipoingreso = tipoing
    soli.estado = estado
    soli.save()

#Inicia modificar datos personales del solicitande    
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
    bandera= request.POST['passDPNC']  # guarda datos personales
    if(bandera == '1'):  
        id= request.POST['idC']
        tipo=request.POST['tipoSN']
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
    idGP=request.POST.getlist('idGPN')
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

#Inicia modificar domicilio del solicitante
    bandera= request.POST['passDLN'] 
    if(bandera == '1'):
        direActS =request.POST['direActS']
        puntoRefS =request.POST['puntoRefS']
        telefonoS =request.POST['telefonoS']
        condicionS =request.POST['condicionS']       
        resideS=request.POST['resideS']
        lugrTrabS =request.POST['lugrTrabS']
        jefS =request.POST['jefeS']
        tiempoS =request.POST['tiempoS']
        
        salarioS =request.POST['salarioS']
        if(salarioS==""):
            salarioS=0.00
        direccionNS =request.POST['direccionNS']
        telefonoNS =request.POST['telefonoNS']
        tipo="Solicitante"
        print(salarioS)
        domicilioS = domicilio.objects.update_or_create(idSolicitud=idSoli,tipo="Solicitante",
        defaults={ 'direccion':direActS,
            'referencia':puntoRefS,
            'telefono':telefonoS, 
            'resideDesde':resideS, 
            'condVivienda':condicionS,
            'lugarTrabajo':lugrTrabS,
            'jefeInm':jefS,
            'tiempEmptiempFun':tiempoS,
            'salarioIngreso':salarioS, 
            'direccionTrabMicro':direccionNS,       
            'telefonoTrabMicro':telefonoNS,
            'tipo':tipo,
            'estado':"1",
            'idSolicitud':soli}) 

#inicia actualizaar domicilio conyuge o codeudor
    bandera= request.POST['passDLNC'] 
    if(bandera == '1'):
        idd=request.POST['idDomicilioCCN']   
        direActC =request.POST['direActC']
        puntoRefC =request.POST['puntoRefC']
        telefonoC =request.POST['telefonoC']
        condicionC =request.POST['condicionC']       
        resideC=request.POST['resideC']
        lugrTrabC =request.POST['lugrTrabC']
        jefC =request.POST['jefeC']
        tiempoC =request.POST['tiempoC']
        salarioC =request.POST['salarioC']
        if(salarioC==""):
            salarioC=0
        direccionNC =request.POST['direccionNC']
        telefonoNC =request.POST['telefonoNC']
        tipo=request.POST['tipoSN']

        if(idd==""):
                domicilioC = domicilio.objects.update_or_create(idSolicitud=idSoli, tipo=tipo,
            defaults={ 'direccion':direActC,
                'referencia':puntoRefC,
                'telefono':telefonoC, 
                'resideDesde':resideC, 
                'condVivienda':condicionC,
                'lugarTrabajo':lugrTrabC,
                'jefeInm':jefC,
                'tiempEmptiempFun':tiempoC,
                'salarioIngreso':salarioC, 
                'direccionTrabMicro':direccionNC,        
                'telefonoTrabMicro':telefonoNC,
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
                'jefeInm':jefC,
                'tiempEmptiempFun':tiempoC,
                'salarioIngreso':salarioC, 
                'direccionTrabMicro':direccionNC,        
                'telefonoTrabMicro':telefonoNC,
                'tipo':tipo,
                'estado':"1",
                'idSolicitud':soli}) 

#Inicia modificar datos de la obre a realiar
    bandera= request.POST['passDORN'] 
    if(bandera == '1'):
        destinoNE =request.POST['destinoNE']
        duenoNE =request.POST['duenoNE']
        parentescoNE =request.POST['parentescoNE']
        direExacta=request.POST['direccionE'] 
        detalleObra =request.POST['detalleObra']
        detalleadic =request.POST['detalleAD']     
        PresupuestoNE =request.POST['PresupuestoNE']
        if(PresupuestoNE==""):
            PresupuestoNE=0.00
        destinoAlt=Alternativa.objects.get(id=destinoNE)    
        detalleObra=ModeloVivienda.objects.get(id=detalleObra)
        dor = datosObra.objects.update_or_create(idSolicitud=idSoli,
        defaults={ 'destino':destinoAlt, 
        'dueno': duenoNE, 
        'parentesco':parentescoNE, 
        'direExacta':direExacta, 
        'detalle':detalleObra, 
        'detalleadic':detalleadic,
        'presupuesto':PresupuestoNE, 
        'estado':"1",
        'idSolicitud':soli}) 
    
#Inicia modificar detalle de la solicitud  
    bandera= request.POST['passDSN'] 
    if(bandera == '1'):
        montoNE =request.POST['montoNE']
        if(montoNE==""):
            montoNE=0
        plazoNE =request.POST['plazoNE']
        cuotaNE =request.POST['cuotaNE']
        if(cuotaNE==""):
            cuotaNE=0
        formaPagoNE =request.POST['formaPagoNE']   
        FechaPagoNE =request.POST['FechaPagoNE']
        
        ds = detalle.objects.update_or_create(idSolicitud=idSoli, 
        defaults={ 'monto':montoNE, 
        'plazo': plazoNE, 
        'cuota':cuotaNE, 
        'formaPago':formaPagoNE, 
        'fechaPago': FechaPagoNE, 
        'estado':'1',
        'idSolicitud':soli})

#Inicia modificar experiencia crediticia
    idExC=request.POST.getlist('idExCN')
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
    idRF=request.POST.getlist('idRFN')
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
    bandera= request.POST['passCMN'] #inicia guardar comentarios
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
        
    registroBit(request, "Se actualizo formulario Solicitud personal " + soli.perfil.dui, "Actualizacion")

    return redirect('administrarPerfil', id=soli.perfil.id)  # id de perfil 

# lista de reportes para el comite
def listaRF(request):
    listSoli = solicitud.objects.filter(estado="Completado", tipo="natural")
    #listapo=Presupuestovdg.objects.all()
    return render(request, "NaturalApp/listaReportesF.html", {"solicitudes":listSoli})

#########################################################
#lista de solicitudes pendientes de aprobacion 
def listaSolicitudesPA(request): 
    listperpa = solicitud.objects.filter(tipo="natural",estadosoli=3, perfil__estadosoli=11, perfil__estado='activo')
    return render(request, "NaturalApp/listaSolicitudPA.html", {"solicitudes":listperpa})

#lista de solicitudes observadas= 5
def listaSolicitudesObs(request): 
    listperpa = solicitud.objects.filter(tipo="natural",estadosoli=5, perfil__estado='activo')

    return render(request, "NaturalApp/listaSObservadas.html", {"solicitudes":listperpa})

#lista de solicitudes  denegadas=6
def listaSolicitudesDen(request): 
    listperpa = solicitud.objects.filter(tipo="natural",estadosoli=6, perfil__estado='activo')

    return render(request, "NaturalApp/listaSDenegadas.html", {"solicitudes":listperpa})

def obtenerRango(request):
    id = request.GET['id']   
    alternativa = "-0"
    if request.is_ajax():  
        try: 
            alternativa = Alternativa.objects.get(id=id) 
            serialized_data =  serialize("json", [  alternativa ])
        except Exception: 
            serialized_data = json.dumps( alternativa , default=str)
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})




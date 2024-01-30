from django.shortcuts import render, redirect
from django.contrib import messages
from ClienteApp.models import Perfil
from SolicitudesApp.models import *
from DeclaracionJurClienteApp.models import *
from TesisApp.views import registroBit

# Create your views here.

def declaracionjc(request, id):

    sol= Declaracionjc.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    if sol == True:
        solv= Declaracionjc.objects.get(ids=id)
    
        return redirect('editarDJ', id=solv.iddj)     
    else:
        try:
            listato=TipoOperacion.objects.filter(estado="activo")
        except TipoOperacion.DoesNotExist:
            listato=""
        try:
            s=  solicitud.objects.get(id=id)
        except solicitud.DoesNotExist:
            s=""
        try:
            d=  detalle.objects.get(idSolicitud=id)
        except detalle.DoesNotExist:
            d=""
        return render(request, "DeclaracionJurClienteApp/declaracionjc.html", {"s":s,"d":d,"operaciones":listato}) 

def registrarDj(request): 
  
    ids=request.POST['ids']
    nombrepna=request.POST['nombrepn']
    duipna=request.POST['ndui']
    toperacion=request.POST['tipoop']
    ncredito=request.POST['ncredito']
    monto=request.POST['monto']   
    plazo=request.POST['plazo']
    cuota=request.POST['cuota']
    formapago=request.POST['fpago']
    cancelacionda=request.POST['creditocan']
    rpagosa=request.POST['rpagosa']
    try:
       procedenciafond=request.POST['procedenciaf']
    except :
        procedenciafond=""
    
    idto=TipoOperacion.objects.get(id=toperacion)
    idto.id=toperacion
    idsol= solicitud.objects.get(id=ids)
    idsol.id=ids 

    declaracionjc= Declaracionjc.objects.create(nombrepna=nombrepna,duipna=duipna,toperacion=idto,ncredito=ncredito,monto=monto,plazo=plazo,cuota=cuota,formapago=formapago,cancelacionda=cancelacionda,rpagosa=rpagosa,procedenciafond=procedenciafond,ids=idsol)
   
    iddjc= Declaracionjc.objects.all().last() #obtengo la ultima declaracion registrada 


    bandera= request.POST['passAE']  # guarda datos de 
    if(bandera == '1'):
        try:
            empleadoen=request.POST['empleadoen']
        except :
            empleadoen=""
        try:
            profecinalind=request.POST['profecionind']
        except :
            profecinalind=""  
        try:
            conocimientoen=request.POST['conocimientoen']
        except :
            conocimientoen=""   
        try:
            empresarioen=request.POST['empresarioen']
        except :
            empresarioen=""   
        try:
            especificaro=request.POST['otrosesp']
        except :
            especificaro=""   
        
       
    declaracionjcaern=Declaracionjcaern.objects.create(empleadoen=empleadoen,profecinalind=profecinalind,conocimientoen=conocimientoen,empresarioen=empresarioen,especificaro=especificaro,iddj=iddjc)
   
    bandera= request.POST['passGN']  # guarda datos de 
    if(bandera == '1'):
        
        try:
            empresa=request.POST['empresad']
        except :
            empresa=""  
        try:
            industriade=request.POST['industiad']
        except :
            industriade=""  
        try:
            comercio=request.POST['comerciod']
        except :
            comercio=""  
        try:
            especificarot=request.POST['espotros']
        except :
            especificarot=""  
       
    declaracionjcjnm=Declaracionjcjnm.objects.create(empresa=empresa,industriade=industriade,comercio=comercio,especificarot=especificarot,iddj=iddjc)
   
    mensaje="Datos guardados"
    registroBit(request, "Se registro Declaracion Jurada " + nombrepna, "Registro")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=declaracionjc.ids.perfil.id)  # id de perfil 

def listaDJ(request):
    listj=  Declaracionjc.objects.all()
    #listper=Perfil.objects.filter(estado="activo")
    return render(request, "DeclaracionJurClienteApp/listaDJ.html", {"listj":listj})

def editarDJ(request, id):
    listato=TipoOperacion.objects.all()

    try:
        dj=  Declaracionjc.objects.get(iddj=id)
    except Declaracionjc.DoesNotExist:
        dj=""
    try:
        dja=  Declaracionjcaern.objects.get(iddj=id)
    except Declaracionjcaern.DoesNotExist:
        dja=""
    try:
        djn=  Declaracionjcjnm.objects.get(iddj=id)
    except Declaracionjcjnm.DoesNotExist:
        djn=""
    idSol=dj.ids.id
    try:
        s=  solicitud.objects.get(id=idSol)
    except solicitud.DoesNotExist:
        s=""

    try:
        d=  detalle.objects.get(idSolicitud=idSol)
    except detalle.DoesNotExist:
        d=""

    return render(request, "DeclaracionJurClienteApp/EditarDeclaracionjc.html", {"s":s,"d":d,"operaciones":listato,"dj":dj,"dja":dja,"djn":djn}) 


def modificarDJ(request): 
  
    idj=request.POST['idj']
    nombrepna=request.POST['nombrepn']
    duipna=request.POST['ndui']
    toperacion=request.POST['tipoop']
    ncredito=request.POST['ncredito']
    monto=request.POST['monto']   
    plazo=request.POST['plazo']
    cuota=request.POST['cuota']
    formapago=request.POST['fpago']
    cancelacionda=request.POST['creditocan']
    rpagosa=request.POST['rpagosa']
    try:
       procedenciafond=request.POST['procedenciaf']
    except :
        procedenciafond=""
    
    idto=TipoOperacion.objects.get(id=toperacion)
    idto.id=toperacion

    declaracionjc= Declaracionjc.objects.get(iddj=idj)
    declaracionjc.nombrepna=nombrepna
    declaracionjc.duipna=duipna
    declaracionjc.toperacion=idto
    declaracionjc.ncredito=ncredito
    declaracionjc.monto=monto
    declaracionjc.plazo=plazo
    declaracionjc.cuota=cuota
    declaracionjc.formapago=formapago
    declaracionjc.cancelacionda=cancelacionda
    declaracionjc.rpagosa=rpagosa
    declaracionjc.procedenciafond=procedenciafond
    declaracionjc.save()


    bandera= request.POST['passAE']  # guarda datos de 
    if(bandera == '1'):
        try:
            empleadoen=request.POST['empleadoen']
        except :
            empleadoen=""
        try:
            profecinalind=request.POST['profecionind']
        except :
            profecinalind=""  
        try:
            conocimientoen=request.POST['conocimientoen']
        except :
            conocimientoen=""   
        try:
            empresarioen=request.POST['empresarioen']
        except :
            empresarioen=""   
        try:
            especificaro=request.POST['otrosesp']
        except :
            especificaro=""   
        
       
    declaracionjcaern=Declaracionjcaern.objects.get(iddj=idj)
    declaracionjcaern.empleadoen=empleadoen
    declaracionjcaern.profecinalind=profecinalind
    declaracionjcaern.conocimientoen=conocimientoen
    declaracionjcaern.empresarioen=empresarioen
    declaracionjcaern.especificaro=especificaro
    declaracionjcaern.save()
   
    bandera= request.POST['passGN']  # guarda datos de 
    if(bandera == '1'):
        
        try:
            empresa=request.POST['empresad']
        except :
            empresa=""  
        try:
            industriade=request.POST['industiad']
        except :
            industriade=""  
        try:
            comercio=request.POST['comerciod']
        except :
            comercio=""  
        try:
            especificarot=request.POST['espotros']
        except :
            especificarot=""  
       
    declaracionjcjnm=Declaracionjcjnm.objects.get(iddj=idj)
    declaracionjcjnm.empresa=empresa
    declaracionjcjnm.industriade=industriade
    declaracionjcjnm.comercio=comercio
    declaracionjcjnm.especificarot=especificarot
    declaracionjcjnm.save()
   
    mensaje="Datos actualizados"
    registroBit(request, "Se actualizó Declaración Jurada " + nombrepna, "Actualización")
    messages.success(request, mensaje)

    return redirect('administrarPerfil', id=declaracionjc.ids.perfil.id)  
 


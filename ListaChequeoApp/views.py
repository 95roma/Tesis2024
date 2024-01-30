from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from ClienteApp.models import *
from ListaChequeoApp.models import *
from InspeccionMejViviendaApp.models import *
from InspeccionLoteApp.models import *
from PresupuestoApp.models import *
from PresupuestoVApp.models import *
from SolicitudInscripcionSApp.models import *

# Create your views here.
# para lista de chequeo
def listaPC(request): 
    listper=Perfil.objects.filter(estado="activo")
    listSoli = solicitud.objects.filter(estado="Completado")
    return render(request, "ListaChequeoApp/listaPC.html", {"sol":listSoli})

def listaChequeov(request, id): # id d solicitud
    sol= listaChequeo.objects.filter(ids=id).exists() # comprueba si en la tabla existe el registro de la solicitud
    
    if sol == True:
        try:
            idlist = listaChequeo.objects.get(ids=id)  
        except listaChequeo.DoesNotExist:
            idlist= " " 
        return redirect('editarCheq', id=idlist.id)

    elif sol == False:
        try:
            solic = solicitud.objects.get(id=id)  
        except solicitud.DoesNotExist:
            solic= " "   
        return render(request,"ListaChequeoApp/listaChequeo.html", {"soli":solic})


def registrarLC(request): 
    cliente=solicitud.objects.get(id= request.POST['ids'])
    try:
        fecha =request.POST['fecha']
    except :
        fecha= " "
    try:
        solicitudc =request.POST['solicitudc']
    except :
        solicitudc= " "
    try:
        fotocdui =request.POST['fotocDN']
    except :
        fotocdui= " "
    try:
        recibos =request.POST['recibosum']
    except :
        recibos= " "
    try:
        copiaduifia =request.POST['copiaDNF']
    except :
        copiaduifia= " "
    try:
        recibosfia =request.POST['copiaralF']
    except :
        recibosfia= " "
    try:
        constempfia =request.POST['constanciaempF']
    except :
        constempfia= " "
    try:
        refercsfia =request.POST['referenciacsf']
    except :
        refercsfia= " "
    try:
        inspecciontec =request.POST['inspecciont']
    except :
        inspecciontec= " "
    try:
        presupuestocons =request.POST['presupuestoc']
    except :
        presupuestocons= " "
    try:
        certifext =request.POST['certificacionext']
    except :
        certifext= " "
    try:
        carenciabien =request.POST['carenciab']
    except :
        carenciabien= " "
    try:
        fotocescrit =request.POST['fotocescr']
    except :
        fotocescrit= " "
    try:
        declaracions =request.POST['declaracions']
    except :
        declaracions= " "
    try:
        infdicom =request.POST['informeD']
    except :
        infdicom= " "
    try:
        docsing =request.POST['docsi']
    except :
        docsing= " "
    try:
        docrem =request.POST['docrem']
    except :
        docrem= " "
    try:
        cancelpec =request.POST['cancelpec']
    except :
        cancelpec= " "
    try:
        finiquitos =request.POST['finiquitos']
    except :
        finiquitos= " "
    try:
        hojaaprovc =request.POST['hojaac']
    except :
        hojaaprovc= " "
    try:
        cartaelbmutuo =request.POST['cartaem']
    except :
        cartaelbmutuo= " "
    try:
        recibpagp =request.POST['recibopp']
    except :
        recibpagp= " "
    try:
        ordendesi =request.POST['ordendi']
    except :
        ordendesi= " "
    try:
        permisocons =request.POST['permisoc']
    except :
        permisocons= " "
    try:
        cartaentcd =request.POST['cartaecd']
    except :
        cartaentcd= " "
    try:
        fotocmutuo =request.POST['fotocmhs']
    except :
        fotocmutuo= " "
    try:
        gestioncobro =request.POST['gestionesc']
    except :
        gestioncobro= " "

    ###
    try:
        constemp =request.POST['constanciaemp']
    except :
        constemp= " "
    try:
        tacoisss =request.POST['tacoisss']
    except :
        tacoisss= " "
    try:
        analisisec =request.POST['analisisen']
    except :
        analisisec= " "
    try:
        balance =request.POST['balance']
    except :
        balance= " "
    try:
        balanceres =request.POST['balancerst']
    except :
        balanceres= " "


    listaCq= listaChequeo.objects.create(fecha=fecha, solicitudc=solicitudc,fotocdui=fotocdui,recibos=recibos,constemp=constemp,tacoisss=tacoisss,analisisec=analisisec,balance=balance,balanceres=balanceres, copiaduifia=copiaduifia,recibosfia=recibosfia,constempfia=constempfia,refercsfia=refercsfia,inspecciontec=inspecciontec,presupuestocons=presupuestocons,certifext=certifext,carenciabien=carenciabien,fotocescrit=fotocescrit,declaracions=declaracions,infdicom=infdicom,docsing=docsing,docrem=docrem,cancelpec=cancelpec,finiquitos=finiquitos,hojaaprovc=hojaaprovc,cartaelbmutuo=cartaelbmutuo,recibpagp=recibpagp,ordendesi=ordendesi,permisocons=permisocons,cartaentcd=cartaentcd,fotocmutuo=fotocmutuo,gestioncobro=gestioncobro,estado="incompleto",ids=cliente )
    
    
    mensaje="Datos guardados"
    messages.success(request, mensaje)

    return redirect('/ListaChequeoApp/listaPC/')


# para lista de chequeo
def listaC(request): 
    listac=listaChequeo.objects.all()
    return render(request, "ListaChequeoApp/listaC.html", {"listac":listac})


def editarCheq(request, id):
    try:
        lc=  listaChequeo.objects.get(id=id)
    except listaChequeo.DoesNotExist:
        lc=""   

    return render(request,"ListaChequeoApp/editarListaChequeo.html", {"lc":lc})


def modificarCheq(request): 
    idl=request.POST['idlc']

    try:
        fecha =request.POST['fecha']
    except :
        fecha= " "
    try:
        solicitudc =request.POST['solicitudc']
    except :
        solicitudc= " "
    try:
        fotocdui =request.POST['fotocDN']
    except :
        fotocdui= " "
    try:
        recibos =request.POST['recibosum']
    except :
        recibos= " "
    try:
        copiaduifia =request.POST['copiaDNF']
    except :
        copiaduifia= " "
    try:
        recibosfia =request.POST['copiaralF']
    except :
        recibosfia= " "
    try:
        constempfia =request.POST['constanciaempF']
    except :
        constempfia= " "
    try:
        refercsfia =request.POST['referenciacsf']
    except :
        refercsfia= " "
    try:
        inspecciontec =request.POST['inspecciont']
    except :
        inspecciontec= " "
    try:
        presupuestocons =request.POST['presupuestoc']
    except :
        presupuestocons= " "
    try:
        certifext =request.POST['certificacionext']
    except :
        certifext= " "
    try:
        carenciabien =request.POST['carenciab']
    except :
        carenciabien= " "
    try:
        fotocescrit =request.POST['fotocescr']
    except :
        fotocescrit= " "
    try:
        declaracions =request.POST['declaracions']
    except :
        declaracions= " "
    try:
        infdicom =request.POST['informeD']
    except :
        infdicom= " "
    try:
        docsing =request.POST['docsi']
    except :
        docsing= " "
    try:
        docrem =request.POST['docrem']
    except :
        docrem= " "
    try:
        cancelpec =request.POST['cancelpec']
    except :
        cancelpec= " "
    try:
        finiquitos =request.POST['finiquitos']
    except :
        finiquitos= " "
    try:
        hojaaprovc =request.POST['hojaac']
    except :
        hojaaprovc= " "
    try:
        cartaelbmutuo =request.POST['cartaem']
    except :
        cartaelbmutuo= " "
    try:
        recibpagp =request.POST['recibopp']
    except :
        recibpagp= " "
    try:
        ordendesi =request.POST['ordendi']
    except :
        ordendesi= " "
    try:
        permisocons =request.POST['permisoc']
    except :
        permisocons= " "
    try:
        cartaentcd =request.POST['cartaecd']
    except :
        cartaentcd= " "
    try:
        fotocmutuo =request.POST['fotocmhs']
    except :
        fotocmutuo= " "
    try:
        gestioncobro =request.POST['gestionesc']
    except :
        gestioncobro= " "

    ###
    try:
        constemp =request.POST['constanciaemp']
    except :
        constemp= " "
    try:
        tacoisss =request.POST['tacoisss']
    except :
        tacoisss= " "
    try:
        analisisec =request.POST['analisisen']
    except :
        analisisec= " "
    try:
        balance =request.POST['balance']
    except :
        balance= " "
    try:
        balanceres =request.POST['balancerst']
    except :
        balanceres= " "



    listaCq= listaChequeo.objects.update_or_create(id=idl,
            defaults={'fecha':fecha, 'solicitudc':solicitudc,'fotocdui':fotocdui,'recibos':recibos,'constemp':constemp,
                      'tacoisss':tacoisss,'analisisec':analisisec,'balance':balance,'balanceres':balanceres, 'copiaduifia':copiaduifia,
                      'recibosfia':recibosfia,'constempfia':constempfia,'refercsfia':refercsfia,'inspecciontec':inspecciontec,
                      'presupuestocons':presupuestocons,'certifext':certifext,'carenciabien':carenciabien,'fotocescrit':fotocescrit,
                      'declaracions':declaracions,'infdicom':infdicom,'docsing':docsing,'docrem':docrem,'cancelpec':cancelpec,
                      'finiquitos':finiquitos,'hojaaprovc':hojaaprovc,'cartaelbmutuo':cartaelbmutuo,'recibpagp':recibpagp,'ordendesi':ordendesi,
                      'permisocons':permisocons,'cartaentcd':cartaentcd,'fotocmutuo':fotocmutuo,'gestioncobro':gestioncobro ,})
 
    clistaCq= listaChequeo.objects.get(id=idl)
    if clistaCq.solicitudc=="Si" and  clistaCq.fotocdui=="Si" and  clistaCq.recibosagua=="Si" and  clistaCq.recibosluz=="Si"  and clistaCq.constemp=="Si" or clistaCq.analisisec=="Si"  or  clistaCq.balance=="Si" or  clistaCq.balanceres=="Si" and  clistaCq.copiaduifia=="Si" and  clistaCq.recibosfiaagua=="Si" and  clistaCq.recibosfialuz=="Si" and  clistaCq.constempfia=="Si" and  clistaCq.refercsfia=="Si" and  clistaCq.inspecciontec=="Si" and  clistaCq.presupuestocons=="Si" and  clistaCq.certifext=="Si" and  clistaCq.fotocescrit=="Si" and  clistaCq.declaracions=="Si" and  clistaCq.infdicom=="Si" :
        clistaCq.estado="completo"
        clistaCq.save()
    
    
    mensaje="Datos Actualizados"
    messages.success(request, mensaje)

    return redirect('/ListaChequeoApp/listaC/')

#########################################################
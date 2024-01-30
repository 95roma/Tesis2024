from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from ClienteApp.models import *
from HistorialApp.models import *
from EvaluacionIvEFApp.models import *
from EvaluacionMicroApp.models import *
from ListaChequeoApp.models import listaChequeo
import json
from django.db.models import Q

from TesisApp.views import registroBit


# Create your views here.


def listaPerfil(request): 
    listper=Perfil.objects.filter(estado="activo")
    return render(request, "HistorialApp/listaHis.html", {"perfil":listper})

def rangoHist(request):
    return render(request, "HistorialApp/rangoHis.html")

def registroHis(request):
    hismax=request.POST['histmax']
    hismin=request.POST['histmin']
    est= request.POST['est']
    porc=request.POST['porc']
    try:
        estado= RangoHis.objects.filter(tipo=est).exists()
    except:
        estado=False
    try: 
        superpuesto = RangoHis.objects.filter(Q(minimo__lte=hismax, maximo__gte=hismin)).exists()
    except:
        superpuesto=''
    #return not superpuesto

    

    if estado == True or superpuesto == True:
        mensaje="Ese rango DICOM ya existe o pertenece a otro rango"
        messages.warning(request, mensaje)
    else:
        rango=RangoHis.objects.create(minimo=hismin, maximo=hismax, tipo=est, porcentaje=porc)
        
        mensaje="Rango registrado"
        registroBit(request, "Se registro rango DICOM " + est, "Registro")

        messages.success(request, mensaje)

    return redirect("rangoh")

def listaRango(request): 
    rango=RangoHis.objects.all()
    #listper=Perfil.objects.filter(estado="activo")
    return render(request, "HistorialApp/listaRang.html", {"rango":rango})

#Modificar rangos de historial

def editarRango(request, idr):
    
    try:
        rango = RangoHis.objects.get(id=idr)
    except RangoHis.DoesNotExist:
        rango=""

     # Convertir la lista a JSON
    #rango_json = json.dumps(list(rango.values()), default=str)  

    return render(request, "HistorialApp/editrangoHis.html", {"rango":rango})

def modificarRango(request ):
    hismax=request.POST['histmax']
    hismin=request.POST['histmin']
    est= request.POST['est']
    porc=request.POST['porc']

    try:
        estado= RangoHis.objects.filter(tipo=est).exists()
    except:
        estado=False
    try: 
        superpuesto = RangoHis.objects.filter(Q(id!=id, minimo__lte=hismax, maximo__gte=hismin)).exists()
    except:
        superpuesto=''
    #return not superpuesto

    

    if estado == True or superpuesto == True:
        mensaje="Ese rango DICOM ya existe o pertenece a otro rango"
        messages.warning(request, mensaje)
    else:
        rango=RangoHis.objects.create(minimo=hismin, maximo=hismax, tipo=est, porcentaje=porc)
        
        mensaje="Rango modificado"
        registroBit(request, "Se actualizó rango DICOM " + est, "Actualización")

        messages.success(request, mensaje)

    return '/'
#def regisRanCli(request,id): 
#    per=Perfil.objects.get(id=id)
#    ran=RangoHis.objects.all()
    #listper=Perfil.objects.filter(estado="activo")
#    return render(request, "HistorialApp/regisRangoCli.html", {"per":per, "rango":ran})


#Resgistrar puntaje del cliente
def regisRanCli(request, id):
    
    per = solicitud.objects.get(id=id)
    ran = RangoHis.objects.all()
    ran_data = list(ran.values())
     # Serializa el campo Decimal usando la función personalizada y el DjangoJSONEncoder
    for item in ran_data:
        if 'porcentaje' in item:
            item['porcentaje'] = float(item['porcentaje'])
            
    ran_json = json.dumps(ran_data)# Convertir la lista a JSON
    return render(request, "HistorialApp/regisRangoCli.html", {"per": per, "ran_json": ran_json, "ran":ran})



def regisPunt(request):
    fe=request.POST['fec']
    punt=request.POST['punt']
    idp=request.POST['idp']
    idh= request.POST['idh']

    idpr=solicitud.objects.get(id= idp)
    idpr.id=idp
    idhi= RangoHis.objects.get(id=idh)
    idhi.id=idh
    if idpr.tipo=='micro':
        eva= Balancesm.objects.get(idp=idpr.perfil)
        
    else:
        eva=Egresosf.objects.get(idp=idpr.perfil)
    try:
        regis=RegHis.objects.filter(idsolicitud=idpr).exists()
    except:
        regis=False
    if(regis != True):
        print(regis)
        if(idhi.porcentaje==0):
            regis=RegHis.objects.create(puntaje=punt, fecha=fe, idRango=idhi, idsolicitud=idpr)
            idpr.observaciones="Su puntaje de DICOM no aplica para financiamiento"
            idpr.estadosoli=6 #Denegar la solicitud porque el puntaje es muy bajo
            idpr.save()
            idpr.perfil.estadosoli=10 # Indicar en perfil que ya se registro dicom
            idpr.perfil.save()
            eva.estado=2 #Desactivar evaluacion si el DICOM es bajo
            eva.save()
                    
            mensaje="Su solicitud de credito NO procede, su puntaje DICOM es muy bajo"
            registroBit(request, "Se registro puntaje DICOM bajo del cliente " + idpr.perfil.dui, "Registro")

        else:# El 65% de su credito al que puede aplicar
            regis=RegHis.objects.create(puntaje=punt, fecha=fe, idRango=idhi, idsolicitud=idpr)
            idpr.perfil.estadosoli=10
            idpr.perfil.save()
            mensaje="Puntaje DICOM registrado"
            registroBit(request, "Se registro puntaje DICOM del cliente " + idpr.perfil.dui, "Registro")

        messages.success(request, mensaje)
    else:
        mensaje="La solicitud ya posee un puntaje registrado"
    # puntaje es mayor a 450 y menor o igual a 550 el 75% del credito
    #puntaje mayor a 550 y menor o igual a 999 el 100% de lo solicitado 
    #mensaje="Puntaje registrado"
        messages.warning(request, mensaje)

         #####################################################
    # para guardar en la lista de chequeo 
    lchequo= listaChequeo.objects.get(ids=idpr)
    lchequo.infdicom ="Si"
    lchequo.save()
    return render(request, "HistorialApp/regisRangoCli.html")



def listaPerfil(request): 
    listper=Perfil.objects.filter(estado="activo")
    return render(request, "HistorialApp/listaHis.html", {"perfil":listper})

# Editar puntaje
def listaPunCli(request):
    listaRanC=RegHis.objects.all()
    return render(request, "HistorialApp/listaPuntaje.html", {"puntaje":listaRanC})

def editarPuntCli(request, idpCli):
    punC = RegHis.objects.get(id=idpCli)
    #falta sacar el rango 
    #dire = Agencia.objects.only('municipio','direccion','telefono','telefono2')
    try:
        listarDepto=Departamento.objects.all()
    except Departamento.DoesNotExist:
        listarDepto=""  
    try:
        rango = RangoHis.objects.all()
    except RangoHis.DoesNotExist:
        rango=""

     # Convertir la lista a JSON
    rango_json = json.dumps(list(rango.values()), default=str)  


    return render(request, "HistorialApp/editRangoCli.html", {"punC":punC, "rango_json": rango_json})

def modificarPuntajeC(request):
    
    idpu=request.POST['idp']
    idh=request.POST['idh']
    puntaje=request.POST['punt']
    
    idpr=solicitud.objects.get(id= idpu)
    idpr.id=idpu
    ranh=RangoHis.objects.get(id=idh)
    puntC=RegHis.objects.get(id=idpu)
    if puntC.idsolicitud.tipo=='micro':
        eva= Balancesm.objects.get(idp=puntC.idsolicitud.perfil.id)
        
    else:
        eva=Egresosf.objects.get(idp=puntC.idsolicitud.perfil.id)
    #Validar que si el rango guardado es menor a 400 debe modificar el estado de la solicitud, perfil y evaluacion
    if(puntC.idRango.porcentaje==0 and ranh.porcentaje>0):
        puntC.idsolicitud.observaciones='NULL'
        puntC.idsolicitud.estadosoli=3
        puntC.save()
        puntC.idsolicitud.perfil.estadosoli=10
        puntC.idsolicitud.perfil.save()
        eva.estado=1
        eva.save()
        puntC.puntaje=puntaje
        puntC.idRango=ranh
        puntC.save()
        
        mensaje="Puntaje DICOM actualizado"
        registroBit(request, "Se actualizó puntaje DICOM del cliente " + puntC.idsolicitud.perfil.dui, "Actualización")

    elif (puntC.idRango.porcentaje>0 and ranh.porcentaje==0):
        puntC.idsolicitud.observaciones='Su puntaje de DICOM no aplica para financiamiento'
        puntC.idsolicitud.estadosoli=3
        puntC.save()
        puntC.idsolicitud.perfil.estadosoli=10
        puntC.idsolicitud.perfil.save()
        eva.estado=2
        eva.save()
        puntC.puntaje=puntaje
        puntC.idRango=ranh
        puntC.save()
        mensaje="Puntaje DICOM actualizado. Puntaje no aplica para credito"
        registroBit(request, "Se actualizó puntaje DICOM del cliente " + puntC.idsolicitud.perfil.dui + " No aplica para credito", "Actualización")
    else:# Si el porcentaje es mayor a 0 la solicitud no es denegada y sigue su proceso
           
        puntC.puntaje=puntaje
        puntC.idRango=ranh
        puntC.save()
        puntC.idsolicitud.perfil.estadosoli=10
        puntC.idsolicitud.perfil.save()
        mensaje="Datos actualizados"
        registroBit(request, "Se actualizó puntaje DICOM del cliente " + puntC.idsolicitud.perfil.dui, "Actualización")
    messages.success(request, mensaje)
    return redirect('listapuntaje')


def con(request):
    dire = Agencia.objects.only('municipio','direccion')
    return render(request,"ConfiguracionApp/consulta.html",{"dire":dire})  

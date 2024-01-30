import json
from cProfile import label
from cgitb import html
from email import message
from pyexpat import model
from time import strftime, strptime
from django.contrib.auth.hashers import make_password, check_password
from django.core.serializers import serialize
from django.shortcuts import render,redirect, HttpResponse
from ClienteApp.models import *
from ConozcaClienteApp.models import Clientedg
from ConfiguracionApp.models import Ocupacion, Salario
from DeclaracionJurClienteApp.models import Declaracionjc
from ListaChequeoApp.models import listaChequeo
from PresupuestoApp.models import Presupuestodg
from SolicitudInscripcionSApp.models import Solicitudis
from PresupuestoVApp.models import Presupuestovdg, Presupuestovdgobra
from ReviApp.models import DocumentosCliente
from InspeccionLoteApp.models import Inspeccionl, pInspeccionl
from InspeccionMejViviendaApp.models import InspeccionM, pInspeccionm
from datetime import date, datetime
from HistorialApp.models import RegHis

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
#from UsuarioApp.serializers import UsuarioSerializers
#from rest_framework.parsers import JSONParser
from SolicitudesApp.models import DatosPersonalesF, solicitud as sol, detalle
from EvaluacionMicroApp.models import *
from EvaluacionIvEFApp.models import Egresosf
from django.http.response import JsonResponse
from django.contrib import messages
from DireccionApp.models import *
from TesisApp.models import *
from django.db.models import Q

from TesisApp.views import registroBit

def perfil(request):
    try:
        listao=Ocupacion.objects.filter(estado="activo")
    except Ocupacion.DoesNotExist:
        listao=""

    try:
        listarDepto=Departamento.objects.all()
    except Departamento.DoesNotExist:
        listarDepto=""   
    
    try:
        lper = Perfil.objects.all()
    except Perfil.DoesNotExist:
        lper=""

     # Convertir la lista a JSON
    lper_json = json.dumps(list(lper.values()), default=str)  

    return render(request,"ClienteApp/perfil.html", {"ocupaciones":listao,"Departamento":listarDepto, "lper_json": lper_json})

def perfilc(request):
    listao=Ocupacion.objects.all()
    listarDepto=Departamento.objects.all()
    return render(request,"ClienteApp/perfilc.html", {"ocupaciones":listao,"Departamento":listarDepto})

def registrarPerfil(request): 
  
    nombres=request.POST['nombres']
    apellidos=request.POST['apellidos']
    dui=request.POST['dui']
    telefono=request.POST['telefono']
    nacionalidad=request.POST['nacionalidad']
    fecha=request.POST['fecha']
    ocu =request.POST['ocupacion']
    salario=request.POST['salario']
    distrito=request.POST['distrito']
    direccion=request.POST['direccion']
    correo =request.POST['correo']
    contrasena=request.POST['contrasena']
    rcontrasena=request.POST['rcontrasena']
    estadosoli=1


    fe= datetime.strptime(fecha, '%Y-%m-%d')
    anio= fe.year
    mes =fe.month
    dia= fe.day

    anioa= date.today().year
    mesa= date.today().month
    diaa= date.today().day

    ed= anioa - anio

    edad= ed

    if anio >= anioa:
        mensaje="ingrese un año valido"
        messages.warning(request, mensaje)
        return redirect('/ClienteApp/')
    elif mes >= mesa  and dia > diaa:
        edad= ed-1
    else:
        edad= ed

    
    sal=float(salario)
    ls=Salario.objects.filter(estado="activo")
    des=""
    for sala in ls:
        if sal>= sala.salariominimo and sal<=sala.salariomaximo:
            min= sala.salariominimo
            max=sala.salariomaximo
            des=sala.tiposalario
            break
        else:
            des=""

    idocu=Ocupacion.objects.get(id=ocu)
    idocu.id=ocu
    #depto=Departamento.objects.get(id=departamento)
    #depto.id=departamento
    #muni=Muni.objects.get(idmuni=municipio)
    
    muni=Distrito.objects.get(id=distrito)
    muni_zona=muni.id

    #########agreagado para guardar a que zona pertenece el cliente
    zona=Zona.objects.get(distri=muni_zona)
    zona.distri=muni
    zo=zona.zona.agencia
    #print(zo)
    #############################
    

    du=Perfil.objects.filter(dui=dui).exists()
    if du == True:
        mensaje="Usted ya esta registrado"
        messages.warning(request, mensaje)
        return redirect( '/')

    elif des=="" :
        observacion="Salario fuera de los rangos establecidos"
        perfilna=Perfilna.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fecha=fecha,edad=edad,salario=sal,Agencia=zo,observaciones=observacion)
        mensaje="Lo sentimos, su solicitud no puede ser aceptada ya que no cumple los requisitos de salario"
        messages.error(request, mensaje)
        return redirect('perfil')
    elif nacionalidad!="salvadoreño" :
        observacion="Nacionalidad no aceptada"
        perfilna=Perfilna.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fecha=fecha,edad=edad,salario=sal,Agencia=zo,observaciones=observacion)
        mensaje="Lo sentimos, su solicitud no puede ser aceptada ya que la nacionalidad no es aceptada"
        messages.error(request, mensaje)
        return redirect('perfil')
    elif edad< 18 or edad > 65:
        observacion="Edad fuera del rango establecido"
        perfilna=Perfilna.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fecha=fecha,edad=edad,salario=sal,Agencia=zo,observaciones=observacion)
        mensaje="Lo sentimos, su solicitud no puede ser aceptada ya que la edad no es aceptada"
        messages.error(request, mensaje)
        return redirect('perfil')
    else:
        esta="activo"
        cont = make_password(contrasena)
        rcont = make_password(rcontrasena)
        test_str=correo
        username=test_str.split('@')[0]
        perfil=Perfil.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fechan=fecha,edad=edad,idocu=idocu,salario=sal,municipio=muni,direccion=direccion,correo=correo,contrasena=cont,rcontrasena=rcont,estado=esta,Agencia=zo,estadosoli=estadosoli)
        registroBit(request, "Registro de perfil" + nombres + " " + apellidos + " DUI " + dui, "Registro")
        ####### Registrar cliente para que pueda iniciar sesion
        
        login=Usuario.objects.create(username=username, nombre=nombres,apellido=apellidos, cargo=3, email=correo, password=cont, agencia=zo)
        mensaje="Datos guardados"
        messages.success(request, mensaje)

        return redirect('perfil')


def eliminar(request, id):
    es="inactivo"
    
    per=sol.objects.filter(perfil=id).exists()
    
    if(per!=True):
        perfil=  Perfil.objects.get(id=id)
   # perfil.delete()
   
        perfil.estado=es
        perfil.save()
        mensaje="Perfil eliminado"
        messages.success(request, mensaje)
    else:
        mensaje="El perfil tiene solicitud en proceso"
        messages.error(request, mensaje)
    
    return redirect('/ClienteApp/listaPerfil')

#def conozcac(request, id):
#    idc=id
#    return redirect('/ConozcaClienteApp/cclientedg', {"id":idc})

def editarPerfil(request, id):
    perfil = Perfil.objects.get(id=id)    
    ocupaciones = Ocupacion.objects.all()
    listarDepto=Departamento.objects.all()
    listarMuni=Muni.objects.filter(depto=perfil.municipio.muni.depto)
    listarDist=Distrito.objects.filter(muni=perfil.municipio.muni.idmuni)
    # nombres 
    Deptop=Departamento.objects.get(id=perfil.municipio.muni.depto.id)
    Munip=Muni.objects.get(idmuni=perfil.municipio.muni.idmuni)
    Distp=Distrito.objects.get(id=perfil.municipio.id)

    try:
        lper = Perfil.objects.all()
    except Perfil.DoesNotExist:
        lper=""

     # Convertir la lista a JSON
    lper_json = json.dumps(list(lper.values()), default=str)  

    return render(request, "ClienteApp/editarperfil.html", {"perfil":perfil,"ocupaciones":ocupaciones,"Departamento":listarDepto,"Municipios":listarMuni,"Distritos":listarDist,"Deptop":Deptop,"Munip":Munip,"Distp":Distp, "lper_json": lper_json})


def modificarPerfil(request):
    idp=request.POST['idp']
    nombres=request.POST['nombres']
    apellidos=request.POST['apellidos']
    dui=request.POST['dui']
    telefono=request.POST['telefono']
    nacionalidad=request.POST['nacionalidad']
    fecha=request.POST['fecha']
    ocu =request.POST['ocupacion']
    salario=request.POST['salario']
    distrito=request.POST['distrito']
    direccion=request.POST['direccion']
    correo =request.POST['correo']

    fe= datetime.strptime(fecha, '%Y-%m-%d')
    anio= fe.year
    mes =fe.month
    dia= fe.day

    anioa= date.today().year
    mesa= date.today().month
    diaa= date.today().day

    ed= anioa - anio

    edad= ed

    if anio >= anioa:
        mensaje="ingrese un año valido"
        messages.warning(request, mensaje)
        return redirect('/ClienteApp/')
    elif mes >= mesa  and dia > diaa:
        edad= ed-1
    else:
        edad= ed

    
    sal=float(salario)
    ls=Salario.objects.filter(estado="activo")
    des=""
    for sala in ls:
        if sal> sala.salariominimo and sal<sala.salariomaximo:
            min= sala.salariominimo
            max=sala.salariomaximo
            des=sala.tiposalario   
            print(des)
            break
        else:
            des=""
            print(des)
    
    idocu=Ocupacion.objects.get(id=ocu)
    idocu.id=ocu
    
    muni=Distrito.objects.get(id=distrito)
    muni_zona=muni.id

    #########agreagado para guardar a que zona pertenece el cliente
    zona=Zona.objects.get(distri=muni_zona)
    zona.distri=muni
    zo=zona.zona.agencia
    #############################
    
    if des=="" or nacionalidad!="salvadoreño" or edad< 18 or edad > 65:
        print(nacionalidad)
        print(edad)
       
        perfilna=Perfilna.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fecha=fecha,edad=edad,salario=sal)
        mensaje="Lo sentimos, su solicitud no puede ser aceptada"
        messages.error(request, mensaje)
        return redirect('/ClienteApp/listaPerfil/')
    else:
        #esta="activo"
        #cont = make_password(contrasena)
        #rcont = make_password(rcontrasena)
        test_str=correo
        username=test_str.split('@')[0]

        usuario = Perfil.objects.get(id=idp)
        usuario.nombres=nombres
        usuario.apellidos=apellidos
        usuario.telefono=telefono
        usuario.fechan=fecha
        usuario.edad=edad
        usuario.idocu=idocu 
        usuario.salario=salario
        usuario.municipio=muni 
        usuario.direccion=direccion
        usuario.correo=correo
        usuario.Agencia=zo
        usuario.save()

    mensaje="Datos de usuario actualizado "
    registroBit(request, actividad=mensaje + usuario.nombres +" "+ usuario.apellidos, nivel="Actualizacion")
    messages.success(request, mensaje)
    return redirect('administrarPerfil', id=usuario.id)  # id de perfil 



def municipios(request):
    id=request.GET['departamento']
    depto=Departamento.objects.get(id=id)
    depto.id=id
    de=depto.id
    muni=Muni.objects.filter(depto=depto)
    return render(request,"ClienteApp/municipio.html", {"Muni":muni})



def distri(request):    
    idmuni=request.GET['municipio']
    idmuni=Muni.objects.get(idmuni=idmuni)
    destri=Distrito.objects.filter(muni=idmuni)
    print(' paso '+str(destri))
    return render(request,"ClienteApp/distrito.html", {"MuniDistrito":destri})

def municipio(request):
    id=request.GET['departamento']
    depto=Departamento.objects.get(id=id)
    muni=Muni.objects.filter(depto=depto.id)

    return render(request,"ClienteApp/municipio.html", { "muni":muni})


#def listaPerfil(request):
    
#    listper=Perfil.objects.filter(estado="activo")
#    return render(request, "ClienteApp/listaperfil.html", {"perfiles":listper})

#### Listado de perfil por agencia
def listaPerfil(request): 
    listper=Perfil.objects.filter(estado="activo")
    return render(request, "ClienteApp/listaPerfil.html", {"perfil":listper})

def solicitud(request, id):
    perfil = Perfil.objects.get(id=id)
    return render(request, "ClienteApp/solicitud.html", {"Perfil":perfil})

def solicitudmMicroempresa(request, id):
    perfil = Perfil.objects.get(id=id)
    return render(request, "ClienteApp/solicitud.html", {"Perfil":perfil})

def registrarDetalle(request):
    area=request.POST['area']
    id=2021
    tipo=1
    estado=1
    comunidad=request.POST['comunidad']
    
    ocupa=perfildetalle.objects.create(perfil=id,comunidad=comunidad,area=area,tipo=tipo,estado=estado)
    return redirect('/')


#########################################################
def listaClienets(request): 
    listper=Perfil.objects.filter(estado="activo")
    return render(request, "ClienteApp/listaClientes.html", {"perfil":listper})

def administrarPerfil(request, id):
    perfil = Perfil.objects.get(id=id)    
    ocupaciones = Ocupacion.objects.all()
    listarDepto=Departamento.objects.all()
    listarMuni=Muni.objects.filter(depto=perfil.municipio.muni.depto)
    return render(request, "ClienteApp/administracionPerfil.html", {"perfil":perfil,"ocupaciones":ocupaciones,"Departamento":listarDepto,"Municipios":listarMuni})


def consulta_evaliacion_micro(request):    
    id = request.GET['idCliente']  
    listaId=[]
    
    if request.is_ajax():        
        try:            
            balance = Balancesm.objects.get(estado="1",idp=id)           
            egresos= Egresosm.objects.get(idb=balance)
            listaId.append(egresos.id)             
        except Exception:           
            listaId.append("-0") 

        try:
            solicitud=sol.objects.filter(Q(perfil=id) & (Q(estadosoli=1) | Q(estadosoli=2) | Q(estadosoli=4)  | Q(estadosoli=3)) ).latest('fecha') #obtengo la ultima solicitud por fecha 
            listaId.append(solicitud.id)
        except Exception:
           listaId.append("-0") 
        try:
            conosca_cliente=Clientedg.objects.get(ids=solicitud.id)
            listaId.append(conosca_cliente.iddg)
        except Exception:
           listaId.append("-0") 
        try:
            declaracion=Declaracionjc.objects.get(ids=solicitud.id)
            listaId.append(declaracion.iddj)
        except Exception:
           listaId.append("-0") 
        try:
            seguro=Solicitudis.objects.get(ids=solicitud.id)
            listaId.append(seguro.id)
        except Exception:
           listaId.append("-0") 
        try:
            if(solicitud.tipoobra!="vivienda"):
                
                try:
                    inspeccion_mejora=InspeccionM.objects.get(ids=solicitud.id)
                    listaId.append(inspeccion_mejora.id)
                except Exception:
                    listaId.append("-0") 
                try:
                    presupuesto=Presupuestodg.objects.get(ids=solicitud.id)
                    listaId.append(presupuesto.id)
                except Exception:
                    listaId.append("-0") 
                try:
                    primeraInspeccion = pInspeccionm.objects.get(idim = inspeccion_mejora, ninspeccion="PRIMERA")
                    listaId.append(primeraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    segundaInspeccion = pInspeccionm.objects.get(idim = inspeccion_mejora, ninspeccion="SEGUNDA")
                    listaId.append(segundaInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    terceraInspeccion = pInspeccionm.objects.get(idim = inspeccion_mejora, ninspeccion="TERCERA")
                    listaId.append(terceraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                
            else:
                try:
                    inspeccion_lote=Inspeccionl.objects.get(ids=solicitud.id)
                    listaId.append(inspeccion_lote.id)   
                except Exception:
                    listaId.append("-0")  
                try:
                  
                    presupuesto=Presupuestovdg.objects.get(ids=solicitud.id)   
                    listaId.append(presupuesto.id)
                except Exception:
                    listaId.append("-0")             
                try:
                    primeraInspeccion = pInspeccionl.objects.get(idil = inspeccion_lote, ninspeccion="PRIMERA")
                    listaId.append(primeraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    segundaInspeccion = pInspeccionl.objects.get(idil = inspeccion_lote, ninspeccion="SEGUNDA")
                    listaId.append(segundaInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    terceraInspeccion = pInspeccionl.objects.get(idil = inspeccion_lote, ninspeccion="TERCERA")
                    listaId.append(terceraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                
        except Exception:
           listaId.append("-0") 
           listaId.append("-0") 
           listaId.append("-0") 
           listaId.append("-0") 
           listaId.append("-0")
        try:            
            lista_chrequeo=listaChequeo.objects.get(ids=solicitud.id)
            listaId.append(lista_chrequeo.id)
        except Exception:
           listaId.append("-0") 

        try:
            dicom=RegHis.objects.get(idsolicitud=solicitud.id)
            listaId.append(dicom.id)
        except Exception:
           listaId.append("-0") 

        try:
            presupuesto_obras_adicionales=Presupuestovdgobra.objects.get(idpdg = presupuesto.id)
            listaId.append(presupuesto_obras_adicionales.id)
        except Exception:
           listaId.append("-0")
              
        print("micro  "+str(listaId)+" p= "+id)
        serialized_data = json.dumps(listaId, default=str)
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})

def consulta_evaliacion_natural(request):    
    id = request.GET['idCliente']  
    listaId=[]
    
    if request.is_ajax():        
        try:            
            egresosf = Egresosf.objects.get(estado="1",idp=id)   
            listaId.append(egresosf.id)             
        except Exception:           
            listaId.append("-0") 

        try:
            solicitud=sol.objects.filter(Q(perfil=id) & (Q(estadosoli=1) | Q(estadosoli=2) | Q(estadosoli=4)  | Q(estadosoli=3)) ).latest('fecha') #obtengo la ultima solicitud por fecha 
            listaId.append(solicitud.id)
        except Exception:
           listaId.append("-0") 
        try:
            conosca_cliente=Clientedg.objects.get(ids=solicitud.id)
            listaId.append(conosca_cliente.iddg)
        except Exception:
           listaId.append("-0") 
        try:
            declaracion=Declaracionjc.objects.get(ids=solicitud.id)
            listaId.append(declaracion.iddj)
        except Exception:
           listaId.append("-0") 
        try:
            seguro=Solicitudis.objects.get(ids=solicitud.id)
            listaId.append(seguro.id)
        except Exception:
           listaId.append("-0") 
        try:
            if(solicitud.tipoobra!="vivienda"):
                try:
                    inspeccion_mejora=InspeccionM.objects.get(ids=solicitud.id)
                    listaId.append(inspeccion_mejora.id)
                except Exception:
                    listaId.append("-0") 
                try:
                    presupuesto=Presupuestodg.objects.get(ids=solicitud.id)
                    listaId.append(presupuesto.id)
                except Exception:
                    listaId.append("-0") 
                try:
                    primeraInspeccion = pInspeccionm.objects.get(idim = inspeccion_mejora, ninspeccion="PRIMERA")
                    listaId.append(primeraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    segundaInspeccion = pInspeccionm.objects.get(idim = inspeccion_mejora, ninspeccion="SEGUNDA")
                    listaId.append(segundaInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    terceraInspeccion = pInspeccionm.objects.get(idim = inspeccion_mejora, ninspeccion="TERCERA")
                    listaId.append(terceraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                
            else:
                try:
                    inspeccion_lote=Inspeccionl.objects.get(ids=solicitud.id)
                    listaId.append(inspeccion_lote.id)
                except Exception:
                    listaId.append("-0")
                try:
                    presupuesto=Presupuestovdg.objects.get(ids=solicitud.id)
                    listaId.append(presupuesto.id)
                except Exception:
                    listaId.append("-0")
                try:
                    primeraInspeccion = pInspeccionl.objects.get(idil = inspeccion_lote, ninspeccion="PRIMERA")
                    listaId.append(primeraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    segundaInspeccion = pInspeccionl.objects.get(idil = inspeccion_lote, ninspeccion="SEGUNDA")
                    listaId.append(segundaInspeccion.id)
                except Exception:
                    listaId.append("-0")
                try:
                    terceraInspeccion = pInspeccionl.objects.get(idil = inspeccion_lote, ninspeccion="TERCERA")
                    listaId.append(terceraInspeccion.id)
                except Exception:
                    listaId.append("-0")
                
        except Exception:
           listaId.append("-0") 
           listaId.append("-0") 
           listaId.append("-0") 
           listaId.append("-0") 
           listaId.append("-0")
        try:
            lista_chrequeo=listaChequeo.objects.get(ids=solicitud.id)
            listaId.append(lista_chrequeo.id)
        except Exception:
           listaId.append("-0") 

        try:
            dicom=RegHis.objects.get(idsolicitud=solicitud.id)
            listaId.append(dicom.id)
        except Exception:
           listaId.append("-0") 
        
        try:
            presupuesto_obras_adicionales=Presupuestovdgobra.objects.get(idpdg = presupuesto.id)
            listaId.append(presupuesto_obras_adicionales.id)
        except Exception:
           listaId.append("-0")
        
        print("aa  "+str(listaId)+" p= "+id)
        serialized_data = json.dumps(listaId, default=str)
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})


def consulta_tipo_solicitud(request):    
    id = request.GET['idCliente']
    cliente = Perfil.objects.get(id=id)
    solicitud = "-0"
    if request.is_ajax():  
        try:             
            if(cliente.estadosoli==2):
                solicitud=sol()
                solicitud.tipo="micro"
            if(cliente.estadosoli==3):
                solicitud=sol()
                solicitud.tipo="natural" 
            if(cliente.estadosoli >3):                        
                solicitud = sol.objects.filter(Q(perfil=id) & (Q(estadosoli=1) | Q(estadosoli=2) | Q(estadosoli=4) | Q(estadosoli=6) | Q(estadosoli=3)) ).latest('fecha') #obtengo la ultima solicitud por fecha    
                solicitud.id=solicitud.id    
            serialized_data =  serialize("json", [ solicitud])
        except Exception: 
            serialized_data = json.dumps(solicitud, default=str)
       
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})

def obtener_historial(request):
    
    id = request.GET['idCliente']
    historial = []
    try:
        lista_solicitudes = sol.objects.filter(Q(perfil=id) & Q(Q(estadosoli=4) | Q(estadosoli=6) | Q(estadosoli=7) ) )##agrefar 6 y 7
        datos = []
        for item in lista_solicitudes:

            try:
                monto=detalle.objects.get(idSolicitud=item.id).monto
            except Exception:
                monto=0.00

            datos.append({'id': item.id, 'monto': monto, 'fecha': item.fecha, 'estado': item.estadosoli, 'tipo': item.tipo, 
                          'tipoObra': item.tipoobra, 'numero': item.numero})
        historial = json.dumps(datos, default=str)
        if(historial=="[]"):
            historial="-0"
    except Exception:
        historial = "-0"

    serialized_data = json.dumps(historial, default=str)
    return HttpResponse(serialized_data, content_type="application/json")

def completar_solicitud(request):
    id_cliente = request.GET['idCliente']
    completa = 'si'
    try:
        solicitud = sol.objects.filter(Q(perfil=id_cliente) & (Q(estadosoli=4) | Q(estadosoli=6) | Q(estadosoli=3)) ).latest('fecha') #obtengo la ultima solicitud por fecha   

        if(solicitud.tipo=="micro"):
            try:         
                balance = Balancesm.objects.get(estado="1",idp=id_cliente)           
                egresos= Egresosm.objects.get(idb=balance)
            except Exception:
                completa = completa+"evaluacion,"
        else:
            try:            
                egresosf = Egresosf.objects.get(estado="1",idp=id_cliente)   
                       
            except Exception:           
                ompleta = completa+"evaluacion,"

        try:
            conosca_cliente=Clientedg.objects.get(ids=solicitud.id)
        except Exception:
           completa = completa+"Conozca a su cliente,"

        try:
            declaracion=Declaracionjc.objects.get(ids=solicitud.id)            
        except Exception:
            completa = completa+"Declaracion jurada,"

        try:
            seguro=Solicitudis.objects.get(ids=solicitud.id)            
        except Exception:
           completa = completa+"Inscripcion de seguro,"

        if(solicitud.tipoobra!="vivienda"):
                try:
                    inspeccion_mejora=InspeccionM.objects.get(ids=solicitud.id)
                except Exception:
                    completa = completa+"Inspeccion mejora,"
                try:
                    presupuesto=Presupuestodg.objects.get(ids=solicitud.id)
                    
                except Exception:
                    completa = completa+"Presupuesto,"
        else:                        
                try:
                   inspeccion_lote=Inspeccionl.objects.get(ids=solicitud.id)
                    
                except Exception:
                    completa = completa+"Inspeccion vivienda,"
              
                try:
                    presupuesto=Presupuestovdg.objects.get(ids=solicitud.id)
                except Exception:
                    completa = completa+"Presupuesto,"

        try:
            lista_chrequeo=listaChequeo.objects.get(ids=solicitud.id, estado="completo")
             
        except Exception:
           completa =completa+"Lista de Chequeo"

        try:
            dicom=RegHis.objects.get(idsolicitud=solicitud.id)
            
        except Exception:
           completa = completa+"DICOM"

        if (solicitud.estadosoli == 3):
            completa = "Completada"
    except Exception:
        completa="-0"

   
    
    serialized_data = json.dumps(completa, default=str)
    return HttpResponse(serialized_data, content_type="application/json")

def consultar_documentos(id):
    completa = "si"

    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="fotocdui")
    except Exception:
        completa="DUI"  
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="aguaDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="luzDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="constanciaEmpDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="duifDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="aguafDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="luzfDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="constEmpDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="referenciasCreDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="referenciasCrefDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="certificacionEstracDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="fotocopiaEscritDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = DocumentosCliente.objects.get(ids=id, nombreD="informeDICOMDoc")
    except Exception:
        completa="DUI" 
    try:        
        doc = listaChequeo.objects.get(ids=id, estado="completo")
    except Exception:
        completa="Lista chequeo incompleta" 


    return completa  

def completar_solicitud_base(request):
    id = request.GET['idCliente']
    bandera="si"
    try:
        perfil = Perfil.objects.get(id= id)
        perfil.estadosoli=11
        perfil.save()

        solicitud = sol.objects.filter(Q(perfil=id) & (Q(estadosoli=4) | Q(estadosoli=6) | Q(estadosoli=3)) ).latest('fecha') #obtengo la ultima solicitud por fecha  
        solicitud.estadosoli=3
        solicitud.save()
    except Exception: 
     bandera="-0"
    
    serialized_data = json.dumps(bandera, default=str)
    return HttpResponse(serialized_data, content_type="application/json")

def denegar_solicitud(request):
    id = request.GET['idSoli']
    bandera="si"
    try:       
        
        solicitud = sol.objects.get(id = id) #obtengo la ultima solicitud por fecha  
        solicitud.estadosoli=6
        solicitud.observaciones="La solicitud no se completo en el plazo de 30 dias"
        solicitud.save()

        perfil = Perfil.objects.get(id= solicitud.perfil.id)
        #perfil.estadosoli=1
        #perfil.save()

        if(solicitud.tipo == "micro"):                       
            balance = Balancesm.objects.get(estado="1",idp=perfil.id)           
            balance.estado=2
            balance.save()    
                
        else:
            egresosf = Egresosf.objects.get(estado="1",idp=perfil.id)   
            egresosf.estado=2
            egresosf.save()

        
    except Exception: 
     bandera="-0"
    
    serialized_data = json.dumps(bandera, default=str)
    return HttpResponse(serialized_data, content_type="application/json")

def Registrar_documento(request):    
    id = request.GET['idCliente']
    fecha = request.GET['fecha']
    if 'archivo' in request.FILES:
        archivo = request.FILES['archivo']
    else:
        archivo = None 

    nombreD = request.GET['nombreD']
    ids = request.GET['ids']

    idsoli=sol.objects.get(id=ids, perfil=id)
    print(str(idsoli))
    print(nombreD)
    bandera= "paso"
      
    if request.is_ajax():     
        
        try:  
            documento, creado = DocumentosCliente.objects.update_or_create(nombreD=nombreD,ids=idsoli, defaults={
                "fecha":fecha,
                "archivo":archivo,
                "nombreD":nombreD,
                "ids":idsoli
            }) 
        
            if creado:
                
                registroBit(request, actividad="Se guardo archivo "+nombreD, nivel="Registro")
            else:
                registroBit(request, actividad="Se guardo archivo "+nombreD, nivel="Actualizacion")
            ##############################
            # para guardar en la lista de chequeo  
            
            try:
                doc=DocumentosCliente.objects.filter(ids=idsoli)  
            except:
                doc=''
            #refe= DatosPersonalesF.objects.get(idSolicitud=idsoli, tipo='codeudor').exists()
            try:
                codeudor =  DatosPersonalesF.objects.get(idSolicitud=idsoli, tipo='codeudor')
                # Tu código para manejar el caso en que el codeudor existe
                codeudor=True
            except DatosPersonalesF.DoesNotExist:
                codeudor=False
            #print(codeudor)
            duic=0
            rec=0
            ref=0
            print("refe"+ str(codeudor))
            for d in doc: 
                             
                if d.nombreD == "duiDoc":
                    print(d.nombreD + ' refe' + str(codeudor)) 
                    duic=1
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.fotocdui ="Si"
                    lchequo.save()
                if d.nombreD == "nitDoc" and duic==1:
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.fotocdui ="Si"
                    lchequo.save()
                
                if d.nombreD == "aguaDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.recibosagua ="Si"
                    lchequo.save()
                    
                if d.nombreD == "luzDoc" :
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.recibosluz ="Si"
                    lchequo.save()

                if d.nombreD == "telDoc" :
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.recibostelef ="Si"
                    lchequo.save()
                
                if d.nombreD == "constanciaEmpDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.constemp ="Si"
                    lchequo.save()
                
                if d.nombreD == "tacoIsssDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.tacoisss ="Si"
                    lchequo.save()
                
                if d.nombreD == "analisisEcNDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.analisisec ="Si"
                    lchequo.save()

                if d.nombreD == "balanceDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.balance ="Si"
                    lchequo.save()
                                
                if d.nombreD == "balanceResDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.balanceres ="Si"
                    lchequo.save()

                if codeudor==True:#Documentos fiador
                    if d.nombreD == "duifDoc" :
                        duif=1
                        lchequo= listaChequeo.objects.get(ids=idsoli)
                        lchequo.copiaduifia ="Si"
                        lchequo.save()
                    if d.nombreD == "nitfDoc" and duif==1:
                        lchequo= listaChequeo.objects.get(ids=idsoli)
                        lchequo.copiaduifia ="Si"
                        lchequo.save()

                    if d.nombreD == "aguafDoc":                      
                        lchequo= listaChequeo.objects.get(ids=idsoli)
                        lchequo.recibosfiaagua ="Si"
                        lchequo.save()

                    if d.nombreD == "luzfDoc":
                        lchequo= listaChequeo.objects.get(ids=idsoli)
                        lchequo.recibosfialuz ="Si"
                        lchequo.save()
     
                    if d.nombreD == "constEmpDoc" or d.nombreD == "analisisEcNDoc":
                        lchequo= listaChequeo.objects.get(ids=idsoli)
                        lchequo.constempfia ="Si"
                        lchequo.save()

                   
                if d.nombreD == "referenciasCreDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.refercs ="Si"
                    lchequo.save()

                if d.nombreD == "referenciasCrefDoc" :
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.refercsfia ="Si"
                    lchequo.save()

                
                if d.nombreD == "inspeccionTecDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.inspecciontec ="Si"
                    lchequo.save()

                if d.nombreD == "presupuestoConsDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.presupuestocons ="Si"
                    lchequo.save()
                
                if d.nombreD == "certificacionEstracDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.certifext ="Si"
                    lchequo.save()
                
                if d.nombreD == "carenciaBienDoc" :
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.carenciabien ="Si"
                    lchequo.save()
                
                if d.nombreD == "fotocopiaEscritDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.fotocescrit ="Si"
                    lchequo.save()
                
                if d.nombreD == "declaracionSalDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.declaracions ="Si"
                    lchequo.save()

                if d.nombreD == "informeDICOMDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.infdicom ="Si"
                    lchequo.save()
                
                if d.nombreD == "documentosSopDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.docsing ="Si"
                    lchequo.save()
                
                if d.nombreD == "documentosRemDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.docrem ="Si"
                    lchequo.save()
                
                if d.nombreD == "cancelacionPresDoc" or d.nombreD == "estadoCuenDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.cancelpec ="Si"
                    lchequo.save()
                
                if d.nombreD == "finiquitosDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.finiquitos ="Si"
                    lchequo.save()

                if d.nombreD == "hojaAprobCredDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.hojaaprovc ="Si"
                    lchequo.save()
                
                if d.nombreD == "cartaElabMutDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.cartaelbmutuo ="Si"
                    lchequo.save()
                
                if d.nombreD == "reciboPagPrimDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.recibpagp ="Si"
                    lchequo.save()
                
                if d.nombreD == "ordenDesIrrevDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.ordendesi ="Si"
                    lchequo.save()
                
                if d.nombreD == "permisoConsDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.permisocons ="Si"
                    lchequo.save()
                
                if d.nombreD == "cartaEntrCostDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.cartaentcd ="Si"
                    lchequo.save()
                
                if d.nombreD == "fotocopiaMutHipDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.fotocmutuo ="Si"
                    lchequo.save()

                if d.nombreD == "gestionesCobrDoc":
                    lchequo= listaChequeo.objects.get(ids=idsoli)
                    lchequo.gestioncobro ="Si"
                    lchequo.save()

            ##### Contador para saber si estan todos los recibos o solo los obligatorios
            """if rec==2:
                lchequo= listaChequeo.objects.get(ids=idsoli)
                lchequo.recibos ="Si"
                lchequo.save()
            elif rec==5:
                lchequo= listaChequeo.objects.get(ids=idsoli)
                lchequo.recibos ="Si"
                lchequo.save()"""

            clistaCq= listaChequeo.objects.get(ids=idsoli)
            if clistaCq.solicitudc=="Si" and  clistaCq.fotocdui=="Si" and  clistaCq.recibosagua=="Si" and  clistaCq.recibosluz=="Si"  and clistaCq.constemp=="Si" or clistaCq.analisisec=="Si"  or  clistaCq.balance=="Si" or  clistaCq.balanceres=="Si" and  clistaCq.copiaduifia=="Si" and  clistaCq.recibosfiaagua=="Si" and  clistaCq.recibosfialuz=="Si" and  clistaCq.constempfia=="Si" and  clistaCq.refercsfia=="Si" and  clistaCq.inspecciontec=="Si" and  clistaCq.presupuestocons=="Si" and  clistaCq.certifext=="Si" and  clistaCq.fotocescrit=="Si" and  clistaCq.declaracions=="Si" and  clistaCq.infdicom=="Si" :
                clistaCq.estado="completo"
                clistaCq.save()

                    
            serialized_data = json.dumps(bandera, default=str)
        except Exception:           
            bandera = "-0"
            serialized_data = json.dumps(bandera, default=str)
       
        return HttpResponse(serialized_data, content_type="application/json")
    else:
        listam = Materiales.objects.filter(estado="activo")
        return render(request, "PresupuestoApp/presupuesto.html", {"materiales": listam})
    

#########################################################
# Listado de perfil que no aplican
def listaPerfilNA(request): 
    listper=Perfilna.objects.all()
    return render(request, "ClienteApp/listaPerfilNA.html", {"perfil":listper})
    
   
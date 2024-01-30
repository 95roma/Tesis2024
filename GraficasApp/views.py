import json
from django.db.models.functions import Coalesce
from django.shortcuts import render,redirect
from ClienteApp.models import *
from NaturalApp.models import *
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
# from django.template import loader
from django.template.loader import get_template
from django.db.models import Count
from django.http import JsonResponse
from django.db.models.functions import TruncDate
from django.views.generic import TemplateView
from django.db.models import Count
from django.db.models.functions import ExtractMonth

from django.db.models import Sum
from django.http import JsonResponse

from SolicitudesApp.models import *

# Create your views here.
def per(request):
    
    #mescon=request.GET['id', False]
    agenciaç=1
    perfil=Perfil.objects.filter(Agencia=agenciaç).count()
   # per=Perfil.objects.filter(fecharegistro='2023-02-23').count()
    data=[]
    mo=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    try:
        
         year=datetime.now().year
         for m in range(1,13):
            total= Perfil.objects.filter(fechaR__year=year,fechaR__month=m).aggregate(r=Coalesce(Count('id'),0)).get('r')
            data.append(total)
            mo[m]=total        
    except:
        pass
    en=mo[1]
    fe=mo[2]
    mar=mo[3]
    abri=mo[4]
    may=mo[5]
    jun=mo[6]
    jul=mo[7]
    ago=mo[8]
    sep=mo[9]
    oct=mo[10]
    nov=mo[11]
    dic=mo[12]
    cantidad=perfil
    ####aqui es para los perfiles por dia ingresados en un mes
   
    dia=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
 
    try:
         #mescon=request.GET['id']
         year=datetime.now().year
         for m in range(1,32):
           to= Perfil.objects.filter(fechaR__day=m,fechaR__month=3).aggregate(r=Coalesce(Count('id'),0)).get('r')
           dia[m]=to   
    except:
        pass
    d1=dia[1]
    d2=dia[2]
    d3=dia[3]
    d4=dia[4]
    d5=dia[5]
    d6=dia[6]
    d7=dia[7]
    d8=dia[8]
    d9=dia[9]
    d10=dia[10]
    d11=dia[11]
    d12=dia[12]
    d13=dia[13]
    d14=dia[14]
    d15=dia[15]
    d16=dia[16]
    d17=dia[17]
    d18=dia[18]
    d19=dia[19]
    d20=dia[20]
    d21=dia[21]
    d22=dia[22]
    d23=dia[23]
    d24=dia[24]
    d25=dia[25]
    d26=dia[26]
    d27=dia[27]
    d28=dia[28]
    d29=dia[29]
    d30=dia[30]
    d31=dia[31]
    print(d1)
    registros = Perfil.objects.annotate(
        fechadia=TruncDate('fechaR')).values('fechadia').annotate(num_registros=Count('id'))
       #fecha dia es variable para la fechaR 
    for r in registros:
     
     fecha=r['fechadia']
     suma=r['num_registros']
     print(fecha,suma)
    

    context={
        'cantidad':cantidad,# aqui mandaamos la variable que necesitamos
        'en':en,'fe':fe,'mar':mar,'abri':abri,'may':may,'jun':jun,'jul':jul,'ago':ago,
        'sep':sep,'oct':oct,'nov':nov,'dic':dic,
        'fecha':fecha,
        'd1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'d7':d7,'d8':d8,'d9':d9,'d10':d10,
        'd11':d11,'d12':d12,'d13':d13,'d14':d14,'d15':d15,'d16':d16,'d17':d17,'d18':d18,'d19':d19,'d20':d20,
        'd21':d21,'d22':d22,'d23':d23,'d24':d24,'d25':d25,'d26':d26,'d27':d27,'d28':d28,'d29':d29,'d30':d30,
        'd31':d31

    } #Context(cantidad)
    #documento=template.render(contexto)
    
    return render(request, "GraficasApp/per.html", context)

def Gporyear(request):
   labels = []
   data=[]
   mo=[1,2,3,4,5,6,7,8,9,10,11,12,13]
   try:
         #fechai=request.POST['fechai']
         #fechaf=request.POST['fechaf']
         year=datetime.now().year
         for m in range(1,13):
            total= Perfil.objects.filter(fechaR__year=year,fechaR__month=m).aggregate(r=Coalesce(Count('id'),0)).get('r')
            #data.append(int(total))
            mo[m]=total 
            data=mo[m]
            print("--",data) 
            print("eee",mo[m])       
   except:
        pass
   en=mo[1]
   fe=mo[2]
   mar=mo[3]
   abri=mo[4]
   may=mo[5]
   jun=mo[6]
   jul=mo[7]
   ago=mo[8]
   sep=mo[9]
   oct=mo[10]
   nov=mo[11]
   dic=mo[12]
   return render(request, "GraficasApp/Gporyear.html", {'en': en,'fe':fe,'mar':mar,
    'abri':abri,'may':may,'jun':jun,'jul':jul,'ago':ago,'sep':sep,'oct':oct,'nov':nov,'dic':dic})


def prueba(request):
   return render(request, "GraficasApp/prueba.html")

class DashboardView(TemplateView):
    template_name='GraficasApp/prueba.html'
    def get_meses(self):
        data=[]
        year=datetime.now().year
        try: 
         for m in range(1,13):
            total= Perfil.objects.filter(fechaR__year=year,fechaR__month=m).aggregate(r=Coalesce(Count('id'),0)).get('r')
            data.append(int(total))           
        except:
          pass
        return data
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['panel']='Panel de administrador'
        context['meses']=self.get_meses()
        return context
    
def graf1(request):
    labels = []
    data=[]
    mo=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    try:
            year=datetime.now().year
            for m in range(1,13):
                total= "" #DetalleApp.objects.filter(fecharegistro__year=year,fecharegistro__month=m).aggregate(r=Coalesce(Count('id'),0)).get('r')
                #data.append(int(total))
                mo[m]=total 
                data=mo[m]
                print("--",data) 
                print("eee",mo[m])       
    except:
            pass
    en=mo[1]
    fe=mo[2]
    mar=mo[3]
    abri=mo[4]
    may=mo[5]
    jun=mo[6]
    jul=mo[7]
    ago=mo[8]
    sep=mo[9]
    oct=mo[10]
    nov=mo[11]
    dic=mo[12]
    
    return render(request, "GraficasApp/graf1.html",{'en': en,'fe':fe,'mar':mar,
    'abri':abri,'may':may,'jun':jun,'jul':jul,'ago':ago,'sep':sep,'oct':oct,'nov':nov,'dic':dic})
"""def population_chart(request):
    labels = []
    data = []
    data=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    year=datetime.now().year
    queryset =  Perfil.objects.filter(fechaR__year=year,fechaR__month=data).aggregate(r=Coalesce(Count('id'),0)).get('r')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })"""

def graf2(request):
    labels = []
    data=[]
    mo=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    try:
            year=datetime.now().year
            for m in range(1,13):
                total= solicitud.objects.filter(fecha__year=year,fecha__month=m).aggregate(r=Coalesce(Count('id'),0)).get('r')
                #data.append(int(total))
                mo[m]=total 
                data=mo[m]
                print("--",data) 
                print("eee",mo[m])       
    except:
            pass
    en=mo[1]
    fe=mo[2]
    mar=mo[3]
    abri=mo[4]
    may=mo[5]
    jun=mo[6]
    jul=mo[7]
    ago=mo[8]
    sep=mo[9]
    oct=mo[10]
    nov=mo[11]
    dic=mo[12]
    
    return render(request, "GraficasApp/graf2.html",{'en': en,'fe':fe,'mar':mar,
    'abri':abri,'may':may,'jun':jun,'jul':jul,'ago':ago,'sep':sep,'oct':oct,'nov':nov,'dic':dic})

def graficaAT(request):    # grafica de solicitudes por agencia y tipo de solicitud(mejora,vivienda)
    agencia_seleccionada = None
    tipo_obra_seleccionado = None

    agencias = Agencia.objects.all()
    tipos_obra = list(solicitud.objects.values('tipoobra').distinct())

    # Definir las variables con valores predeterminados
    solicitudes_por_mes_json = []

    if request.method == 'POST':
        agencia_id = request.POST.get('agencia')
        tipo_obra = request.POST.get('tipo_obra')

        if agencia_id and tipo_obra:
            tipo_obra_seleccionado = tipo_obra           
            agencia_seleccionada = Agencia.objects.get(pk=agencia_id)

            solicitudes = solicitud.objects.filter(tipoobra=tipo_obra_seleccionado,perfil__Agencia=agencia_seleccionada)
            perfiles = Perfil.objects.filter(Agencia=agencia_seleccionada)
            
            # Anota las solicitudes por mes
            solicitudes_por_mes = solicitudes.annotate(mes=ExtractMonth('fecha')).values('mes').annotate(cantidad=Count('id'))
            solicitudes_por_mes_json = json.dumps(list(solicitudes_por_mes))
            # Esto te dará una lista de diccionarios, donde cada diccionario tiene 'mes' y 'cantidad'
            print(solicitudes_por_mes)
        

    return render(request, "GraficasApp/grafAgenciaTipo.html", {
        'agencias': agencias,
        'tipos_obra': tipos_obra,
        'solicitudes_por_mes': solicitudes_por_mes_json  # Datos de gráfico para tipo de obra
    })

def graficaATS(request):    # grafica de solicitudes por agencia y tipo de solicitud(micro,personal)
    agencia_seleccionada = None
    tipo_sol_seleccionado = None

    agencias = Agencia.objects.all()

    # Definir las variables con valores predeterminados
    solicitudes_por_mes_json = []

    if request.method == 'POST':
        agencia_id = request.POST.get('agencia')
        tipo_sol = request.POST.get('tipo_sol')

        if agencia_id and tipo_sol:
            tipo_sol_seleccionado = tipo_sol           
            agencia_seleccionada = Agencia.objects.get(pk=agencia_id)

            solicitudes = solicitud.objects.filter(tipo=tipo_sol_seleccionado,perfil__Agencia=agencia_seleccionada)
            perfiles = Perfil.objects.filter(Agencia=agencia_seleccionada)
            
            # Anota las solicitudes por mes
            solicitudes_por_mes = solicitudes.annotate(mes=ExtractMonth('fecha')).values('mes').annotate(cantidad=Count('id'))
            solicitudes_por_mes_json = json.dumps(list(solicitudes_por_mes))
            # Esto te dará una lista de diccionarios, donde cada diccionario tiene 'mes' y 'cantidad'
            print(solicitudes_por_mes)
        

    return render(request, "GraficasApp/grafAgenciaTipoSol.html", {
        'agencias': agencias,
        'solicitudes_por_mes': solicitudes_por_mes_json  # Datos de gráfico para tipo de obra
    })

def graficaASolic(request):    # grafica de solicitudes aprobadas, denegadas, observadas y vencidas
    agencia_seleccionada = None
    tipo_sol_seleccionado = None

    agencias = Agencia.objects.all()

    # Definir las variables con valores predeterminados
    solicitudes_por_mes_json = []

    if request.method == 'POST':
        agencia_id = request.POST.get('agencia')
        tipo_sol = request.POST.get('tipo_sol')

        if agencia_id and tipo_sol:
            tipo_sol_seleccionado = tipo_sol           
            agencia_seleccionada = Agencia.objects.get(pk=agencia_id)

            solicitudes = solicitud.objects.filter(estadosoli=tipo_sol_seleccionado,perfil__Agencia=agencia_seleccionada)
            perfiles = Perfil.objects.filter(Agencia=agencia_seleccionada)
            
            # Anota las solicitudes por mes
            solicitudes_por_mes = solicitudes.annotate(mes=ExtractMonth('fecha')).values('mes').annotate(cantidad=Count('id'))
            solicitudes_por_mes_json = json.dumps(list(solicitudes_por_mes))
            # Esto te dará una lista de diccionarios, donde cada diccionario tiene 'mes' y 'cantidad'
            print(solicitudes_por_mes)
        

    return render(request, "GraficasApp/grafAgenciaSolic.html", {
        'agencias': agencias,
        'solicitudes_por_mes': solicitudes_por_mes_json  # Datos de gráfico para tipo de obra
    })



def graficaM1(request):
    # Consulta para contar la cantidad de perfiles por edad
    data = Perfil.objects.values('edad').annotate(total=Count('edad')).order_by('edad')

    # Convierte los datos en formato JSON
    data_json = list(data)  # Convierte el queryset en una lista de diccionarios

     # Redirige al usuario a la página HTML deseada usando JavaScript
    response_data = {
        'data_json': data_json,
        'redirect_url': '/GraficasApp/grafM/',  # Define la URL de redirección
    }

    return JsonResponse(response_data)
    #return JsonResponse(data_json, safe=False)
    #return render(request, "GraficasApp/grafM.html", {"data_json":data_json})


def grafTipoSol(request):

    # Realiza una consulta para obtener los distintos valores de tipoobra
    tipos_obra = solicitud.objects.values('tipoobra').distinct()

    if request.method == 'POST':
        tipo_obra = request.POST.get('tipo_obra')

        if tipo_obra:
            # Filtra las solicitudes por el tipo de obra seleccionado
            solicitudes = solicitud.objects.filter(tipoobra=tipo_obra)

            # Anota las solicitudes por mes
            solicitudes_por_mes = solicitudes.annotate(mes=ExtractMonth('fecha')).values('mes').annotate(cantidad=Count('id'))

            solicitudes_por_mes_json = json.dumps(list(solicitudes_por_mes))
            # Esto te dará una lista de diccionarios, donde cada diccionario tiene 'mes' y 'cantidad'
            print(solicitudes_por_mes_json)
        return render(request, "GraficasApp/grafTipoSol.html", {'solicitudes_por_mes': solicitudes_por_mes_json, 'tipos_obra': tipos_obra})
    return render(request, "GraficasApp/grafTipoSol.html", {'tipos_obra': tipos_obra})


def grafAgenciaP(request): # grafica de perfiles por agencias     
        agencia_seleccionada = None
        agencias = Agencia.objects.all()  # Obtén todas las agencias disponibles

        if request.method == 'POST':
            agencia_id = request.POST.get('agencia')
            if agencia_id:
                agencia_seleccionada = Agencia.objects.get(pk=agencia_id)
                perfiles = Perfil.objects.filter(Agencia=agencia_seleccionada)

        # Obtén todos los perfiles de la agencia seleccionada
        perfiles = Perfil.objects.filter(Agencia=agencia_seleccionada)

        # Anota los perfiles por mes
        perfiles_por_mes = perfiles.annotate(mes=ExtractMonth('fechaR')).values('mes').annotate(cantidad=Count('id'))
        # Convierte perfiles_por_mes a JSON
        perfiles_por_mes_json = json.dumps(list(perfiles_por_mes))
        # Esto te dará una lista de diccionarios, donde cada diccionario tiene 'mes' y 'cantidad'
        print(perfiles_por_mes_json)

        return render(request, "GraficasApp/grafAgenciaP.html", {'agencias': agencias, 'perfiles_por_mes':perfiles_por_mes_json})


def grafAgenciaPN(request): # grafica de perfiles por agencias     
        agencia_seleccionada = None
        agencias = Agencia.objects.all()  # Obtén todas las agencias disponibles

        if request.method == 'POST':
            agencia_id = request.POST.get('agencia')
            if agencia_id:
                agencia_seleccionada = Agencia.objects.get(pk=agencia_id)
                perfiles = Perfilna.objects.filter(Agencia=agencia_seleccionada)

        # Obtén todos los perfiles de la agencia seleccionada
        perfiles = Perfilna.objects.filter(Agencia=agencia_seleccionada)

        # Anota los perfiles por mes
        perfiles_por_mes = perfiles.annotate(mes=ExtractMonth('fechaR')).values('mes').annotate(cantidad=Count('id'))
        # Convierte perfiles_por_mes a JSON
        perfiles_por_mes_json = json.dumps(list(perfiles_por_mes))
        # Esto te dará una lista de diccionarios, donde cada diccionario tiene 'mes' y 'cantidad'
        print(perfiles_por_mes_json)

        return render(request, "GraficasApp/grafAgenciaPN.html", {'agencias': agencias, 'perfiles_por_mes':perfiles_por_mes_json})

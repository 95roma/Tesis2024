from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imp
import json
import smtplib
#from inspect import _empty
#from queue import Empty
from telnetlib import LOGOUT
from typing import Any
from urllib import request
import uuid
from django import http
from django.template.loader import render_to_string
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import View
#from django.contrib.auth.forms import UserCreationForm

#from django.contrib.auth import get_user_model
from ConfiguracionApp.models import *
from Tesis import settings
from TesisApp.models import Bitacora
from TesisApp.models import Usuario
#from django.core.files.storage import FileSystemStorage
import pytz
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect, JsonResponse
from TesisApp.forms import FormularioLogin #,FormularioUsuario

from ClienteApp.models import *
from ConfiguracionApp.models import Ocupacion, Salario
from datetime import date, datetime
from DireccionApp.models import *
from TesisApp.reset import ChangePasswordForm, ResetPasswordForm

# Create your views here.
def home(request):
    return render(request, "TesisApp/base.html")
def registroUsuario(request):
    listaragencia=Agencia.objects.all()
    return render(request, "TesisApp/registroUsuario.html",{"Agencia":listaragencia})
def iniciosession(request):
    

    return render(request, "TesisApp/iniciosession.html")

def admin():
    ag=None
    try:
        ag=Agencia.objects.all()
    except:
        ag=None
    print(ag)
    if not ag:
        print("entro")
        agen=Agencia.objects.create(nombre="Agencia", direccion="Central", telefono="0000-0000", telefono2="0000-0000", departamento="central", municipio="central", distrito="central", estado=5)
        print("hola")
        agen=Agencia.objects.get(estado=5)
        cont= make_password("admin")
        usu=Usuario.objects.create(username="admin", nombre="Administrador",apellido="Admin", cargo=1, email="admin@gmial.com", password=cont, agencia=agen)
    
    

def insertar(request):
    
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    contra=request.POST['contra']
    id=request.POST['agencia']
    print(id)
    cargo=request.POST['cargo']
    agencia=Agencia.objects.get(id=id)
    agencia.id=id
    test_str=correo
    username=test_str.split('@')[0]
    cont= make_password(contra)
    usuario=Usuario.objects.create(username=username, nombre=nombre,apellido=apellido, cargo=cargo, email=correo, password=cont, agencia=agencia)
    mensaje="Usuario registrado"
    #registroBit(request, actividad=mensaje, nivel="Registro")
    messages.success(request, mensaje)
    return redirect('/')




#######################################
# perfil
def perfils(request):
    listao=Ocupacion.objects.all()
    listarDepto=Departamento.objects.all()
    return render(request,"TesisApp/perfilS.html", {"ocupaciones":listao,"Departamento":listarDepto})


def rPerfils(request): 
  
    nombres=request.POST['nombres']
    apellidos=request.POST['apellidos']
    dui=request.POST['dui']
    telefono=request.POST['telefono']
    nacionalidad=request.POST['nacionalidad']
    fecha=request.POST['fecha']
    ocu =request.POST['ocupacion']
    salario=request.POST['salario']
    municipio=request.POST['municipio']
    direccion=request.POST['direccion']
    correo =request.POST['correo']
    contrasena=request.POST['contrasena']
    rcontrasena=request.POST['rcontrasena']



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
        messages.success(request, mensaje)
        return redirect('/TesisApp/perfilS')
    elif contrasena != rcontrasena:
        mensaje="Las contraseñas no coinciden"
        messages.success(request, mensaje)
        return redirect('/TesisApp/perfilS')
    elif mes >= mesa  and dia > diaa:
        edad= ed-1
    else:
        edad= ed

    
    sal=float(salario)
    ls=Salario.objects.get(estado="activo")
    min= ls.salariominimo
    max=ls.salariomaximo

    idocu=Ocupacion.objects.get(id=ocu)
    idocu.id=ocu
    #depto=Departamento.objects.get(id=departamento)
    #depto.id=departamento
    muni=Muni.objects.get(idmuni=municipio)
    muni.idmuni=municipio

    #########agreagado para guardar a que zona pertenece el cliente
    zona=Zona.objects.get(municipio=muni)
    zona.municipio=muni
    zo=zona.zona.agencia
    #print(zo)
    #############################


    du=Perfil.objects.filter(dui=dui).exists()
    if du == True:
        mensaje="Usted ya esta registrado"
        messages.warning(request, mensaje)
        return redirect( '/')

    elif sal < min or sal > max or nacionalidad!="salvadoreño" or edad< 18 or edad > 65:
       
        perfilna=Perfilna.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fecha=fecha,edad=edad,salario=salario)
        mensaje="Lo sentimos, su solicitud no puede ser aceptada"
        messages.error(request, mensaje)
        return redirect('/')
    else:
        esta="activo"
        cont = make_password(contrasena)
        rcont = make_password(rcontrasena)
        perfil=Perfil.objects.create(nombres=nombres,apellidos=apellidos,dui=dui,telefono=telefono,nacionalidad=nacionalidad,fechan=fecha,edad=edad,idocu=idocu,salario=salario,municipio=muni,direccion=direccion,correo=correo,contrasena=cont,rcontrasena=rcont,estado=esta,Agencia=zo)
        mensaje="Datos guardados"
        messages.success(request, mensaje)

        return redirect('/')


def municipio(request):
    id=request.GET['departamento']
    depto=Departamento.objects.get(id=id)
    depto.id=id
    de=depto.id
    muni=Muni.objects.filter(depto=depto)
    return render(request,"TesisApp/municipio.html", {"Muni":muni})


class Login(FormView):
    template_name='TesisApp/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')
   
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs): 
        if request.user.is_authenticated:
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            admin()
            return super(Login,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        usuar=Usuario.objects.get(username=self.request.POST['username'])
        print(usuar.agencia.nombre)
        print(usuar.cargo)
        print(form.get_user())
        login(self.request,form.get_user())
        registroBit(self.request, actividad="Inicio sesion", nivel="Login")
        return super(Login,self).form_valid(form)
    
def logoutUsuario(request):
    registroBit(request, actividad="Cierre de sesion", nivel="Logout")
    logout(request)
    
    return HttpResponseRedirect('/accounts/login/')

def registroBit(request, actividad, nivel):
    usua=request.user.iduser
    fechah=datetime.now()
    fecha=fechah.strftime('%Y-%m-%d %H:%M:%S')
    print("fecha: ", fecha)
    usu=Usuario.objects.get(iduser=usua)
    bit=Bitacora.objects.create(fechaHora=fecha, actividad=actividad, nivel=nivel, idusuario=usu)

def listaB(request):
    usua=request.user.iduser
    bit=Bitacora.objects.filter(idusuario=usua).order_by('-fechaHora')
    return render(request, "TesisApp/listarBitacora.html",{"bitacora":bit})
    
def listaBitC(request):
    bit=Bitacora.objects.all()
    
def listaBita(request):
    usua=request.user.iduser
    bit=Bitacora.objects.filter(idusuario=usua)

def fechas(request):
    
    fini=request.GET['ini']
    ffin=request.GET['fin']
    fini=fini+' 00:'+'00:'+'00'
    ffin=ffin+' 23:'+'59:'+'59'
    lista_bit=[]
    
    print("entro")
    if request.is_ajax():
        try:
            bit=Bitacora.objects.filter(fechaHora__gte=fini, fechaHora__lte=ffin)
            #muni=Distrito.objects.filter(muni=id)
            for item in bit:
                lista_bit.append({"id":item.id, "actividad":item.actividad, "fecha":item.fechaHora, "tipo":item.nivel, "usu":item.idusuario})
        except Exception:
            None
            print("pasoo"+str(fini))
        serialized_data = json.dumps(lista_bit,default=str)
        #serialized_data = serialize("safe",[lista_muni])
        return HttpResponse(serialized_data, content_type="application/json")
    
class ResetPasswordView(FormView):
    form_class=ResetPasswordForm
    template_name='TesisApp/resetpwd.html'
    success_url=reverse_lazy('/')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def send_email_reset_pwd(self, user): #Enviar correo
        data={}
        try:
            URL=settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']
            user.token = uuid.uuid4()
            user.save()

            mailServer=smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            print(mailServer.ehlo())
            mailServer.starttls()
            print(mailServer.ehlo())
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            print('conectado...')

            #email_to= 'duranroxa.10@gmail.com'
            email_to=user.email
            #Construimos el mensaje
            mensaje= MIMEMultipart()
            mensaje['From']= settings.EMAIL_HOST_USER
            mensaje['To']= email_to
            mensaje['Subject']= "Cambiar contraseña"

            content= render_to_string('TesisApp/send_email.html', {
                'user': user,
                'link_resetpwd':'http://{}/change/password/{}/'.format(URL, str(user.token)),
                'link_home': 'http://{}'.format(URL)
            })
            mensaje.attach(MIMEText(content, 'html'))
            mailServer.sendmail(settings.EMAIL_HOST_USER,
                                email_to,
                                mensaje.as_string())
            
            print('Correo enviado correctamente')
            #messages.success(request, "Correo enviado correctamente")
        except Exception as e:
            #data['error']=str(e)
            print(e)
            #messages.error(request, str(e))
        return data

    def post(self, request,  *args, **kwargs):
        data={}
        try:
            form=ResetPasswordForm(request.POST) #self.get_form()
            if form.is_valid():
                user= form.get_user()
                #print(self.request.META['HTTP_HOST'])
                data= self.send_email_reset_pwd(user)
                messages.success(request, "Correo enviado correctamente")
            else:
                mensaje=form.errors
                messages.error(request, "Usuario invalido")
                #data['error']=form.errors
                #messages.error(request, data['error'])
                return redirect(reverse_lazy('reset_password'))
            print("Hola entro")
            print(request.POST)
            #return ResetPasswordView(request)
                
        except Exception as e:
            data['error']=str(e)
            JsonResponse(data, safe=False)
            messages.error(request, data['error'])
        return HttpResponseRedirect('/')
        
    def form_valid(self, form):
        pass
        return HttpResponseRedirect(self.success_url)
        #return super().form_valid(form)
        #super(Login,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reseteo de Contraseña"
        return context
            

class ChangePasswordView(FormView):
    form_class=ChangePasswordForm
    template_name='TesisApp/changepwd.html'
    success_url=reverse_lazy('/')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        token= self.kwargs['token']
        if Usuario.objects.filter(token=token).exists():
            print(self.kwargs['token'])
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect('/')
    
    def post(self, request,  *args, **kwargs):
        data={}
        try:
           form= ChangePasswordForm(request.POST)
           if form.is_valid():
               user = Usuario.objects.get(token=self.kwargs['token'])
               user.set_password(request.POST['password'])
               user.token=uuid.uuid4()
               user.save()
               mensaje="Contraseña modificada"
               messages.success(request, mensaje)
               
           else:
               mensaje=form.errors
               messages.error(request, "Contraseña invalida")
               return redirect(reverse_lazy('change_password'))
               #data['error'] = form.errors
        except Exception as e:
            data['error']=str(e)
            JsonResponse(data, safe=False)
            messages.error(request, "Error: Las contraseñas deben ser validas")
            return redirect(reverse_lazy('change_password', kwargs={'token': self.kwargs['token']}))
        return HttpResponseRedirect('/')
           # messages.error(request, str(e))
            #data['error']=str(e)
        #return JsonResponse(data, safe=False)
        
    def form_valid(self, form):
        pass
        return HttpResponseRedirect(self.success_url)
        #return super().form_valid(form)
        #super(Login,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reseteo de Contraseña"
        return context
        

        


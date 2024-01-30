from django.urls import path
from GraficasApp import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
     path('',login_required(views.per), name="Grafica"),
      path('Gporyear',login_required(views.Gporyear), name="Gporyear"), 
      path('prueba',login_required(views.prueba), name="prueba"), 
      path('graf1',login_required(views.graf1), name="graf1"), 
      path('graf2',login_required(views.graf2), name="graf2"), 
      path('graficaAT',views.graficaAT, name="graficaAT"), # agencias por tipo de obra
      path('graficaATS',views.graficaATS, name="graficaATS"), # agencias por tipo de solicitud
      path('graficaASolic',views.graficaASolic, name="graficaASolic"), # solicitudes aprobadas, denegadas, observadas y vencidas
      path('grafTipoSol',views.grafTipoSol, name="grafTipoSol"), 
      path('grafAgenciaP',views.grafAgenciaP, name="grafAgenciaP"), 
      path('grafAgenciaPN',views.grafAgenciaPN, name="grafAgenciaPN"), 
      
     # path('prueba/', TemplateView.as_view(template_name="GraficasApp/prueba.html"),name="prueba"),   
]
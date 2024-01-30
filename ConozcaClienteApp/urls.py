from django.urls import path
from ConozcaClienteApp import views
from Reportes import views as viewsnat


urlpatterns = [
path('cclientedg/',views.ccliente, name="ccliente"),  #/<id>
path('registrarD/',views.registrarD), 
path('cclientedgf/',views.cclientedgf, name="cclientedgf"),



path('listaCC/', views.listaConozcaC, name="listaCC"),
path('listaCC/editarCliente/<id>',views.editarCliente),
path('editarD/', views.editarD),

# para reporte
path('listaCC/conozcaC/<id>', viewsnat.conozcaClient, name="conozcaC"),

]
from django.urls import path
from DeclaracionJurClienteApp import views
from Reportes import views as viewsnat

urlpatterns = [

path('',views.declaracionjc, name="declaracionjc"),
path('registrarDj/',views.registrarDj), 
path('listaDJ/', views.listaDJ, name="listaDJ"),
path('listaDJ/editarDJ/<id>', views.editarDJ, name="editarDJ"),
path('modificarDJ/', views.modificarDJ),

# para reporte de Declaración Jurada cliente
path('listaDJ/declaracionjc/<id>/<idp>', viewsnat.declaracion),

]
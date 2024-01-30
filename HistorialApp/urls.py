from django.urls import path
from HistorialApp import views
from Reportes import views as viewsnat

urlpatterns = [

    path('listaHis/', views.listaPerfil, name="listaHis"),
    path('rangoHis/', views.rangoHist, name="rangoh"),
    path('listarango/', views.listaRango, name="listaRango"),
    path('editRango/<idr>', views.editarRango),
    path('modHistCli/', views.modificarPuntajeC),
    path('registroHist/', views.registroHis, name="puntajeRan"),
    path('listaHis/registroHistCli/<id>', views.regisRanCli),
    path('regisPunt/',views.regisPunt),
    path('listaPunt/', views.listaPunCli, name="listapuntaje"),
    path('editHistCli/<idpCli>', views.editarPuntCli),
    path('modHistCli/', views.modificarPuntajeC),
    #reporte
    path('listaHis/historial/<id>',viewsnat.historialC, name="historial"),
    path('listaHis/autorizacion/<id>',viewsnat.autorizacion, name="autorizacion"),
    
]
from django.urls import path
from DireccionApp import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #login_required()
     path('',views.depto, name="depto"),
     path('registrarDepto/',views.registrarDepto), 
     path('listarDepto',views.listarDepto, name="listarDepto"),
     path('modiDepto/<id>', views.modiDepto),
     #path('listarDepto/modiDepto/<id>', views.modiDepto),
     path('editDepto/',views.editDepto),
     ############PARA MUNICIPIOS
     path('muni',views.muni, name="muni"),
     path('registrarMuni/',views.registrarMuni), 
     path('listarMuni',views.listarMuni, name="listarMuni"),
     path('modiMuni/<idmuni>', views.modiMuni),
     path('mu/',views.mu),
     path('editMuni/',views.editMuni),

     path('distrito',views.distrito, name="distrito"),
     path('municipio/',views.municipio), 
     path('registrarDistri/',views.registrarDistri), 
     path('listarDistrito/', views.listarDistrito, name="listarDistrito"),
     path('mun/', views.mun),
     path('munic/', views.munic),
     path('modiDistri/<iddistri>', views.modiDistri),
     path('editDistri/', views.editDistri),

]
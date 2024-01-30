from django.urls import path
from PresupuestoVApp import views
from Reportes import views as viewsnat

urlpatterns = [
    
   # path('',views.home, name="home"),
    path('presupuestov/',views.presupuestov, name="presupuestov"),# apunta a la raiz 
    path('presupuestos/', views.get, name='presupuestos'), # llena el select con los materiales
    path('registrarPV/',views.registrarPV, name="registrarPV"), 
    path('listaPV/', views.listaPV, name="listaPV"),
    path('listaPV/editarPV/<id>', views.editarPV, name="editarPV"),
    path('actualizarPresupuestoV/', views.actualizar_presupuestoV), 
    # para reporte
    path('listaPV/presupuestoVv/<id>', viewsnat.presupuestoViv, name="presupuestoVv"),

    # para presupuesto de obras adicionales
    path('listaPV/presupuestovoa/<id>',views.presupuestovoa, name="presupuestovoa"),
    path('presupuestosobra/', views.obtenermt, name='presupuestosobra'), # llena el select con los materiales
    path('registrarPVObra/',views.registrarPVObra, name="registrarPVObra"), 
    path('listaPVO/', views.listaPVO, name="listaPVO"),
    path('listaPVO/editarPVO/<id>', views.editarPVO, name="editarPVO"),
    path('modificarPVObra/', views.modificarPVO),
    # para reporte
    path('listaPVO/presupuestoVvO/<id>', viewsnat.presupuestoVivO, name="presupuestoVvO"),

]
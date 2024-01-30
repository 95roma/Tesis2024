from django.urls import path
from PresupuestoApp import views
from Reportes import views as viewsnat

urlpatterns = [
    
   # path('',views.home, name="home"),
    path('presupuesto/',views.presupuesto, name="presupuesto"),# apunta a la raiz 
    path('presupuestos/', views.get, name='presupuestos'),
    path('registrarP/',views.registrarP, name="registrarP"), 
    path('listaPM/', views.listaPM, name="listaPM"),
    path('listaPM/modPresupuesto/<id>',views.modificarPresupuesto, name="modPresupuesto"),
    path('actualizarPresupuesto/',views.actualizarPresupuesto),

    # para reporte
    path('listaPM/presupuestoMj/<id>', viewsnat.presupuestoMej, name="presupuestoMj"),


    

]
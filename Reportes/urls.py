from django.urls import path
from Reportes import views

urlpatterns = [
    path('soliPer/<idp>', views.SolicitudPe, name="soliPer"),
    path('historialC/<idp>', views.historialC, name="historialC"),
    path('evaluacionIvEF/<id>', views.evaluacionF, name="evaluacionIvEF"),
    path('evaluacionIM/<id>', views.evaluacionM, name="evaluacionIM"),
    path('inspeccionM/<id>', views.inspeccionM, name="inspeccionM"),
    path('inspeccionL/<id>', views.inspeccionL, name="inspeccionL"),
    path('listaCheq/<id>', views.listaC, name="listaCheq"),
    path('pinspl/<id>', views.pinspecL, name="pinspl"), # esquema lote
    path('pinsplU/<id>', views.pinspecLU, name="pinsplU"),# ubicacion lote
    path('pinsplR/<id>', views.pinspecLR, name="pinsplR"), # reporte fotografico lote
    path('pinspmU/<id>', views.pinspecMU, name="pinspmU"),# ubicacion mejora
    path('pinspmR/<id>', views.pinspecMR, name="pinspmR"), # reporte fotografico mejora
    path('presupuestoMj/<id>', views.presupuestoMej, name="presupuestoMj"),
    path('presupuestoVv/<id>', views.presupuestoViv, name="presupuestoVv"),
    path('presupuestoVvO/<id>', views.presupuestoVivO, name="presupuestoVvO"), # presupuesto de obras adicionales
    path('hojaP/<id>', views.hojaPreAprobacion, name="hojaP"), # para micro
    path('formularioC/<id>', views.formComiteC, name="formularioC"), # para micro
    path('hojaPN/<id>', views.hojaPreAprobacionN, name="hojaPN"), # para natural
    path('formularioCN/<id>', views.formComiteCN, name="formularioCN"), # para natural
    path('solP/<id>', views.solicPA, name="solP"), # solicitudes pendientes de aprobacion
    path('pelfilNA/<id>', views.perfilNA, name="pelfilNA"), # perfiles que no aplican
    path('solObs/<id>', views.solicObs, name="solObs"), # solicitudes observadas
    path('solDen/<id>', views.solicDen, name="solDen"), # solicitudes observadas
]
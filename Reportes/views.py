from django.shortcuts import render
from fpdf import FPDF, HTMLMixin
from NaturalApp.models import *
from Reportes.formComite import *
from Reportes.formComiteN import *
from Reportes.historialC import *
from Reportes.hojaPre import *
from Reportes.hojaPreN import *
from Reportes.solMicro import *
from Reportes.solPer import *
from Reportes.autoInfor import *
from Reportes.declaJur import *
from Reportes.conozcaClie import *
from Reportes.seguro import *
from Reportes.inspeccionl import *
from Reportes.inspeccionm import *
from Reportes.evaluacionIvE import *
from Reportes.evaluacionMc import *
from Reportes.listChequeo import *
from Reportes.pInspeccionLE import *
from Reportes.pInspeccionLU import *
from Reportes.pInspeccionLR import *
from Reportes.pInspeccionMU import *
from Reportes.pInspeccionMR import *
from Reportes.presupuestoM import *
from Reportes.presupuestoV import *
from Reportes.presupuestoVO import *
from Reportes.solicitudesPA import *
from Reportes.perfilesNA import *
from Reportes.solicitudesObs import *
from Reportes.solicitudesDen import *


# Create your views here.


def SolicitudPe(request, ids):
    solp=solicitudPer()
    soliPers=solp.soliPer(ids)
    return soliPers

def historialC(request, id):
    his=HistorialC()
    histo=his.historialC(id)
    return histo

def solicitudMicro(request, ids, idp):
    solm=SolicitudMicro()
    micro=solm.soliMicro(ids, idp)
    return micro

def autorizacion(request, id):
    aut=Autorizacion()
    auto=aut.autorizacionI(id)
    return auto

def declaracion(request, id, idp):
    dec=Declaracion()
    declar=dec.declaJur(id, idp)
    return declar

def conozcaClient(request, id):
    con=ConozcaC()
    conoz=con.conozcaClie(id)
    return conoz

def seguro(request, id):
    seg=Seguro()
    segu=seg.seguro(id)
    return segu

def inspeccionM(request,id):
    inspm=InspeccionMV()
    insp=inspm.inspeccionM(id)
    return insp

def inspeccionL(request,id):
    inspl=InspeccionL()
    insp=inspl.inspeccionL(id)
    return insp

def evaluacionF(request, id):
    eva=evaluacionIvEF()
    evaf=eva.evaluacionIvE(id)
    return evaf

def evaluacionM(request, id):
    eva=evaluacionIM()
    evam=eva.evaluacionMc(id)
    return evam

def listaC(request, id):
    lsc=listaCheq()
    listc=lsc.listChequeo(id)
    return listc


# esquema primera inspeccion lote
def pinspecL(request, id):
    pil=pinspl()
    pinsl=pil.pInspeccionLE(id)
    return pinsl

# ubicacion primera inspeccion lote
def pinspecLU(request, id):
    pilu=pinsplu()
    pinslu=pilu.pInspeccionLU(id)
    return pinslu

# reporte fotografico primera inspeccion lote
def pinspecLR(request, id):
    pilr=pinsplr()
    pinslr=pilr.pInspeccionLR(id)
    return pinslr

# ubicacion primera inspeccion mejora
def pinspecMU(request, id):
    pimu=pinspmu()
    pinsmu=pimu.pInspeccionMU(id)
    return pinsmu

# reporte fotografico primera inspeccion mejora
def pinspecMR(request, id):
    pimr=pinspmr()
    pinsmr=pimr.pInspeccionMR(id)
    return pinsmr

def presupuestoMej(request, id):
    pre=presupuestoMj()
    prem=pre.presupuestoM(id)
    return prem

def presupuestoViv(request, id):
    pres=presupuestoVv()
    prev=pres.presupuestoV(id)
    return prev

def presupuestoVivO(request, id):
    pres=presupuestoVvO()
    prevo=pres.presupuestoVO(id)
    return prevo

def hojaPreAprobacion(request, id):
    hoj=hojaP()
    hojp=hoj.hojaPre(id)
    return hojp

def formComiteC(request, id):
    form=formularioC()
    formc=form.formComite(id)
    return formc

def hojaPreAprobacionN(request, id): # para natural
    hoj=hojaPN()
    hojp=hoj.hojaPreN(id)
    return hojp

def formComiteCN(request, id): # para natural
    form=formularioCN()
    formc=form.formComiteN(id)
    return formc


def solicPA(request, id):
    sl=solP()
    solp=sl.solicitudesPA(id)
    return solp

def perfilNA(request, id):
    pn=perN()
    prn=pn.perfilesNA(id)
    return prn

def solicObs(request, id):
    slo=solObs()
    solobs=slo.solicitudesObs(id)
    return solobs

def solicDen(request, id):
    sld=solDen()
    solden=sld.solicitudesDen(id)
    return solden

from fpdf import FPDF
from datetime import date
import locale
from ClienteApp.models import *

from django.http import FileResponse
from SolicitudesApp.models import *
from ClienteApp.models import Perfil
from SolicitudInscripcionSApp.models import *
from django.db.models import Q



class Seguro(FPDF):
    
    def consultas(request, id):
        return ""

    def seguro(request, id):

        locale.setlocale(locale.LC_TIME, 'es_ES')
        fecha=date.today()
        
        print(fecha)
        # idSolicitud=request.POST['idSoli']
        try:
            sol=solicitud.objects.get(id=id)
        except:
            sol=''
        try:
            seg=Solicitudis.objects.get(ids=id)
        except:
            seg=''

        try:
            dp=datosPersonales.objects.get(idSolicitud=id)
        except:
            dp=''
        try:
            sda=Solicitudisdadf.objects.get(idsis=seg.id)
        except:
            sda=''
        
        try:
            dom=domicilio.objects.get(idSolicitud=id, tipo="Solicitante")
        except:
            dom=''
        try:
            pad=SolicitudisPadecimiento.objects.filter(idp=sol.perfil.id)
            con=pad.count()
        except:
            pad=''
        try:
            enf=SolicitudisEnfermedad.objects.all()
        except:
            enf=''


        
        #dp=DatosPersonalesF.objects.get(idSolicitud=ids, tipo ='codeudor')
        #print(dp)
        #if(dp.tipo !="Solicitante"):
        #    dpt=datosPersonales.objects.get(id=dp.id)
        
        r=0
        g=0#102
        b=0#153
        aux=[0, 1, 2, 3]
        aux2=[0, 1, 2]    
        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        
        pdf.image('TesisApp\static\TesisApp\images\segu.png', x=10, y=10, w=20, h=10)#, link=url)

        #pdf.set_font('Arial', 'B', 12)
        #pdf.text(x=40, y=30, txt='AUTORIZACIÓN PARA CONSULTAR Y COMPARTIR INFORMACIÓN.')
        
        tex1="De acuerdo con las condiciones de la Póliza No. CD-0033 de Seguro COLECTIVO DE VIDA TEMPOLAR DECRECIENTE emitida a nombre de ASOCIACION HPH EL SALVADOR, se solicita inscribir como asegurado a"
        tex2='Convengo en que la presente solicitud y los datos proporcionados en ella son parte y constituyen la base del Contrato de Seguro y acepto las Condiciones de la Póliza correspondiente. Declaro que los datos proporcionados son verdaderos y completos. Acepto que cualquier diferencia encontrada en la informacion proporcionada en esta Solicitud, que he firmado para el otorgamiento del credito, y mi estado de salud actual, ocasionará que el presente seguro quede sin efecto asi como los beneficios contratados. Autorizo a cualquier medico, hospital o clinica que me haya atendido revele a Aseguradora Agrícola Comercial, S.A. cualquier dato o información que ésta requiera.'
        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(r,g,b)
        pdf.text(x=30, y=25, txt='SOLICITUD DE INSCRIPCION PARA SEGURO COLECTIVO DE VIDA TEMPORAL.')
        
            
        pdf.set_font('Arial', '', 9.5)
        pdf.set_y(30)
        pdf.set_left_margin(15)
        pdf.multi_cell(w=0,h=5,txt=tex1, border=0, align='J', fill=False)
        pdf.cell(w=0,h=5,txt=sol.perfil.nombres+' '+sol.perfil.apellidos, border='B', align='C', fill=False, ln=1)
        pdf.ln(h=2)
        pdf.cell(w=50,h=5,txt='Montos asegurados anteriores:', border=0, align='L', fill=False)
        pdf.cell(w=35,h=5,txt='$ '+str(seg.montoaa) if hasattr(seg, 'montoaa') else '', border='B', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=50,h=5,txt='Nuevo monto a asegurar:', border='', align='L', fill=False)
        pdf.cell(w=35,h=5,txt='$ '+ str(seg.nuevoma) if hasattr(seg, 'nuevoma') else '', border='B', align='L', fill=False)
        pdf.cell(w=20,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=10,h=5,txt='Plazo', border='', align='L', fill=False)
        pdf.cell(w=10,h=5,txt=seg.plazo if hasattr(seg, 'plazo') else '', border='B', align='C', fill=False)
        pdf.cell(w=10,h=5,txt='años', border='', align='L', fill=False)
        pdf.cell(w=15,h=5,txt='Garantía:', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt=seg.garantia if hasattr(seg, 'garantia') else '', border='B', align='L', fill=False)
        pdf.cell(w=50,h=5,txt='Monto Total asegurado:', border='', align='L', fill=False)
        pdf.cell(w=35,h=5,txt='$ '+str(seg.montot) if hasattr(seg, 'montot') else '', border='B', align='L', fill=False)
        pdf.cell(w=40,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=25,h=5,txt='San Salvador,', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='B', align='C', fill=False)
        pdf.cell(w=150,h=5,txt='', border='', align='C', fill=False)
        pdf.multi_cell(w=0,h=8,txt='', border='B', align='C', fill=False)
        pdf.cell(w=150,h=5,txt='', border='', align='C', fill=False)
        pdf.multi_cell(w=0,h=5,txt='Por el Contratante', border='T', align='C', fill=False)
        #pdf.ln(h=3)
        pdf.cell(w=0,h=3,txt='', border='B', align='C', fill=False, ln=1)
        pdf.multi_cell(w=0,h=5,txt='En relacion con la presente solicitud, manifiesto mi conformidad para ser inscrito como asegurado y opara ese fin proporciono los siguientes datos:', border='', align='J', fill=False)
        pdf.cell(w=33,h=8,txt='1. Nombre completo', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt=sol.perfil.nombres+' '+sol.perfil.apellidos, border='B', align='C', fill=False)
        pdf.cell(w=38,h=8,txt='2. Fecha de nacimiento', border='', align='L', fill=False)
        pdf.cell(w=30,h=5,txt=sol.perfil.fechan.strftime("%d/%m/%Y") if hasattr(sol, 'perfil') else '', border='B', align='C', fill=False)
        pdf.cell(w=10,h=8,txt='Edad:', border='', align='L', fill=False)
        pdf.cell(w=10,h=5,txt=str(sol.perfil.edad) if hasattr(sol, 'perfil') else '', border='B', align='C', fill=False)
        pdf.cell(w=15,h=8,txt='años', border='', align='L', fill=False)
        pdf.cell(w=24,h=8,txt='3. Estado civil:', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt=dp.estadocivilC if hasattr(dp, 'estadocivilC') else '', border='B', align='C', fill=False)
        pdf.cell(w=20,h=8,txt='4. Sexo:', border='', align='L', fill=False)
        pdf.set_xy(30,100)
        if dp.generoC is 'Femenino':
            pdf.cell(w=5,h=8,txt='M', border='', align='L', fill=False)
            pdf.set_xy(35,102)
            pdf.cell(w=3,h=3,txt='', border=1, align='C', fill=False)
            pdf.set_xy(40,100)
            pdf.cell(w=5,h=8,txt='F', border='', align='C', fill=False)
            pdf.set_xy(45,102)
            pdf.cell(w=3,h=3,txt='X', border=1, align='C', fill=False)
        else:
            pdf.cell(w=5,h=8,txt='M', border='', align='L', fill=False)
            pdf.set_xy(35,102)
            pdf.cell(w=3,h=3,txt='X', border=1, align='C', fill=False)
            pdf.set_xy(40,100)
            pdf.cell(w=5,h=8,txt='F', border='', align='C', fill=False)
            pdf.set_xy(45,102)
            pdf.cell(w=3,h=3,txt='', border=1, align='C', fill=False)
        pdf.set_xy(48,100)
        pdf.cell(w=15,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=20,h=8,txt='5. Estatura:', border='', align='L', fill=False)
        pdf.cell(w=10,h=5,txt=str(seg.estatura) if hasattr(seg, 'estatura') else '', border='B', align='C', fill=False)
        pdf.cell(w=15,h=8,txt='Mts.', border='', align='L', fill=False)
        pdf.cell(w=10,h=8,txt='Peso:', border='', align='L', fill=False)
        pdf.cell(w=15,h=5,txt=str(seg.peso) if hasattr(seg, 'peso') else '', border='B', align='C', fill=False)
        pdf.cell(w=10,h=8,txt='libras', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=8,txt='', border='', align='L', fill=False)
        pdf.cell(w=30,h=5,txt='6. Ocupacion actual', border='', align='L', fill=False)
        pdf.cell(w=60,h=5,txt=sol.perfil.idocu.ocupacion if hasattr(sol, 'perfil') else '', border='B', align='C', fill=False)
        pdf.cell(w=5,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=20,h=8,txt='7. No.DUI', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt=sol.perfil.dui if hasattr(sol, 'perfil') else '', border='B', align='C', fill=False)
        pdf.cell(w=50,h=8,txt='8. Lugar de trabajo:', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt=dom.lugarTrabajo if hasattr(dom, 'lugarTrabajo') else '', border='B', align='C', fill=False)
        pdf.multi_cell(w=0,h=5,txt='9. Designo como beneficiario irrevocable a ASOCIACION HPH EL SALVADOR hasta por el importe de la deuda contraida con dicha institucion', border='', align='J', fill=False)
        #pdf.ln()
        pdf.multi_cell(w=0,h=5,txt='DECLARACION DE SALUD:', border='', align='C', fill=False)
        pdf.cell(w=50,h=5,txt='PADECE O HA PADECIDO DE :', border='', align='L', fill=False, ln=1)
        pdf.cell(w=80,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=10,h=5,txt='SI', border=1, align='C', fill=False)
        pdf.cell(w=10,h=5,txt='NO', border=1, align='C', fill=False)
        pdf.cell(w=70,h=5,txt='', border=1, align='C', fill=False)
        pdf.cell(w=10,h=5,txt='SI', border=1, align='C', fill=False)
        pdf.multi_cell(w=0,h=5,txt='NO', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 7)
        i=1
        x=0
        y=0
        cont=0
        padext=''
        if pad is not '' and con>0: #Verificar que el solicitante tenga padecimientos registrados
            for fila in enf: # Obtener las enfermedades para ir generando la tabla
                i=i%2 #Sirve para saber si es una columna par
                print('entro')
                if i!= 0 and fila.personal!='Si': #Verifica si la columna es par o impar
                    pdf.cell(w=80,h=5,txt=fila.nombreenf if hasattr(fila, 'nombreenf') else '', border=1, align='L', fill=False) #Mostrar los nombres de las enfermedades
                    c=0
                    for p in pad:
                        c=c+1
                        #print(fila.id + ' '+ p.idsisenf.id)
                        if fila.id == p.idsisenf.id: #Mostara las enfermedades que el solicitante ha guardado
                            pdf.cell(w=10,h=5,txt='X', border=1, align='C', fill=False)
                            pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                            cont=cont+1
                            break
                        elif c == con:
                            pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                            pdf.cell(w=10,h=5,txt='X', border=1, align='C', fill=False)
                            
                elif fila.personal!='Si':
                    pdf.cell(w=70,h=5,txt=fila.nombreenf if hasattr(fila, 'nombreenf') else '', border=1, align='L', fill=False)
                    c=0
                    for p in pad:
                        c=c+1
                        if fila.id == p.idsisenf.id:
                            pdf.cell(w=10,h=5,txt='X', border=1, align='C', fill=False)
                            pdf.multi_cell(w=0,h=5,txt='', border=1, align='C', fill=False)
                            cont=cont+1
                            break
                        elif c == con:
                            pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                            pdf.multi_cell(w=0,h=5,txt='X', border=1, align='C', fill=False)
                            
                i=i+1
                #pdf.ln()
            
            for np in enf: # Obtener las enfermedades para ir generando la tabla
                i=i%2 #Sirve para saber si es una columna par
                print('entro')
                if i!= 0: #Verifica si la columna es par o impar
                    c=0
                    for p in pad:
                        
                        c=c+1
                        #print(fila.id + ' '+ p.idsisenf.id)
                        if np.id == p.idsisenf.id and np.personal=='Si': #Mostrara la enfermedad extra que el solicitante ha registra
                            pdf.cell(w=80,h=5,txt=np.nombreenf if hasattr(np, 'nombreenf') else '', border=1, align='L', fill=False) #Mostrar los nombres de las enfermedades
                            pdf.cell(w=10,h=5,txt='X', border=1, align='C', fill=False)
                            pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                            cont=cont+1
                            padext='si'#Padecimiento agregado del solicitante
                            break
                                                
                else:
                    c=0
                    for p in pad:
                        c=c+1
                        if np.id == p.idsisenf.id  and np.personal=='Si':
                            pdf.cell(w=70,h=5,txt=np.nombreenf if hasattr(np, 'nombreenf') else '', border=1, align='L', fill=False)
                            pdf.cell(w=10,h=5,txt='X', border=1, align='C', fill=False)
                            pdf.multi_cell(w=0,h=5,txt='', border=1, align='C', fill=False)
                            cont=cont+1
                            padext='si'#Padecimiento agregado del solicitante
                            break
                                                    
                i=i+1
                #pdf.ln()
                x=pdf.get_x()
                y=pdf.get_y()
            if cont>=pad.count() and padext=='':
                i=i%2 #Sirve para saber si es una columna par
                
                if i!= 0 and x<50: #Verifica si la columna es par o impar
                    pdf.cell(w=80,h=5,txt= str(x), border=1, align='L', fill=False) 
                    pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                    pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                    
                else:
                    pdf.cell(w=70,h=5,txt= '', border=1, align='L', fill=False)
                    pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                    pdf.multi_cell(w=0,h=5,txt='', border=1, align='C', fill=False)
            

                            
        else:
            for fila in enf:
                i=i%2
                if i!= 0:
                    pdf.cell(w=80,h=5,txt=fila.nombreenf if hasattr(fila, 'nombreenf') else '', border=1, align='L', fill=False)
                    pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                    pdf.cell(w=10,h=5,txt='X', border=1, align='C', fill=False)                          
                else:
                    pdf.cell(w=70,h=5,txt=fila.nombreenf if hasattr(fila, 'nombreenf') else '', border=1, align='L', fill=False)
                    pdf.cell(w=10,h=5,txt='', border=1, align='C', fill=False)
                    pdf.multi_cell(w=0,h=5,txt='X', border=1, align='C', fill=False)
                            
                i=i+1
                #pdf.ln()                 
        

        
        pdf.ln()
        pdf.set_font('Arial', 'B', 8.5)
        pdf.multi_cell(w=0,h=3,txt='Declaro que no padezco ni me ha sido diagnosticada ninguna enfermedad que he marcado como NO y  acepto que de padecer de alguna de estas enfermedades previo a la fecha de esta declaraión, no tendre derecho a ninguno de los beneficios o coberturas descritas en la poliza de seguro, de la cual forma parte esta solicitud. Si marqué SI en alguno de los padecimientos nombrados, a continuación proporciono los detalles (fecha, padecimiento, tratamiento recibido, situacion actual):', border='', align='J', fill=False)
        pdf.set_font('Arial', '', 8.5)
        for det in pad:
            pdf.cell(w=40,h=5,txt=det.fechap.strftime("%d/%m/%Y") +' - '+ det.tratamientor + ' / ', border='B', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='B', align='C', fill=False)
        #pdf.ln(h=3)
        pdf.cell(w=135,h=5,txt='10. Tiene  alguna   deformidad,   amputacion  o  defecto   fisico,   defecto  de  la  vista  o  del   oido?', border='', align='J', fill=False)
        pdf.cell(w=20,h=5,txt='', border='B', align='C', fill=False)
        pdf.multi_cell(w=0,h=5,txt='(Caso  afirmativo  dar', border='', align='R', fill=False)
        pdf.cell(w=15,h=5,txt='detalles)', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='B', align='C', fill=False)
        pdf.cell(w=45,h=8,txt='11. Fuma cigarrillos o pipa?', border='', align='L', fill=False)
        pdf.set_xy(53,200)
        if sda.fumacp == 'No':
            pdf.cell(w=6,h=8,txt='SI', border='', align='C', fill=False)
            pdf.set_xy(59,201)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
            pdf.set_xy(64,200)
            pdf.cell(w=6,h=8,txt='NO', border='', align='C', fill=False)
            pdf.set_xy(71,201)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
        else:
            pdf.cell(w=6,h=8,txt='SI', border='', align='C', fill=False)
            pdf.set_xy(59,201)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
            pdf.set_xy(64,200)
            pdf.cell(w=6,h=8,txt='NO', border='', align='C', fill=False)
            pdf.set_xy(71,201)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
        pdf.set_xy(75,200)
        pdf.cell(w=10,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=25,h=8,txt='Cuántos al día?', border='', align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='B', align='C', fill=False)
        pdf.cell(w=50,h=8,txt='12. Ingiere bebedas alcohólicas)', border='', align='L', fill=False)
        pdf.set_xy(65,205)
        if sda.bebidadalc == 'No':
            pdf.cell(w=7,h=8,txt='SI', border='', align='L', fill=False)
            pdf.set_xy(70,206)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
            pdf.set_xy(75,205)
            pdf.cell(w=7,h=8,txt='NO', border='', align='L', fill=False)
            pdf.set_xy(82,206)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
        else:
            pdf.cell(w=7,h=8,txt='SI', border='', align='L', fill=False)
            pdf.set_xy(70,206)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
            pdf.set_xy(75,205)
            pdf.cell(w=7,h=8,txt='NO', border='', align='L', fill=False)
            pdf.set_xy(82,206)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
        pdf.set_xy(87,205)    
        pdf.cell(w=40,h=8,txt='Con qué frecuencia?', border='', align='R', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='B', align='C', fill=False)
        pdf.cell(w=120,h=5,txt='13 ¿Ha      estado      en       tratamiento      con      algun       medico,      hospital     o      clinica?', border='', align='J', fill=False)
        pdf.cell(w=20,h=5,txt='', border='B', align='C', fill=False)
        pdf.multi_cell(w=50,h=5,txt='(Caso    afirmativo    dar', border='', align='R', fill=False)
        pdf.cell(w=20,h=5,txt='detalles):', border=0, align='L', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='B', align='C', fill=False)
        pdf.cell(w=82,h=5,txt='14. Practíca alguna actividad o deporte peligroso o extermo?', border='', align='L', fill=False)
        pdf.set_xy(100,220)
        if sda.practicaad == 'No':
            pdf.cell(w=7,h=6,txt='SI', border='', align='L', fill=False)
            pdf.set_xy(106,221)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
            pdf.set_xy(111,220)
            pdf.cell(w=7,h=6,txt='NO', border='', align='L', fill=False)
            pdf.set_xy(117,221)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
        else:
            pdf.cell(w=7,h=5,txt='SI', border='', align='L', fill=False)
            pdf.set_xy(106,221)
            pdf.cell(w=3,h=3,txt='X', border=1, align='C', fill=False)
            pdf.set_xy(111,220)
            pdf.cell(w=7,h=5,txt='NO', border='', align='L', fill=False)
            pdf.set_xy(117,221)
            pdf.cell(w=3,h=3,txt='', border=1, align='C', fill=False)
        pdf.set_xy(125,220)
        
        pdf.multi_cell(w=0,h=5,txt='En caso afirmativo favor indicar que clase y la frecuencia:', border='', align='J', fill=False)
        pdf.cell(w=0,h=4,txt=sda.frecuenciaad or '', border='B', align='C', fill=False, ln=1)
        pdf.ln(4)
        pdf.cell(w=30,h=5,txt='Seguro de Desempleo', border='', align='L', fill=False)
        pdf.set_xy(48,233)
        if sda.segurodd == 'No':
            pdf.cell(w=5,h=5,txt='SI', border='', align='C', fill=False)
            pdf.set_xy(55,233)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
            pdf.set_xy(60,233)
            pdf.cell(w=5,h=5,txt='NO', border='', align='C', fill=False)
            pdf.set_xy(65,233)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
        else:
            pdf.cell(w=5,h=5,txt='SI', border='', align='C', fill=False)
            pdf.set_xy(55,233)
            pdf.cell(w=4,h=4,txt='X', border=1, align='C', fill=False)
            pdf.set_xy(60,233)
            pdf.cell(w=5,h=5,txt='NO', border='', align='C', fill=False)
            pdf.set_xy(65,233)
            pdf.cell(w=4,h=4,txt='', border=1, align='C', fill=False)
        pdf.multi_cell(w=0,h=5,txt='', border='', align='C', fill=False)
        pdf.multi_cell(w=0,h=3,txt=tex2, border='T', align='J', fill=False)
        pdf.cell(w=50,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=50,h=5,txt='', border='', align='C', fill=False)
        pdf.cell(w=50,h=5,txt='', border='', align='C', fill=False)
       
        pdf.line(30, 265, 90, 265)
        pdf.text(x=45, y=270, txt='Firma Solicitante ')
        pdf.line(130, 265, 180, 265)
        pdf.text(x=120, y=265, txt='Fecha: ')
        
        pdf.output('solicitudSeguro.pdf', 'F')
        return FileResponse(open('solicitudSeguro.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
        #return redirect("listaSolicitud")

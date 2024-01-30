let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//botones para formularios
let btnEvaluacion = document.getElementById("btnEvaliacionMicro")
let btnSolicitudCredito = document.getElementById("btnSolicitudCredito")
let btnConozCliente = document.getElementById("btnConozCliente")
let btnDeclaracionJurada = document.getElementById("btnDeclaracionJurada")
let btnInscripcionSeguro = document.getElementById("btnInscripcionSeguro")
let btnInspeccionLote = document.getElementById("btnInspeccionLote")
let btnPresupuestoVivienda = document.getElementById("btnPresupuestoVivienda")
let btnDicom = document.getElementById("btnDicom")  
let btnlistaChequeo = document.getElementById("btnlistaChequeo")
let btnPrimeraInspeccion = document.getElementById("btnPrimeraInspeccion")
let btnSegundaInspeccion = document.getElementById("btnSegundaInspeccion")
let btnTerceraInspeccion = document.getElementById("btnTerceraInspeccion")
let btnObrasAdicionales = document.getElementById("btnObrasAdicionales")

//botones para reportes
let btnConozClienteRepo = document.getElementById("btnConozClienteRepo")
let btnDeclaracionJuradaRepo = document.getElementById("btnDeclaracionJuradaRepo") 
let btnInscripcionSeguroRepo = document.getElementById("btnInscripcionSeguroRepo")
let btnInspeccionLoteRepo = document.getElementById("btnInspeccionLoteRepo")
let btnPresupuestoViviendaRepo = document.getElementById("btnPresupuestoViviendaRepo")
let btnEvaluacioRepo = document.getElementById("btnEvaliacionRepo")
let btnSolicitudRepo = document.getElementById("btnSolicitudCreditoRepo")
let btnesquema1Repo = document.getElementById("btnesquema1Repo")
let btnUbicacion1Repo = document.getElementById("btnUbicacion1Repo")
let btnPFotografico1Repo = document.getElementById("btnPFotografico1Repo")
let btnesquema2Repo = document.getElementById("btnesquema2Repo")
let btnUbicacion2Repo = document.getElementById("btnUbicacion2Repo")
let btnPFotografico2Repo = document.getElementById("btnPFotografico2Repo")
let btnesquema3Repo = document.getElementById("btnesquema3Repo")
let btnUbicacion3Repo = document.getElementById("btnUbicacion3Repo")
let btnPFotografico3Repo = document.getElementById("btnPFotografico3Repo")
let btnListaChequeoRepo = document.getElementById("btnListaChequeoRepo")
let btnObrasAdicionalesRepo = document.getElementById("btnObrasAdicionalesRepo")


//mensajes
let titulo = document.getElementById("titulo")
let descipcion = document.getElementById("despcipcion")
//role panel
let roleIniciar = document.getElementById("nueva-soli-role")
let panelIniciar = document.getElementById("nueva-solicitud")
let roleFormularios = document.getElementById("role-formularios")
let panelFormularios= document.getElementById("tab_content3")
let roleReporte = document.getElementById("roler-reportes")
let roleChequeo = document.getElementById("roler-chequeo")
let panelReporte = document.getElementById("tab_reportes")
let panelChequeo = document.getElementById("tab_chequeo")
let roleHistorial = document.getElementById("roler-historial")
let panelHistorial = document.getElementById("historial-tab2")
//variables
let idCliente = document.getElementById("idCliente").value
let idEv = ""
let estadoCliente = document.getElementById("estado-cliente").value
let idSoli = ""
let tipoObra = ""

//barras de progresos de formularios
let progresoSolicitud = document.getElementById("progresoSoli")
let progresoEvaluacionMicro = document.getElementById("rogresoEvaluacionMicro") 
let progresoEvaluacionNatural= document.getElementById("rogresoEvaluacionNatural")
let progresoSoliMicro = document.getElementById("progresoSoliMicro")
let progresoConozcaCliente = document.getElementById("progresoConozcaCliente")
let progresoDeclaracion = document.getElementById("progresoDeclaracion")
let progresoSeguro = document.getElementById("progresoSeguro")
let progresoInspeccion = document.getElementById("progresoInspeccion")
let progresoPresupuesto = document.getElementById("progresoPresupuesto")
let progresoPrimeraInspeccion = document.getElementById("progresoPrimeraInspeccion")
let progresoSegundaInspeccion = document.getElementById("progresoSegundaInspeccion")
let progresoTerceraInspeccion = document.getElementById("progresoTerceraInspeccion")
let progresoObrasAdd = document.getElementById("progresoObrasAdd")

//barra de progreso reportes
let progresoConozcaClienteRepo = document.getElementById("progresoConozcaClienteRepo") 
let progresoDeclaracionRepo = document.getElementById("progresoDeclaracionRepo")
let progresoSeguroRepo = document.getElementById("progresoSeguroRepo")
let progresoInspeccionRepo = document.getElementById("progresoInspeccionRepo")
let progresoPresupuestoRepo = document.getElementById("progresoPresupuestoRepo")
let progresoSolicitudRepo = document.getElementById("progresoSoliRepo")
let progresoEvaluacionRepo= document.getElementById("rogresoEvaluacionRepo") 
let progresoObrasAdicionalesRepo= document.getElementById("progresoObrasAdicionalesRepo") 
let progreso = 1
$(document).ready(function () {
    if (estadoCliente == "1") {
        titulo.textContent = "Iniciar nueva solicitud"
        descipcion.textContent = "Seleccione el tipo"
        $('#nueva-soli').fadeIn();
        $('#progreso-soli').fadeOut();

        roleIniciar.classList.add("active")
        panelIniciar.classList.remove("fade")
        panelIniciar.classList.add("active")

    } else {
        consultaTipoSolicitud()
        obtenerHistorial()
        completarSolicitud()
        
    }
    
})

window.onload = function() {
   
  };

//$('#vistaPDF').fadeOut();
//        $('#vista').fadeIn();
// cambiarUrlMicro() Y cambiarUrlNatural()
// si el estado cliente es igual a 2 el cliente ya registro la evaluacion por lo cual se redireeciona a modificar la evaluacion y a registrar una nueva solicitud
// el estado de la evaluacion debe estar en 1 para saber que es la evaluacion activa de la nueva solicitud
// la solicitud activa tiene como estadosoli = 3
// *** estadodoli del perfil del cliete es el estadoCliente de este archivo    **
// para el estadosoli de cliente se guarda actualiza a 2 en el registro de evaluacion micro para saber que se tiene que redireccionar a los formularios de solicitud micro
// en el caso de las evaluacion natural de guarda 3 en estadosoli del cliente para llamar a los formularios de solicitud natural
// cuando se registra una solicitud de cualquier tipo en estadodoli del perfil pasa a 4 
function cambiarUrlMicro(estado) {

    $.ajax({
        url: "/ClienteApp/consultaEvaluacionMicro/?idCliente=" + idCliente,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0") { 
                titulo.textContent = "Solicitud Personal"
                descipcion.textContent = "Progreso: Evaluacion de Microempresa"
                btnEvaluacioRepo.href = "../../../EvaluacionMicroApp/listaEvaluacionm/evaluacionIM/" + response[0]
                progresoEvaluacionRepo.classList.remove("progress-bar-dange")
                progresoEvaluacionRepo.classList.add("progress-bar-success")
                
                if (estadoCliente == "2") {
                    btnEvaluacion.href = "../../../EvaluacionMicroApp/listaEvaluacionm/editarEvaluacionm/" + response[0]
                    btnSolicitudCredito.href = "../../../EvaluacionMicroApp/listaEvaluacionm/solicitudMicro/" + idCliente

                    progresoEvaluacionMicro.classList.remove("progress-bar-dange")
                    progresoEvaluacionMicro.classList.add("progress-bar-success")
                    progreso++
                }
                if (parseInt(estadoCliente) > 3) {
                    $('#home-tab').fadeIn();   
                    

                    $('#btnDicom').fadeIn();
                    if(response[11] == "-0"){
                        btnDicom.href = "../../../HistorialApp/listaHis/registroHistCli/" + response[1]
                    }else{
                        btnDicom.href = "../../../HistorialApp/editHistCli/" + response[11]
                    }
                    $('#btnlistaChequeo').fadeIn();  
                    desactivarAlerta()
                    btnEvaluacion.href = "../../../EvaluacionMicroApp/listaEvaluacionm/editarEvaluacionm/" + response[0]
                    btnSolicitudCredito.href = "../../../SolicitudesApp/listaSoli/modificarSolicitudMicro/" + response[1]
                    idSoli = response[1]

                    progresoEvaluacionMicro.classList.remove("progress-bar-dange")
                    progresoEvaluacionMicro.classList.add("progress-bar-success")

                    progresoSoliMicro.classList.remove("progress-bar-dange")
                    progresoSoliMicro.classList.add("progress-bar-success")
                    descipcion.textContent = "Progreso: Solicitud registrada"                    
                    

                    titulo.textContent = "Solicitud para ingresos provenientes de microempresa"
                    btnSolicitudRepo.onclick=""
                    btnSolicitudRepo.href = "../../../SolicitudesApp/listaSC/solic/" + response[1] + "/" + idCliente
                    progresoSolicitudRepo.classList.remove("progress-bar-dange")
                    progresoSolicitudRepo.classList.add("progress-bar-success")
                    progreso=1.7
                    //alert((estadoCliente*10)+"%")
                    if (response[2] == "-0") {
                        btnConozCliente.href = "../../../SolicitudesApp/listaSC/ccliente/" + response[1]

                    } else {
                        btnConozCliente.href = "../../../ConozcaClienteApp/listaCC/editarCliente/" + response[2]
                        btnConozClienteRepo.onclick = ""
                        btnConozClienteRepo.href = "../../../ConozcaClienteApp/listaCC/conozcaC/" + response[2]
                        descipcion.textContent = "Progreso: formulario conozca a su cliente"

                        progresoConozcaCliente.classList.remove("progress-bar-danger")
                        progresoConozcaCliente.classList.add("progress-bar-success")
                        progresoConozcaClienteRepo.classList.remove("progress-bar-danger")
                        progresoConozcaClienteRepo.classList.add("progress-bar-success")
                        progreso=progreso+1.66
                    }

                    if (response[3] == "-0") {
                        btnDeclaracionJurada.href = "../../../SolicitudesApp/listaSC/declaracionjc/" + response[1]

                    } else {
                        btnDeclaracionJurada.href = "../../../DeclaracionJurClienteApp/listaDJ/editarDJ/" + response[3]
                        descipcion.textContent = "Progreso: Declaracion jurada cliente"
                        btnDeclaracionJuradaRepo.onclick = ""
                        btnDeclaracionJuradaRepo.href = "../../../DeclaracionJurClienteApp/listaDJ/declaracionjc/" + response[3] + "/" + idCliente

                        progresoDeclaracion.classList.remove("progress-bar-dange")
                        progresoDeclaracion.classList.add("progress-bar-success")
                        progresoDeclaracionRepo.classList.remove("progress-bar-dange")
                        progresoDeclaracionRepo.classList.add("progress-bar-success")
                        
                        progreso=progreso+1.66
                    }

                    if (response[4] == "-0") {
                        btnInscripcionSeguro.href = "../../../SolicitudesApp/listaSC/solicitudI/" + response[1]

                    } else {
                        btnInscripcionSeguro.href = "../../../SolicitudInscripcionSApp/listaIS/editarSIS/" + response[4]
                        descipcion.textContent = "Progreso: Inscripcion de seguro"
                        btnInscripcionSeguroRepo.onclick = ""
                        btnInscripcionSeguroRepo.href = "../../../SolicitudInscripcionSApp/listaIS/seguro/" + response[1]

                        progresoSeguro.classList.remove("progress-bar-dange")
                        progresoSeguro.classList.add("progress-bar-success")
                        progresoSeguroRepo.classList.remove("progress-bar-dange")
                        progresoSeguroRepo.classList.add("progress-bar-success")
                        progreso=progreso+1.66
                    }
                    if (tipoObra != "vivienda") { // **  mejora de vivienda
                        btnInspeccionLote.textContent = "Inspeccion vivienda"
                        if (response[5] == "-0") {
                            btnInspeccionLote.href = "../../../SolicitudesApp/listaSC/inspeccion/" + response[1]

                        } else {
                            btnInspeccionLote.href = "../../../InspeccionMejViviendaApp/listaIM/editarIM/" + response[5]
                            descipcion.textContent = "Progreso: Inspeccion vivienda"
                            progresoInspeccion.classList.remove("progress-bar-dange")
                            progresoInspeccion.classList.add("progress-bar-success")
// ***************************************************************  agregar link del reporte inspeccion mejora de vivienda ******************
                            btnInspeccionLoteRepo.href = "../../../InspeccionMejViviendaApp/listaIM/inspeccionM/" + response[5]
                            btnInspeccionLoteRepo.onclick = "" ; 
                            progresoInspeccionRepo.classList.remove("progress-bar-dange")
                            progresoInspeccionRepo.classList.add("progress-bar-success")

                            btnPrimeraInspeccion.onclick = "" ; 
                            $('#divubicacion1').fadeOut();
                            $('#divubicacion2').fadeOut();
                            $('#divubicacion3').fadeOut();
                            $('#divEsquema2').fadeOut();
                            $('#divEsquema3').fadeOut();
                            if(response[7] == "-0"){
                                btnPrimeraInspeccion.href = "../../../InspeccionMejViviendaApp/listaIM/pinspeccion/" +response[5] +"/PRIMERA"
                            }else{
                                btnSegundaInspeccion.onclick = ""
                                btnPrimeraInspeccion.href = "../../../InspeccionMejViviendaApp/listaPIM/editarPIM/" + response[7] 
                             

                                btnesquema1Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmU/"+ response[7] 
                                $('#divubicacion1').fadeOut();
                                btnPFotografico1Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmR/"+ response[7] 

                                if(response[8] == "-0"){
                                    btnSegundaInspeccion.href = "../../../InspeccionMejViviendaApp/listaIM/pinspeccion/" +response[5] +"/SEGUNDA"
                                }else{
                                    btnSegundaInspeccion.href = "../../../InspeccionMejViviendaApp/listaPIM/editarPIM/" + response[8] 
                                    btnesquema2Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmU/"+ response[8] 
                                    $('#divubicacion2').fadeOut();
                                    btnPFotografico2Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmR/"+ response[8] 
                                    btnTerceraInspeccion.onclick=""
                                    if(response[9] == "-0"){
                                        btnTerceraInspeccion.href = "../../../InspeccionMejViviendaApp/listaIM/pinspeccion/" +response[5] +"/TERCERA"
                                    }else{
                                        
                                        btnTerceraInspeccion.href ="../../../InspeccionMejViviendaApp/listaPIM/editarPIM/" + response[9] 
                                        btnesquema3Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmU/"+ response[9] 
                                $('#divubicacion3').fadeOut();
                                btnPFotografico3Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmR/"+ response[9] 
                                        
                                    }
                                }
                            }
                            progreso=progreso+1.66
                        }
                        //presupuesto
                        if (response[6] == "-0") {
                            btnPresupuestoVivienda.href = "../../../SolicitudesApp/listaSC/presupuesto/" + response[1]
                        } else {
                            btnPresupuestoVivienda.href = "../../../PresupuestoApp/listaPM/modPresupuesto/" + response[6]
                            descipcion.textContent = "Progreso: Presupuesto "
                            btnPresupuestoViviendaRepo.onclick = ""
                            btnPresupuestoViviendaRepo.href = "../../../PresupuestoApp/listaPM/presupuestoMj/" + response[6] //**** agregar aqui el link del reporte */

                            progresoPresupuesto.classList.remove("progress-bar-danger")
                            progresoPresupuesto.classList.add("progress-bar-success")
                            
                            progresoPresupuestoRepo.classList.remove("progress-bar-danger")
                            progresoPresupuestoRepo.classList.add("progress-bar-success")
                            
                            progreso=progreso+1.66
                        }
                        

                    } else {                     // *** para lote mas vivienda
                        if (response[5] == "-0") {
                            btnInspeccionLote.href = "../../../SolicitudesApp/listaSC/inspeccionl/" + response[1]

                        } else {
                            btnInspeccionLote.href = "../../../InspeccionLoteApp/listaI/editarIL/" + response[5]
                            descipcion.textContent = "Progreso: Inspeccion lote"
                            progresoInspeccion.classList.remove("progress-bar-dange")
                            progresoInspeccion.classList.add("progress-bar-success")


                            btnInspeccionLoteRepo.href = "../../../InspeccionLoteApp/listaI/inspeccionL/" + response[5]
                            btnInspeccionLoteRepo.onclick = "" ; 
                            progresoInspeccionRepo.classList.remove("progress-bar-dange")
                            progresoInspeccionRepo.classList.add("progress-bar-success")

                            btnPrimeraInspeccion.onclick = "" ; 
                            $('#divubicacion2').fadeOut();
                            $('#divubicacion3').fadeOut();
                            $('#divEsquema2').fadeOut();
                            $('#divEsquema3').fadeOut();
                            if(response[7] == "-0"){
                                btnPrimeraInspeccion.href = "../../../InspeccionLoteApp/listaI/pinspeccionl/" +response[5] +"/PRIMERA"
                            }else{
                                btnSegundaInspeccion.onclick = ""
                                btnPrimeraInspeccion.href = "../../../InspeccionLoteApp/listaPIL/editarPIL/" + response[7] 
                                

                                btnesquema1Repo.href = "../../../InspeccionLoteApp/listaPIL/pinspl/"+ response[7] 
                                btnUbicacion1Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplU/"+ response[7] 
                                btnPFotografico1Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplR/"+ response[7] 

                                if(response[8] == "-0"){
                                    btnSegundaInspeccion.href = "../../../InspeccionLoteApp/listaI/pinspeccionl/" +response[5] +"/SEGUNDA"
                                }else{
                                    btnSegundaInspeccion.href = "../../../InspeccionLoteApp/listaPIL/editarPIL/" + response[8] 
                                   btnesquema2Repo.href = "../../../InspeccionLoteApp/listaPIL/pinspl/"+ response[8] 
                                btnUbicacion2Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplU/"+ response[8] 
                                btnPFotografico2Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplR/"+ response[8] 

                                    btnTerceraInspeccion.onclick=""
                                    if(response[9] == "-0"){
                                        btnTerceraInspeccion.href = "../../../InspeccionLoteApp/listaI/pinspeccionl/" +response[5] +"/TERCERA"
                                    }else{
                                        
                                        btnTerceraInspeccion.href ="../../../InspeccionLoteApp/listaPIL/editarPIL/" + response[9] 
                                       btnesquema3Repo.href = "../../../InspeccionLoteApp/listaPIL/pinspl/"+ response[9] 
                                btnUbicacion3Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplU/"+ response[9] 
                                btnPFotografico3Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplR/"+ response[9] 

                                        
                                    }
                                }
                            }
                            progreso=progreso+1.66
                        }

                        //presupuesto
                        if (response[6] == "-0") { 
                            btnPresupuestoVivienda.href = "../../../SolicitudesApp/listaSC/presupuestov/" + response[1]
                        } else {
                            btnPresupuestoVivienda.href = "../../../PresupuestoVApp/listaPV/editarPV/" + response[6]
                            descipcion.textContent = "Progreso: Presupuesto "
                            btnPresupuestoViviendaRepo.onclick = ""
                            btnPresupuestoViviendaRepo.href = "../../../PresupuestoVApp/listaPV/presupuestoVv/" + response[6]

                            progresoPresupuesto.classList.remove("progress-bar-danger")
                            progresoPresupuesto.classList.add("progress-bar-success")
                            progresoPresupuestoRepo.classList.remove("progress-bar-danger")
                            progresoPresupuestoRepo.classList.add("progress-bar-success")
                            $('#trObras').fadeIn();
                            $('#trObrasRepo').fadeIn();
                            btnObrasAdicionales.onclick = ""
                            if(response[12] == "-0"){
                                btnObrasAdicionales.href="../../../PresupuestoVApp/listaPV/presupuestovoa/" + response[6]
                            }else{
                                btnObrasAdicionales.href="../../../PresupuestoVApp/listaPVO/editarPVO/"  + response[12]
                                progresoObrasAdd.classList.remove("progress-bar-danger")
                                progresoObrasAdd.classList.add("progress-bar-success")

                                btnObrasAdicionalesRepo.onclick = ""
                                btnObrasAdicionalesRepo.href = "../../../PresupuestoVApp/listaPVO/presupuestoVvO/" + response[12]
                                progresoObrasAdicionalesRepo.classList.remove("progress-bar-danger")                                
                                progresoObrasAdicionalesRepo.classList.add("progress-bar-success")
                            }

                            progreso=progreso+1.66
                        }               
                    }
                    if(response[10] != "-0"){
                        btnlistaChequeo.href = "../../../ListaChequeoApp/listaC/editarCheq/" + response[10]
                        btnListaChequeoRepo.href = "../../../ListaChequeoApp/listaC/listaCheq/" + response[10]
                        $('#divlistaChequeoRepo').fadeIn();
                    }else{
                        btnlistaChequeo.disabled="true"
                    }
                    progresoSolicitud.ariaValueNow = (progreso * 10) + ""
                    progresoSolicitud.style.width = (progreso * 10) + "%"
                    
                }
                aprobada(estado)
                return progreso
            }

            if (response == "-0")
                return
            //alertA("Complete la evaluacion primero")

        },
        error: function (error) {
            alertE("nurl micro")
        }
    });

}

function cambiarUrlNatural(estado) {

    $.ajax({
        url: "/ClienteApp/consultaEvaluacionNatural/?idCliente=" + idCliente,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0") { 
                titulo.textContent = "Solicitud Personal"
                descipcion.textContent = "Progreso: Evaluacion de Ingresos vs Egresos"
                btnEvaluacioRepo.href = "../../../EvaluacionIvEFApp/listaEvaluacion/evaluacionIvEF/" + response[0]
                progresoEvaluacionRepo.classList.remove("progress-bar-dange")
                progresoEvaluacionRepo.classList.add("progress-bar-success")
                
                if (estadoCliente == "3") {
                    progresoEvaluacionMicro.classList.remove("progress-bar-dange")
                    progresoEvaluacionMicro.classList.add("progress-bar-success")

                    btnEvaluacion.href = "../../../EvaluacionIvEFApp/listaEvaluacion/editarEvaluacion/" + response[0]
                    btnSolicitudCredito.href = "../../../EvaluacionIvEFApp/listaEvaluacion/solicitudNatu/" + idCliente
                    progreso++
                }
                if (parseInt(estadoCliente) > 3) {
                    $('#home-tab').fadeIn();   

                    
                    
                    $('#btnDicom').fadeIn();
                    $('#btnlistaChequeo').fadeIn();  
                    if(response[11] == "-0"){
                        btnDicom.href = "../../../HistorialApp/listaHis/registroHistCli/" + response[1]
                    }else{
                        btnDicom.href = "../../../HistorialApp/editHistCli/" + response[11]
                    }
                    desactivarAlerta()
                    btnEvaluacion.href = "../../../EvaluacionIvEFApp/listaEvaluacion/editarEvaluacion/" + response[0]
                    btnSolicitudCredito.href = "../../../NaturalApp/listarSN/editarSolicitudN/" + response[1]
                    idSoli = response[1]

                    progresoEvaluacionMicro.classList.remove("progress-bar-dange")
                    progresoEvaluacionMicro.classList.add("progress-bar-success")

                    progresoSoliMicro.classList.remove("progress-bar-dange")
                    progresoSoliMicro.classList.add("progress-bar-success")
                    descipcion.textContent = "Progreso: Solicitud registrada"
                    btnSolicitudRepo.onclick=""
                    btnSolicitudRepo.href = "../../../NaturalApp/listarSNC/soliPer/" + response[1]
                    progresoSolicitudRepo.classList.remove("progress-bar-dange")
                    progresoSolicitudRepo.classList.add("progress-bar-success")
                    progreso=1.7
                    if (response[2] == "-0") {
                        btnConozCliente.href = "../../../NaturalApp/listarSNC/ccliente/" + response[1]

                    } else {
                        btnConozCliente.href = "../../../ConozcaClienteApp/listaCC/editarCliente/" + response[2]
                        descipcion.textContent = "Progreso: formulario conozca a su cliente"
                        btnConozClienteRepo.onclick = ""
                        btnConozClienteRepo.href = "../../../ConozcaClienteApp/listaCC/conozcaC/" + response[2]

                        progresoConozcaCliente.classList.remove("progress-bar-dange")
                        progresoConozcaCliente.classList.add("progress-bar-success")
                        progresoConozcaClienteRepo.classList.remove("progress-bar-dange")
                        progresoConozcaClienteRepo.classList.add("progress-bar-success")
                        progreso=progreso+1.66
                    }

                    if (response[3] == "-0") {
                        btnDeclaracionJurada.href = "../../../NaturalApp/listarSNC/declaracionjc/" + response[1]

                    } else {
                        btnDeclaracionJurada.href = "../../../DeclaracionJurClienteApp/listaDJ/editarDJ/" + response[3]
                        descipcion.textContent = "Progreso: Declaracion jurada cliente"
                        btnDeclaracionJuradaRepo.onclick = ""
                        btnDeclaracionJuradaRepo.href = "../../../DeclaracionJurClienteApp/listaDJ/declaracionjc/" + response[3] + "/" + idCliente

                        progresoDeclaracion.classList.remove("progress-bar-dange")
                        progresoDeclaracion.classList.add("progress-bar-success")
                        progresoDeclaracionRepo.classList.remove("progress-bar-dange")
                        progresoDeclaracionRepo.classList.add("progress-bar-success")
                        progreso=progreso+1.66
                    }

                    if (response[4] == "-0") {
                        btnInscripcionSeguro.href = "../../../NaturalApp/listarSNC/solicitudI/" + response[1]

                    } else {
                        btnInscripcionSeguro.href = "../../../SolicitudInscripcionSApp/listaIS/editarSIS/" + response[4]
                        descipcion.textContent = "Progreso: Inscripcion de seguro"
                        btnInscripcionSeguroRepo.onclick = ""
                        btnInscripcionSeguroRepo.href = "../../../SolicitudInscripcionSApp/listaIS/seguro/" + response[1]

                        progresoSeguro.classList.remove("progress-bar-dange")
                        progresoSeguro.classList.add("progress-bar-success")
                        progresoSeguroRepo.classList.remove("progress-bar-dange")
                        progresoSeguroRepo.classList.add("progress-bar-success")
                        progreso=progreso+1.66
                    }
                    if (tipoObra != "vivienda") { //  mejora de vivienda
                        btnInspeccionLote.textContent = "Inspeccion vivienda"
                        if (response[5] == "-0") {
                            btnInspeccionLote.href = "../../../SolicitudesApp/listaSC/inspeccion/" + response[1]

                        } else {
                            btnInspeccionLote.href = "../../../InspeccionMejViviendaApp/listaIM/editarIM/" + response[5]
                           descipcion.textContent = "Progreso: Inspeccion vivienda"
                            progresoInspeccion.classList.remove("progress-bar-dange")
                            progresoInspeccion.classList.add("progress-bar-success")

                            // ***************************************************************  agregar link del reporte inspeccion mejora de vivienda ******************
                            
                            btnInspeccionLoteRepo.href = "../../../InspeccionMejViviendaApp/listaIM/inspeccionM/" + response[5]
                            btnInspeccionLoteRepo.onclick = "" ; 
                            progresoInspeccionRepo.classList.remove("progress-bar-dange")
                            progresoInspeccionRepo.classList.add("progress-bar-success")

                            btnPrimeraInspeccion.onclick = "" ; 
                            $('#divubicacion1').fadeOut();
                            $('#divubicacion2').fadeOut();
                            $('#divubicacion3').fadeOut();
                            $('#divEsquema2').fadeOut();
                            $('#divEsquema3').fadeOut();
                            if(response[7] == "-0"){
                                btnPrimeraInspeccion.href = "../../../InspeccionMejViviendaApp/listaIM/pinspeccion/" +response[5] +"/PRIMERA"
                            }else{
                                btnSegundaInspeccion.onclick = ""
                                btnPrimeraInspeccion.href = "../../../InspeccionMejViviendaApp/listaPIM/editarPIM/" + response[7] 
                               

                                btnesquema1Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmU/" + response[7] 
                               
                                btnPFotografico1Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmR/" + response[7] 


                                if(response[8] == "-0"){
                                    btnSegundaInspeccion.href = "../../../InspeccionMejViviendaApp/listaIM/pinspeccion/" +response[5] +"/SEGUNDA"
                                }else{
                                    btnSegundaInspeccion.href = "../../../InspeccionMejViviendaApp/listaPIM/editarPIM/" + response[8] 
                                    btnesquema2Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmU/"+ response[8] 
                                   
                                    btnPFotografico2Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmR/"+ response[8] 
                                    
                                    btnTerceraInspeccion.onclick=""
                                    if(response[9] == "-0"){
                                        btnTerceraInspeccion.href = "../../../InspeccionMejViviendaApp/listaIM/pinspeccion/" +response[5] +"/TERCERA"
                                    }else{
                                        
                                        btnTerceraInspeccion.href ="../../../InspeccionMejViviendaApp/listaPIM/editarPIM/" + response[9] 
                                    btnesquema3Repo.href = "../../../InspeccionMejViviendaApp/listaPIM/pinspmU/"+ response[9] 
                               
                                
                                        
                                    }
                                }
                            }
                            progreso=progreso+1.66
                        //presupuesto
                        if (response[6] == "-0") {
                            btnPresupuestoVivienda.href = "../../../SolicitudesApp/listaSC/presupuesto/" + response[1]
                        } else {
                            btnPresupuestoVivienda.href = "../../../PresupuestoApp/listaPM/modPresupuesto/" + response[6]
                            descipcion.textContent = "Progreso: Presupuesto "
                            btnPresupuestoViviendaRepo.onclick = ""
                            btnPresupuestoViviendaRepo.href = "../../../PresupuestoApp/listaPM/presupuestoMj/" + response[6] //**** agregar aqui el link del reporte */

                            progresoPresupuesto.classList.remove("progress-bar-dange")
                            progresoPresupuesto.classList.add("progress-bar-success")
                            progresoPresupuestoRepo.classList.remove("progress-bar-dange")
                            progresoPresupuestoRepo.classList.add("progress-bar-success")
                            
                            progreso=progreso+1.66
                        }
                        }
                    } else {
                        if (response[5] == "-0") {// inspeccion lote 
                            btnInspeccionLote.href = "../../../SolicitudesApp/listaSC/inspeccionl/" + response[1]

                        } else {
                            btnInspeccionLote.href = "../../../InspeccionLoteApp/listaI/editarIL/" + response[5]
                            descipcion.textContent = "Progreso: Inspeccion lote"
                            progresoInspeccion.classList.remove("progress-bar-dange")
                            progresoInspeccion.classList.add("progress-bar-success")

                            // ***************************************************************  agregar link del reporte inspeccion mejora de vivienda ******************
                            btnInspeccionLoteRepo.href = "../../../InspeccionLoteApp/listaI/inspeccionL/" + response[5]
                            btnInspeccionLoteRepo.onclick = "" ; 
                            progresoInspeccionRepo.classList.remove("progress-bar-dange")
                            progresoInspeccionRepo.classList.add("progress-bar-success")

                            btnPrimeraInspeccion.onclick = "" ; 
                            $('#divubicacion2').fadeOut();
                            $('#divubicacion3').fadeOut();
                            $('#divEsquema2').fadeOut();
                            $('#divEsquema3').fadeOut();
                            if(response[7] == "-0"){
                                btnPrimeraInspeccion.href = "../../../InspeccionLoteApp/listaI/pinspeccionl/" +response[5] +"/PRIMERA"
                            }else{
                                btnSegundaInspeccion.onclick = ""
                                btnPrimeraInspeccion.href = "../../../InspeccionLoteApp/listaPIL/editarPIL/" + response[7] 
                                

                                btnesquema1Reposquema1Repo.href = "../../../InspeccionLoteApp/listaPIL/pinspl/" + response[7] 
                                btnUbicacion1Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplU/" + response[7] 
                                btnPFotografico1Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplR/" + response[7] 


                                if(response[8] == "-0"){
                                    btnSegundaInspeccion.href = "../../../InspeccionLoteApp/listaI/pinspeccionl/" +response[5] +"/SEGUNDA"
                                }else{
                                    btnSegundaInspeccion.href = "../../../InspeccionLoteApp/listaPIL/editarPIL/" + response[8] 
                                    btnesquema2Repo.href = "../../../InspeccionLoteApp/listaPIL/pinspl/"+ response[8] 
                                btnUbicacion2Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplU/"+ response[8] 
                                btnPFotografico2Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplR/"+ response[8] 

                                    btnTerceraInspeccion.onclick=""
                                    if(response[9] == "-0"){
                                        btnTerceraInspeccion.href = "../../../InspeccionLoteApp/listaI/pinspeccionl/" +response[5] +"/TERCERA"
                                    }else{
                                        
                                        btnTerceraInspeccion.href ="../../../InspeccionLoteApp/listaPIL/editarPIL/" + response[9] 
                                       btnesquema3Repo.href = "../../../InspeccionLoteApp/listaPIL/pinspl/"+ response[9] 
                                btnUbicacion3Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplU/"+ response[9] 
                                btnPFotografico3Repo.href = "../../../InspeccionLoteApp/listaPIL/pinsplR/"+ response[9] 

                                    }
                                }
                            }
                            progreso=progreso+1.66
                        }

                        //presupuesto
                        if (response[6] == "-0") {
                            btnPresupuestoVivienda.href = "../../../SolicitudesApp/listaSC/presupuestov/" + response[1]
                        } else {
                            btnPresupuestoVivienda.href = "../../../PresupuestoVApp/listaPV/editarPV/" + response[6]
                            descipcion.textContent = "Progreso: Presupuesto Vivienda"
                            btnPresupuestoViviendaRepo.onclick = ""
                            btnPresupuestoViviendaRepo.href = "../../../PresupuestoVApp/listaPV/presupuestoVv/" + response[6] //**** agregar aqui el link del reporte */

                            progresoPresupuesto.classList.remove("progress-bar-dange")
                            progresoPresupuesto.classList.add("progress-bar-success")
                            progresoPresupuestoRepo.classList.remove("progress-bar-dange")
                            progresoPresupuestoRepo.classList.add("progress-bar-success")
                            
                            $('#trObras').fadeIn();
                            $('#trObrasRepo').fadeIn();
                            btnObrasAdicionales.onclick = ""
                            if(response[12] == "-0"){
                                btnObrasAdicionales.href="../../../PresupuestoVApp/listaPV/presupuestovoa/" + response[6]
                            }else{
                                btnObrasAdicionales.href="../../../PresupuestoVApp/listaPVO/editarPVO/"  + response[12]
                                progresoObrasAdd.classList.remove("progress-bar-danger")
                                progresoObrasAdd.classList.add("progress-bar-success")

                                btnObrasAdicionalesRepo.onclick = ""
                                btnObrasAdicionalesRepo.href = "../../../PresupuestoVApp/listaPVO/presupuestoVvO/" + response[12]
                                btnObrasAdicionalesRepo.classList.remove("progress-bar-danger")                                
                                btnObrasAdicionalesRepo.classList.add("progress-bar-success")
                            }


                            progreso=progreso+1.66
                        }
                       
                    }

                    if(response[10] != "-0"){
                        btnlistaChequeo.href = "../../../ListaChequeoApp/listaC/editarCheq/" + response[10]
                        btnListaChequeoRepo.href = "../../../ListaChequeoApp/listaC/listaCheq/" + response[10]
                        $('#divlistaChequeoRepo').fadeIn();
                    }else{
                        btnlistaChequeo.disabled="true"
                    }

                    progresoSolicitud.ariaValueNow = (progreso * 10) + ""
                    progresoSolicitud.style.width = (progreso * 10) + "%"
                    //alert(progreso)
                }
                aprobada(estado)
                return progreso
            }

            if (response == "-0")
                return
        },
        error: function (error) {
            alertE("no paso")
        }
    });

}

function solicitudVencida(fecha) {
    if(fecha != null){
        let actual = new Date();
        let f = Date.parse(fecha);
        let plazo = 1000 * 60 * 60 * 24 * 30
        let fechaMaxima = new Date(f.getTime()+plazo)   
    
        if(fechaMaxima.getTime() > actual.getTime()){
            return 0
        }        
        return 1
    }else{ return 0}
    

}

function consultaTipoSolicitud() {
   
    $.ajax({
        url: "/ClienteApp/consultaTipoSolicitud/?idCliente=" + idCliente,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0")
                tipoObra = response[0].fields.tipoobra
            
            if (response[0].fields.estadosoli == 6) {
                progresoSolicitud.classList.remove("progress-bar-striped")
                progresoSolicitud.classList.add("progress-bar-danger")
                progresoSolicitud.ariaValueNow = (100) + ""
                progresoSolicitud.style.width = (100) + "%"
                titulo.textContent = "Solicitud Negada"
                descipcion.textContent =response[0].fields.observaciones    // "El porcentaje de DICOM obtenido es mayor al requerido para continuar"
                $('#nueva-soli').fadeIn();
                roleIniciar.classList.add("active")
                panelIniciar.classList.remove("fade")
                panelIniciar.classList.add("active")
                $('#btnDicom').fadeIn();
                $('#btnlistaChequeo').fadeOut();
                btnDicom.textContent="Actualizar DICOM"
//**************************** AGREGAR AQUI EL LINK PARA ACTUALIZA EL DICOM */     
        
                btnDicom.href = "../../../HistorialApp/editHistCli/" +  response[0].pk
            } else {    
                if(solicitudVencida(response[0].fields.fecha) == 1){
                    denegarSolicitud(response[0].pk)
                }

                btnlistaChequeo.href = "../../../ListaChequeoApp/listaPC/listaChequeov/" + response[0].pk
                $('#reportes-tab2').fadeIn();
                $('#formularios-tab2').fadeIn();      
                if (response[0].fields.tipo == "natural") {   
                    idSoli = response[0].pk
                    roleFormularios.classList.add("active")
                    panelFormularios.classList.remove("fade")
                    panelFormularios.classList.add("active")                   
                    ActualizarNombresFormularios()                   
                    cambiarUrlNatural(response[0].fields.estadosoli)
                } else {   
                    idSoli = response[0].pk
                    roleFormularios.classList.add("active")
                    panelFormularios.classList.remove("fade")
                    panelFormularios.classList.add("active")                    
                    cambiarUrlMicro(response[0].fields.estadosoli)
                }
               
            }
            //alert('hola  '+response[0].fields.tipo)

            if (response == "-0")
                return
        },
        error: function (error) {
            alert("no paso consulta tipo solicitud "+ error )
        }
    });
}

function aprobada(estado){
    if( estado == 3){
        progresoSolicitud.ariaValueNow = (100) + ""
        progresoSolicitud.style.width = (100) + "%"

        titulo.textContent = "Solicitud Completada"
        descipcion.textContent = "Pendiente de aprobación"

        $('#inspecciones').fadeIn();
        $('#formularios-tab2').fadeOut();
        roleReporte.classList.add("active")
        panelReporte.classList.remove("fade")
        panelReporte.classList.add("active")  
        panelFormularios.classList.remove("active")
        panelFormularios.classList.add("fade")
        return "ok"
    }
}

function desactivarAlerta() {
    btnConozCliente.onclick = ""
    btnDeclaracionJurada.onclick = ""
    btnInscripcionSeguro.onclick = ""
    btnInspeccionLote.onclick = ""
    btnPresupuestoVivienda.onclick = ""
}

function ActualizarNombresFormularios(){
     btnEvaluacion.textContent = "Evaluacion"
     btnSolicitudCredito = document.getElementById("btnSolicitudCredito")
     btnConozCliente = document.getElementById("btnConozCliente")
     btnDeclaracionJurada = document.getElementById("btnDeclaracionJurada")
     btnInscripcionSeguro = document.getElementById("btnInscripcionSeguro")
     btnInspeccionLote = document.getElementById("btnInspeccionLote")
     btnPresupuestoVivienda = document.getElementById("btnPresupuestoVivienda")
}


function vistaPrevia(archivo) {
    let reader = new FileReader()
    vista = archivo.id + "Vista"
    tipo = archivo.files[0].type
    reader.readAsDataURL(archivo.files[0])

    reader.onload = function (e) {
        if (tipo == 'image/jpeg' || tipo == 'image/png') {

            document.getElementById(vista).src = e.target.result;

            registrarDocumento(archivo);
        }
        if (tipo == "application/pdf") {
            registrarDocumento(archivo);
            // $('#vista').fadeOut();
            // $('#vistaPDF').fadeIn();
            // document.getElementById('vista').src = "";
            // document.getElementById('vistaPDF').src = e.target.result;
        };

    }


}

function registrarDocumento(archivo) {
    var archivodt = new FormData()
    archivodt.append("archivo", archivo.files[0])
    $.ajax({
        url: "/ClienteApp/registrarDocumento/?idCliente=" + idCliente + "&fecha=" + obtenerFecha() + "&archivo=" + archivo.value + "&nombreD=" + archivo.id + "&ids=" + idSoli,
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        dataType: "json",
        data: archivodt,
        contentType: false,
        processData: false,
        success: function (response) {

            if (response != "-0") {
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: 'Documento Guardado',
                    showConfirmButton: false,
                    showClass: {
                        popup: 'animate__animated animate__fadeInDown'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOutUp'
                    },
                    timer: 1500
                })
            }
           
        },
        error: function (error) {
            alertE("registro documento "+ error)
        }
    });
}

function obtenerHistorial() {
    $.ajax({
        url: "/ClienteApp/obtenerHistorial/?idCliente=" + idCliente,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0"){
                $('#historial-tab2').fadeIn();
                panelHistorial.classList.remove("fade")
                panelHistorial.classList.add("active")
                let estado=""
                let tipo=""
                let historial = JSON.parse(response);
                for (i = 0; i < historial.length; i++) {
                    if(historial[i].estado==4) {estado="Aprobado"}
                    if(historial[i].estado==6) {estado="Negado"}
                    if(historial[i].estado==7) {estado="Vencido"}
                    if(historial[i].tipo=="micro") {tipo="Microempresa"}else{ tipo="Personal" }

                    let filamo = '<tr id="' + historial[i].id + '"><td>' + (i+1)+ '</td><td>' +historial[i].monto+ '</td><td>' +
                    historial[i].fecha + '</td><td>' + tipo + '</td><td>' + historial[i].tipoObra + '</td><td>' + estado+ '</td></tr>'; //esto seria lo que contendria la fila
                    $('#tablaHistorial tbody').append(filamo);
                }
            }
                
          
            if (response == "-0")
                return
        },
        error: function (error) {
            alert("obtener historial " + error )
        }
    });
}

function completarSolicitud() {
    
    $.ajax({
        url: "/ClienteApp/completarSolicitud?idCliente=" + idCliente  ,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0"){
                if (response == "si"){
                    alertC("Solicitud completada")
                    completarSolicitudBase(idCliente)
                }
            }
                
          
            if (response == "-0")
                return
        },
        error: function (error) {
           // alert("completar solicitus " + error)
        }
    });
}

function completarSolicitudBase() {
    $.ajax({
        url: "/ClienteApp/completarSolicitudBase?idCliente=" + idCliente  ,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0"){
                location. reload()
            }
                
          
            if (response == "-0")
                return
        },
        error: function (error) {
        }
    });
}

function denegarSolicitud(idSoli) {
    $.ajax({
        url: "/ClienteApp/denegarSolicitud?idSoli=" + idSoli  ,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0"){
                location. reload()
            }
                
          
            if (response == "-0")
                return
        },
        error: function (error) {
            
        }
    });
}

function obtenerFecha() {
    let fecha = new Date();
    let f = fecha.getDate() + "/" + (fecha.getMonth() + 1) + "/" + fecha.getFullYear();
    return f

}
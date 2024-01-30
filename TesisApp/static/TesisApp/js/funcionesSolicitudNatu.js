function validarDatosN() {
    if (document.getElementById("nombreS").value.length == 0 &&
      document.getElementById("apellidoS").value.length == 0 &&
      document.getElementById("duiS").value.length == 0 &&
      document.getElementById("fechExS").value.length == 0 &&
      document.getElementById("fechNaS").value.length == 0 &&
      document.getElementById("edadS").value.length == 0 &&
      document.getElementById("estadoCivilS").value.length == 0 &&
      document.getElementById("generoS").value.length == 0 &&
      document.getElementById("profecionS").value.length == 0 
    ) {
      return 0;
    } else {
      return 1;
      //alertA('Datos personales no completados');
     
    }

  }

  function validarDatosNC() {
    if (document.getElementById("nombreC").value.length == 0 &&
        document.getElementById("apellidoC").value.length == 0 &&
        document.getElementById("duiC").value.length == 0 &&
        document.getElementById("fechExC").value.length == 0 &&
        document.getElementById("fechNaC").value.length == 0 &&
        document.getElementById("edadC").value.length == 0 &&
        document.getElementById("profecionC").value.length == 0 ) {
        return 0;
      } else {
        return 1;
      }
  }

  function validarGrupoFN() {
    pass = 1;
    for (i = 0; i < document.getElementsByName('nombreGP').length; i++) {
      if (
        document.getElementsByName('nombreGP')[i].value.length == 0 &&
        document.getElementsByName('edadGP')[i].value.length == 0 &&
        document.getElementsByName('salarioGP')[i].value.length == 0 &&
        document.getElementsByName('trabajoGP')[i].value.length == 0 &&
        document.getElementsByName('parentescoGP')[i].value.length == 0 
      ) {
        pass = 0;
      } else {
        if (document.getElementsByName('nombreGP')[i].value.length == 0 &&
          document.getElementsByName('edadGP')[i].value.length == 0 &&
          document.getElementsByName('salarioGP')[i].value.length == 0 &&
          document.getElementsByName('trabajoGP')[i].value.length == 0 &&
          document.getElementsByName('parentescoGP')[i].value.length == 0 && i != 0) {
          pass = 0;
        } else {
          //alertA('Grupo familiar no completado');
          return 1;
        }

      }
    }
    return pass;

  }

  function validarDomicilioNatural() {
    if (document.getElementById("direActS").value.length == 0 &&
      document.getElementById("puntoRefS").value.length == 0 &&
      document.getElementById("telefonoS").value.length == 0 &&
      document.getElementById("resideS").value.length == 0 &&
      document.getElementById("condicionS").value.length == 0 &&
      document.getElementById("lugrTrabS").value.length == 0 &&
      document.getElementById("jefeS").value .length == 0 &&
      document.getElementById("tiempoS").value.length == 0 &&
      document.getElementById("salarioS").value.length == 0 &&
      document.getElementById("direccionNS").value.length == 0 &&
      document.getElementById("telefonoNS").value.length == 0 
    ) { return 0; } else {
      // alertA('Datos de domicilio y lugar de microempresa no completados');
      return 1;
    }
  }

  function validarDomicilioCNatural() {
   
    if (document.getElementById("direActC").value.length == 0 &&
      document.getElementById("puntoRefC").value.length == 0 &&
      document.getElementById("telefonoC").value.length == 0 &&
      document.getElementById("resideC").value.length == 0 &&
      document.getElementById("condicionC").value.length == 0 &&
      document.getElementById("lugrTrabC").value.length == 0 &&
      document.getElementById("jefeC").value.length == 0 &&
      document.getElementById("tiempoC").value.length == 0 &&
      document.getElementById("salarioC").value.length == 0 &&
      document.getElementById("direccionNC").value.length == 0 &&
      document.getElementById("telefonoNC").value.length == 0 
    ) { return '0'; } else {
      // alertA('Datos de domicilio y lugar de microempresa no completados');
      return 1;
    }
  }
 

  function validarDatosObraN() {
    if (document.getElementById("destinoNE").value.length == 0 &&
      document.getElementById("duenoNE").value.length == 0 &&
      document.getElementById("parentescoNE").value.length == 0 &&
      document.getElementById("detalleObra").value.length == 0 &&
      document.getElementById("PresupuestoNE").value.length == 0 
    ) { return 0; } else {
      //alertA('Datos de obra no completados');
      return 1;
    }
  }

  function validarDetalleN() {
    if (document.getElementById("montoNE").value.length == 0 &&
      document.getElementById("plazoNE").value.length == 0 &&
      document.getElementById("cuotaNE").value.length == 0 &&
      document.getElementById("FechaPagoNE").value.length == 0 
    ) { return 0; } else {
      //alertA('Detalles de la no completados');
      return 1;
    }
  }

  function validarExpeCrediN() {
    pass = 1;
    for (i = 0; i < document.getElementsByName('lugarEC').length; i++) {
      if (
        document.getElementsByName('lugarEC')[i].value.length == 0 &&
        document.getElementsByName('montoEC')[i].value.length == 0 &&
        document.getElementsByName('fechaEC')[i].value.length == 0 &&
        document.getElementsByName('estadoEC')[i].value.length == 0 &&
        document.getElementsByName('cuotaEC')[i].value.length == 0 
      ) {
        pass = 0;
      } else {
        if (document.getElementsByName('lugarEC')[i].value.length == 0 &&
          document.getElementsByName('montoEC')[i].value.length == 0 &&
          document.getElementsByName('fechaEC')[i].value.length == 0 &&
          document.getElementsByName('estadoEC')[i].value.length == 0 &&
          document.getElementsByName('cuotaEC')[i].value.length == 0 && i != 0) {
          pass = 0;
        } else {
          //alertA('Experiencia crediticia no completada');
          return 1;
        }

      }
    }
    return pass;

  }

  function validarReferenciasPFN() {
    pass = 1;
    for (i = 0; i < document.getElementsByName('nombreRPF').length; i++) {
      if (
        document.getElementsByName('nombreRPF')[i].value.length == 0 &&
        document.getElementsByName('parentescoRPF')[i].value.length == 0 &&
        document.getElementsByName('domicilioRPF')[i].value.length == 0 &&
        document.getElementsByName('telefonoRPF')[i].value.length == 0 
      ) {
        pass = 0;
      } else {
        if (document.getElementsByName('nombreRPF')[i].value.length == 0 &&
          document.getElementsByName('parentescoRPF')[i].value.length == 0 &&
          document.getElementsByName('domicilioRPF')[i].value.length == 0 &&
          document.getElementsByName('telefonoRPF')[i].value.length == 0 && i != 0) {
          pass = 0;
        } else {

          return 1;
        }

      }
    }
    return pass;

  }

  function validarComentariosN() {
    if (document.getElementById("comIniciativa").value.length == 0 &&
      document.getElementById("comEvaluacion").value.length == 0 &&
      document.getElementById("comGarantia").value.length == 0 
    ) { return 0; } 
    else {
     if(document.getElementById("comIniciativa").value != "" &&
     document.getElementById("comEvaluacion").value != "" &&
     document.getElementById("comGarantia").value != ""  ){
      return 1;
     }
      return 0;
    }
  }


// validando fechas
function validarFechaExpN(fecha) {
    var actual = new Date();
    var f = Date.parse(fecha.value);
    var anio = actual.getFullYear();
    var mes = actual.getMonth();
    var dia = actual.getDate();

    if (f.getFullYear() > anio) {
      alertE("Ingrese una fecha valida ");
      fecha.value = "";
    } else {
      if (f.getMonth() > mes && f.getFullYear() == anio) {
        alertE("Ingrese una fecha valida ");
        fecha.value = "";
      } else {
        if (f.getDate() > dia && f.getMonth() == mes) {
          alertE("Ingrese una fecha valida ");
          fecha.value = "";
        }
      }
    }
  }  

function validarFechaNacN(fecha) {
    var actual = new Date();
    var f = Date.parse(fecha.value);
    var anio = actual.getFullYear();
    var mes = actual.getMonth();
    var dia = actual.getDate();

    if ((anio - f.getFullYear()) < 18) {
      alertE("Ingrese una fecha de nacimiento valida ");
      fecha.value = "";
    } else {
      if ((anio - f.getFullYear() == 18)) {
        if (f.getMonth() > mes) {
          alertE("Ingrese una fecha de nacimiento valida");
          fecha.value = "";
        } else {
          if (f.getDate() > dia) {
            alertE("Ingrese una fecha de nacimiento valida");
            fecha.value = "";
          } else {
            if (fecha.id == "fechNaS") {
              document.getElementById("edadS").value = calcularEdad(dia, mes, anio, f)
            } else {
              document.getElementById("edadC").value = calcularEdad(dia, mes, anio, f)
            }
          }
        }
      } else {
        if (fecha.id == "fechNaS") {
          document.getElementById("edadS").value = calcularEdad(dia, mes, anio, f)
        } else {
          document.getElementById("edadC").value = calcularEdad(dia, mes, anio, f)
        }
      }
    }
  }


  function calcularEdad(dia, mes, anio, f) {
    if (f.getMonth() == mes) {
      if (f.getDate() > dia) {
        return (anio - f.getFullYear()) - 1
      } else {
        return (anio - f.getFullYear())
      }
    } else {
      if (f.getMonth() > mes) {
        return (anio - f.getFullYear()) - 1
      } else {
        return (anio - f.getFullYear())
      }
    }
  }

  function validarEdadGPN(edad) {
    if (edad.value < 18) {
      Swal.fire({
        position: 'top-end',
        icon: 'warning',
        title: 'Solo puede ingrasar personas mayores de edad',
        showConfirmButton: false,
        showClass: {
          popup: 'animate__animated animate__fadeInDown'
        },
        hideClass: {
          popup: 'animate__animated animate__fadeOutUp'
        },
        timer: 1500
      })
      edad.value = "";
    }
    if (edad.value > 65) {
      Swal.fire({
        position: 'top-end',
        icon: 'warning',
        title: 'Solo puede ingrasar personas mayores de edad y menores de 70 años',
        showConfirmButton: false,
        showClass: {
          popup: 'animate__animated animate__fadeInDown'
        },
        hideClass: {
          popup: 'animate__animated animate__fadeOutUp'
        },
        timer: 1500
      })
      edad.value = "";
    }
  }

//validando salario
function validarSalarioGPFN(salario) {
    if (salario.value < 0) {
      alertE('Ingrese un valor valido');
      salario.value = "";
    }
  }

 //otros
 function validarTel(tel) {
    var num = tel.value.length;
    var primer = tel.value;
    if (num == 4)
      tel.value = tel.value + '-';

    if (num == 1) {
      if (primer == '2' || primer == '7' || primer == "6")
        return
      else {
        tel.value = "";
        tel.title = "El Telefono debe comenzar con 2, 6 o 7";

        Swal.fire({
          position: 'top-end',
          icon: 'warning',
          title: 'El Telefono debe comenzar con 2, 6 o 7',
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
    }

  }

 
  function du(id) {
    var num = document.getElementById(id).value.length;

    if (num == 8)
      document.getElementById(id).value = document.getElementById(id).value + '-';

  }

 
  function sinECN2(valor){
    
    if(valor.checked){
      for (i = 0; i < document.getElementsByName('lugarEC').length; i++) {
      document.getElementsByName("lugarEC")[i].disabled=true;
      document.getElementsByName("montoEC")[i].disabled=true;
      document.getElementsByName("fechaEC")[i].disabled=true;
      document.getElementsByName("estadoEC")[i].disabled=true;
      document.getElementsByName("cuotaEC")[i].disabled=true;
      }
      if(document.getElementById("comEvaluacion").value.length == 0 ){
        document.getElementById("comEvaluacion").value=document.getElementById("comEvaluacion").value+"No posee experiencia crediticia."
      }
      
    }else{
      for (i = 0; i < document.getElementsByName('lugarEC').length; i++) {
      document.getElementsByName("lugarEC")[i].disabled=false;
      document.getElementsByName("montoEC")[i].disabled=false;
      document.getElementsByName("fechaEC")[i].disabled=false;
      document.getElementsByName("estadoEC")[i].disabled=false;
      document.getElementsByName("cuotaEC")[i].disabled=false;
      }
      document.getElementById("comEvaluacion").value=""
    }
  }

  // cambiar datos segun alternativas seleccionadad
  function cambioAlternativas(){
    /*
    id=document.getElementById('detalleObra').value;
    plazo = id.split("|")
    alert(""+plazo[0])
    document.getElementById('plazoME').value=plazo[1];
    */
  }

  function obtenerRangoNatural(id) {
    if(id=="-0")
      id= document.getElementById("destinoNE").value
    $.ajax({
        url: "/NaturalApp/obtenerRango/?id=" +  id,
        type: "get",
        headers: { "X-CSRFToken": '{{ csrf_token }}' },
        dataType: "json",
        success: function (response) {
            if (response != "-0"){
              montoMinNat = response[0].fields.montominimo 
              montoMaxNat = response[0].fields.montomaximo
            }
                
          
            if (response == "-0")
                alert(document.getElementById('alter').value)
        },
        error: function (error) {
            alert("no paso")
        }
    });
}

function validarMontoNat(monto){
  if(monto.value < montoMinNat || monto.value > montoMaxNat){
    alertA("EL monto tiene que estar dentro del rango de la alternativa seleccionada")
    monto.value = ""
  }
}

  
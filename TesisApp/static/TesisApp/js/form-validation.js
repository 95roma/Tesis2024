
$(function() {
  /* Inicialice la validación del formulario en el formulario de registro.
 Tiene el atributo de nombre "contact"*/
$.validator.addMethod("alfanumOespacio", function(value, element) {
return /^(?!.*(.)\1{2})[ a-zA-Z0-9áéíóúüñ.]*$/i.test(value);
}, "Ingrese sólo letras o números sin repetir más de 2 veces .");

$.validator.addMethod("validartelefono", function(value, element) {
return  /^[7|6|2]\d{3}-\d{4}$/.test(value);
}, "Ingrese correctamente que comience con 7,6 ó 2");

$.validator.addMethod("validaemail", function(value, element) {
return/^(?:[^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*|"[^\n"]+")@(?:[^<>()[\].,;:\s@"]+\.)+[^<>()[\]\.,;:\s@"]{2,63}$/i.test(value);
}, "Ingrese un correo válido  en formaro que contenga @ y .com");

  $("form[name='contact']").validate({
// Especificar reglas de validación

   rules :{
                nombre : {
                    required : true, minlength : 3, alfanumOespacio:true,  maxlength : 25
                },
               apellido: {
                    required : true, minlength : 3, alfanumOespacio:true,  maxlength : 25
                },
                telefono: {  required: true, validartelefono: true, maxlength:9
                },
                fecha:{
                  required:true
                },
                correo:{
                  required:true, validaemail: true
                }
            },
            messages : {
                
                nombre : {
                    required : "Debe ingresar un nombre",
                    minlength : "EL nombre debe tener un minimo de 3 caracteres",
                    maxlength : "EL nombre debe tener un maximo de 25 caracteres"
                },
                 apellido : {
                    required : "Debe ingresar un apellido",
                    minlength : "EL apellido debe tener un minimo de 3 caracteres",
                    maxlength : "EL apellido debe tener un maximo de 25 caracteres"
                },
                telefono: {
                  required: "Debe ingresar el telefono",
                  maxlength: "Máximo de 9 caracteres"
                },
                fecha: {
                   required: 'Ingrese fecha'
                },
                correo:{
                  required: 'Ingrese correo'
                }
            },

    submitHandler: function(form) {
      form.submit();
    }
  });
});
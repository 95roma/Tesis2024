    
function alertA(texto) {
    Swal.fire({
         imageUrl: '../../../static/TesisApp/images/iconHabiW.png',
        imageWidth: '65px',
        title: 'Advertencia!!! ',
        icon: 'warning',        
        html: '<h3>'+texto+'</h3>',        
        width: '30%',
        confirmButtonText: 'confirmar',
       
       // imageHeight: '50px',        
        
        customClass: {    
            //title:'clini-title',
             image:'clini-logo',
             icon:'clini-icon',
             header: 'clini-header',
        },
    });
}

function alertP(texto) {
    Swal.fire({
         imageUrl: '../../../static/TesisApp/images/iconHabi.png',
        imageWidth: '65px',
        title: 'Esta seguro ',
        icon: 'question',
        
        html: '<h3>'+texto+'</h3>',     
        width: '30%',
        confirmButtonText: 'confirmar',
       
       // imageHeight: '50px',        
        
        customClass: {    
            //title:'clini-title',
             image:'clini-logo',
             icon:'clini-icon',
             header: 'clini-header',
        },
    });
}
function alertC(texto) {
    //alert("paso");
    Swal.fire({
         imageUrl: '../../../static/TesisApp/images/iconHabiS.png',
        imageWidth: '65px',
        title: 'Exito',
        icon: 'success',
        
        html: '<h3>'+texto+'</h3>',     
        width: '30%',
        confirmButtonText: 'confirmar',
       
       // imageHeight: '50px',        
        
        customClass: {    
            //title:'clini-title',
             image:'clini-logo',
             icon:'clini-icon',
             header: 'clini-header',
        },
    });
}
function alertE(texto) {
    Swal.fire({
         imageUrl: '../../../static/TesisApp/images/iconHabiE.png',
        imageWidth: '65px',
        title: 'Ops! ',
        icon: 'error',
        
        html: '<h3>'+texto+'</h3>',     
        width: '30%',
        confirmButtonText: 'confirmar',
       
       // imageHeight: '50px',        
        
        customClass: {    
            //title:'clini-title',
             image:'clini-logo',
             icon:'clini-icon',
             header: 'clini-header',
        },
    });
}

function confirmar(texto, formulario) {
    Swal.fire({
        imageUrl: '../../../static/TesisApp/images/iconHabi.png',
        imageWidth: '65px',
        title: 'Esta seguro ',
        icon: 'question',

        html: '<h3>'+texto+'</h3>',     
        width: '30%',  
      
      //showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: 'Guardar',
      denyButtonText: `No guardar`,
      cancelButtonText: 'Cancelar',

      customClass: {    
        //title:'clini-title',
         image:'clini-logo',
         icon:'clini-icon',
         header: 'clini-header',
    },
    }).then((result) => {
      /* Read more about isConfirmed, isDenied below */
      if (result.isConfirmed) {
        alertC('Solicitud registrada como incompleta');
        formulario.submit();
      } else if (result.isDenied) {
        return false;
       // Swal.fire('Changes are not saved', '', 'info')
      }
    })
}

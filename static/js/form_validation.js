function validation_form_prof() {

	var cedula = document.getElementByCedula('id_cedula_profesor').value;
	var nombre = document.getElementByNombre('id_nombre_profesor').value;
	var apellido = document.getElementByApellido('id_apellido_profesor').value;
	var asigna = document.getElementByAsignacion('id_asignacion').value;

	if (cedula == null || cedula.length < 8 || isNaN(cedula)){
		alert('ERROR: Debe Ingresar Una Cedula Correcta!');
		return false
	}

}

function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ";/
    especiales = [8, 37, 39, 46, 6];  
    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if(letras.indexOf(tecla) == -1 && !tecla_especial){
alert('Tecla no aceptada');
        return false;
      }
}

function SoloNumeros(evt){
 if(window.event){
  keynum = evt.keyCode; 
 }
 else{
  keynum = evt.which; 
 } 
 if((keynum > 47 && keynum < 58) || keynum == 8 || keynum == 13 || keynum == 6 ){
  return true;
 }
 else{
  return false;
 }
}

$(document).ready(function(){
    $('form').submit(function(event) { // o el id de tu formulario
        if($('#{{form.nombre.id_cedula_profesor}}').val() == '') {
            // aqui puedes hacer lo que quieras, como poner clases de error en tus inputs para especificar el error, lanzar un alert, como sea
            return false;
        }
    })

})
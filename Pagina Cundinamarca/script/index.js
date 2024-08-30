function validarNombre(event) {
    var nombre = document.getElementById("nombre").value
    var celular = document.getElementById("celular").value
    var correo = document.getElementById("correo").value
    var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var correoOk = regex.test(correo);
    if (!correoOk) {
        alert("correo negado, verifica tu correo")
    }

   
  

    var valorSi = document.getElementById("si")
    var valorNo = document.getElementById("no")

    var region = document.getElementById("region").value
    var tipoCc = document.getElementById("tipoCc")
    var tipoCll = document.getElementById("tipoCll")
    var tipoCw = document.getElementById("tipoCw")
    var tipoDeContacto = []

    if (tipoCc.checked == true) {
        tipoDeContacto.push(tipoCc.value)
    }
    if (tipoCll.checked == true){
        tipoDeContacto.push(tipoCll.value)
    }
    if (tipoCw.checked == true){
        tipoDeContacto.push(tipoCw.value)
    }

    localStorage.setItem('nombre',nombre)
    localStorage.setItem('numero',celular)
    localStorage.setItem('email',correo)
    localStorage.setItem('region',region)
    localStorage.setItem('masInfo',valorSi)
    localStorage.setItem('masInfo',valorNo)
    localStorage.setItem('tipoDeContactp',tipoDeContacto)

    location.href = "../pages/pageDatos.html"
   
}

function Datos() {

    nombre=localStorage.getItem('nombre')
    console.log(nombre)
    document.getElementById("nombreOk").value=nombre
}

document.addEventListener("DOMContentLoaded", function(){
    function masInfo() {
        valorSi = document.getElementById("si")
        valorNo = document.getElementById("no")
       
        var divTipoC = document.getElementById("tipoContacto")
        
        if (valorSi.checked) {
            divTipoC.hidden = false
        }
        if (valorNo.checked) {
            divTipoC.hidden = true
        }
    }
    document.getElementById("si").onclick = masInfo
    document.getElementById("no").onclick = masInfo

})


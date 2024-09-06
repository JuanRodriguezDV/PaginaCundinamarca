function validarNombre(event) {
    event.preventDefault();
    var nombre = document.getElementById("nombre").value
    var celular = document.getElementById("celular").value
    var correo = document.getElementById("correo").value
    var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var correoOk = regex.test(correo);
    var valorSi = document.getElementById("si")
    var valorNo = document.getElementById("no")
    var region = document.getElementById("region").value
    var tipoCc = document.getElementById("tipoCc")
    var tipoCll = document.getElementById("tipoCll")
    var tipoCw = document.getElementById("tipoCw")
    var tipoContacto = []
    if (!correoOk) {
        alert("correo negado, verifica tu correo")
        return;
    }

    if (tipoCc.checked) {
        tipoContacto.push(tipoCc.value)
    }
    if (tipoCll.checked){
        tipoContacto.push(tipoCll.value)
    }
    if (tipoCw.checked){
        tipoContacto.push(tipoCw.value)
    }

    localStorage.setItem('nombre',nombre)
    localStorage.setItem('celular',celular)
    localStorage.setItem('correo',correo)
    localStorage.setItem('region',region)
    localStorage.setItem('masInfo',valorSi.checked ? 'si': valorNo.checked ? 'no' : 'N/A')
    localStorage.setItem('tipoContacto',JSON.stringify(tipoContacto))

    location.href = "/Pagina Cundinamarca/pages/pageDatos.html"
   
}

function Datos() {
    nombre      = localStorage.getItem('nombre')
    celular     = localStorage.getItem('celular')
    email       = localStorage.getItem('correo')
    region      = localStorage.getItem('region')
    masInfo     = localStorage.getItem('masInfo')
    tipoContacto= JSON.parse(localStorage.getItem('tipoContacto'))
    
    document.getElementById("nombreOk").value= nombre
    document.getElementById("celularOk").value=celular
    document.getElementById("correoOk").value=email
    document.getElementById("regionOk").value=region
    if(masInfo == "si"){
        document.getElementById("masInfoOk").value="Si";
    }else if (masInfo == "no"){
        document.getElementById("masInfoOk").value="No";
    }

    document.getElementById("tipoCOk").value = (Array.isArray(tipoContacto) && tipoContacto.length > 0)
    ? tipoContacto.join(", ")
    : 'N/A';
}

document.addEventListener("DOMContentLoaded", function(){
    valorSi = document.getElementById("si")
    valorNo = document.getElementById("no")
    if(valorSi && valorNo){
        function masInfo() {
            var divTipoC = document.getElementById("tipoContacto")
            
            if (valorSi.checked) {
                divTipoC.hidden = false
                
            }
            if (valorNo.checked) {
                divTipoC.hidden = true
            }
    }}
    valorSi.addEventListener("change", masInfo);
    valorNo.addEventListener("change", masInfo);
    masInfo()

})


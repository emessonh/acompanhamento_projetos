// console.log('entrou no js');
$(document).ready(function() {
    // console.log('entrou aqui');
    $('#cpf').mask('000.000.000-00');
});

let checkbox = document.querySelector('#mostrar-senha');
checkbox.addEventListener('click', function() {
    let input = document.querySelector('#password');
    if(input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
    } else {
        input.setAttribute('type', 'password');
    }
});


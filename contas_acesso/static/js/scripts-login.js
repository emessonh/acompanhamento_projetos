$(document).ready(function() {
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

let checkbox_confirm_senha = document.querySelector('#mostrar-confirmacao-senha');
// console.log('chegou na confirmacao de senha');
checkbox_confirm_senha.addEventListener('click', function() {
    let input = document.querySelector('#confirm-password');
    if(input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
    } else {
        input.setAttribute('type', 'password');
    }
});


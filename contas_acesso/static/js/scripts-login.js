// Máscara do cpf, no login, criacao de conta e alterar senha
$(document).ready(function() {
    $('#cpf').mask('000.000.000-00');
});

// mostra a senha 
let checkbox = document.querySelector('#mostrar-senha');
checkbox.addEventListener('click', function() {
    let input = document.querySelector('#password');
    if(input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
    } else {
        input.setAttribute('type', 'password');
    }
});
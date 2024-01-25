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

// // mostra a senha de confirmação
// let checkbox_confirm_senha = document.querySelector('#mostrar-confirmacao-senha');
// checkbox_confirm_senha.addEventListener('click', function() {
//     let input = document.querySelector('#confirm-password');
//     if(input.getAttribute('type') == 'password') {
//         input.setAttribute('type', 'text');
//     } else {
//         input.setAttribute('type', 'password');
//     }
// });

// // mostra o nome da pessoa
// let cpf = document.querySelector('#cpf');
// cpf.addEventListener('change', function(){
//     if (cpf.value.length == 14){
//         let input = document.querySelector('#nome')
//         // input.value = 'Emesson';
//         // console.log('apresenta nome');
//     }
// });






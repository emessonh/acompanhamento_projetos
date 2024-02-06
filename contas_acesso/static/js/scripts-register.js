$(document).ready(function() {
    $('#cpf').mask('000.000.000-00');
});

// Mostra senha
let checkbox = document.querySelector('#mostrar-senha');
checkbox.addEventListener('click', function() {
    let input = document.querySelector('#password');
    if(input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
    } else {
        input.setAttribute('type', 'password');
    }
});

// Mostra confirmação de senha
let checkbox_confirm_senha = document.querySelector('#mostrar-confirmacao-senha');
checkbox_confirm_senha.addEventListener('click', function() {
    let input = document.querySelector('#confirm-password');
    if(input.getAttribute('type') == 'password') {
        input.setAttribute('type', 'text');
    } else {
        input.setAttribute('type', 'password');
    }
});

// mostra o nome da pessoa
$(document).ready(function() {
    $('#cpf').on('focus', function() {
        // console.log('alterou o campo de cpf');
        $('#cpf').on('blur', function(){
            var cpf = $(this).val();
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            $.ajax({
                url: "mostra-nome",
                data: {
                    'cpf': cpf,
                    "csrfmiddlewaretoken": csrftoken
                },
                method: 'POST',
                dataType: 'json',
                success: function(data) {
                    $('#nome').val(data.nome);
                },
                error: function(xhr, status, error) {
                    $('#nome').val('');
                }
            });
        });
        
    });
});
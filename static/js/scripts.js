// $(document).ready(function(){
//     var deleteBtn = $('.delete-btn');
//     $(deleteBtn).on('click', function(e){
//         e.preventDefault();
//         var delLink = $(this).attr('href');
//         var result = confirm('Confirma a deleção?');
//         if (result){
//             window.location.href = delLink;
//         }
//     });
// });

$(document).ready(function() {
    $('#cpf').mask('000.000.000-00');
});

// Faz o modal de delete funcionar

var link = null;
$('.delete-btn').on('click', function(){
    link = $(this).attr('href');
});

$('#confirma-exclusao').on('click', function () {
    window.location.href = link;
})

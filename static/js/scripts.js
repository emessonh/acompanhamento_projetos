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
    // console.log('entrou aqui');
    $('#cpf').mask('000.000.000-00');
});

// 

var link = null;
$('.delete-btn').on('click', function(){
    link = $(this).attr('href');
});

$('#confirma-exclusao').on('click', function () {
    // var Link = $('.delete-btn').attr('href');
    window.location.href = link;
})

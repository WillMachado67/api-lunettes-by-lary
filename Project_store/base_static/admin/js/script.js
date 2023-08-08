$(document).ready(function() {
    //ao finalizar o carregamento, adiciona as duas funcoes.

    //cria uma funcao chamada quando acontece alteracao no campo
    $('#id_status').change(function(){
        feactured = $('#id_featured_products');
        if ($(this).prop('checked') != true){
            feactured.prop('checked', false);
            feactured.prop('disabled', true);
        } else {
            feactured.prop('disabled', false);
        }
    });
});

$(document).ready(function() {
    $('#id_category').change(function() {
        const selectedText = $(this).find('option:selected').text();
        
        console.log('Opção selecionada:', selectedText);
    });
});


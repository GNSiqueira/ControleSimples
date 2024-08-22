document.getElementById('produto').addEventListener('input', function() {
    var datalist = document.getElementById('produtos');
    var ovalue = document.getElementById('ovalue');
    var input = this.value;

    if (datalist && ovalue) {
        var options = datalist.children;
        var found = false; // Flag para verificar se encontramos a opção

        for (var i = 0; i < options.length; i++) {
            if (options[i].value === input) {
                ovalue.value = options[i].getAttribute('data-ovalue');
                found = true;
                break;
            }
        }

        // Se não encontrou a opção, você pode definir um valor padrão ou limpar o campo
        if (!found) {
            ovalue.value = ''; // Limpa o campo ou defina um valor padrão
        }
    }
});

function finalizar() {
    var form = document.getElementById('form-principal');
    var produto = document.getElementById('produto');
    var qtd = document.getElementById('qtd');

    qtd.removeAttribute('required');
    produto.removeAttribute('required');
    form.action = "/produto/saida/end";
    form.method = "post";
    form.submit();
    qtd.setAttribute('required', 'required');
    produto.setAttribute('required', 'required');
}

document.addEventListener('DOMContentLoaded', function() {
    var cor = document.querySelector('#msg');

    if (cor.textContent != 'sucesso') {
        cor.style.color = 'red';
        setTimeout(function() {
            cor.style.color = 'white';
        }, 7000);
    }
    
})

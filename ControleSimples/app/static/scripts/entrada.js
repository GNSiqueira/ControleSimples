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
    var valor = document.getElementById('valor');

    qtd.removeAttribute('required');
    produto.removeAttribute('required');
    valor.removeAttribute('required');
    form.action = "/produto/entrada/end";
    form.method = "post";
    form.submit();
    valor.setAttribute('required', 'required');
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

function formatarMoeda(valor) {
    valor = valor.replace(/\D/g, "");
    valor = (valor / 100).toFixed(2) + ""; 
    valor = valor.replace(".", ",");
    valor = valor.replace(/(\d)(?=(\d{3})+\,)/g, "$1."); // Adiciona os pontos separadores de milhar
    return valor;
}

document.getElementById('valor').addEventListener('input', function() {
    this.value = formatarMoeda(this.value);
});
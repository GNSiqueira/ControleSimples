document.addEventListener('DOMContentLoaded', function cor() {
    var cor = document.querySelector('#msg');

    switch (cor.textContent) {
        case 'sucesso':
            cor.style.color = 'white';
            break;
        case 'Produto cadastrado com sucesso!':
            cor.style.color = 'green';
            break;
        default:
            cor.style.color = 'red';
            break;
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
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
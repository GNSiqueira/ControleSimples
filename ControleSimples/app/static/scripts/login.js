document.addEventListener('DOMContentLoaded', function() {
    var cor = document.querySelector('#msg');

    switch (cor.textContent) {
        case 'Senha ou login invalido':
            cor.style.color = 'red';
            break;
        default:
            break;
    }
    
})
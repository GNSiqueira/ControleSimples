document.getElementById('produto').addEventListener('input', function() {
    var datalist = document.getElementById('produtos');
    var input = this.value;
    var options = datalist.children;
    for (var i = 0; i < options.length; i++) {
        if (options[i].value === input) {
            document.getElementById('ovalue').value = options[i].getAttribute('data-ovalue');
            break;
        }
    }
});
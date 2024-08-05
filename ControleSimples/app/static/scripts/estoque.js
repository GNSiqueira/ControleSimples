function buscarProdutos() {
    // Obtém o termo de busca inserido pelo usuário no campo de input com id 'search-bar'
    const termoBusca = document.getElementById('search-bar').value;

    // Envia uma solicitação HTTP GET ao servidor Flask, passando o termo de busca como parâmetro de consulta
    fetch(`/buscar_produtos?termo=${termoBusca}`)
        .then(response => response.json()) // Quando a resposta for recebida, converte-a para JSON
        .then(data => {
            // Seleciona o corpo da tabela onde os produtos serão exibidos
            const tabela = document.getElementById('tabela-produtos');
            tabela.innerHTML = ''; // Limpa o conteúdo atual da tabela

            // Para cada produto recebido na resposta (que é um array de objetos de produto)
            data.forEach(produto => {
                // Cria um novo elemento de linha de tabela (tr)
                const linha = document.createElement('tr');

                // Define o conteúdo HTML da linha, preenchendo com os dados do produto
                linha.innerHTML = `
                    <td>${produto.nome}</td>
                    <td>${produto.qtd}</td>
                    <td>${produto.valor}</td>
                    <td>
                        <a href="/produto/remover/${produto.id}">Remover</a>
                        <a href="/produto/alterar/${produto.id}">Alterar</a>
                    </td>
                `;

                // Adiciona a nova linha à tabela
                tabela.appendChild(linha);
            });
        });
}

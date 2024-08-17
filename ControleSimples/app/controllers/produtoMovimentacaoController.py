from app.daos import produtoMovimentacaoDao

def create_produto_movimentacao(movimentacao, produtos, qtd, valor):
    return produtoMovimentacaoDao.create_produto_movimentacao(movimentacao, produtos, qtd, valor)
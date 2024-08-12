from app.daos import produtoDao
from app.models.produtoModel import Produto

def carregar_produtos():
    retorno = produtoDao.read_produtos()
    
    if retorno == 2:
        return 2
    elif retorno == 1:
        return 1
    else:
        return retorno
    
def cadastrar_produto(descricao, valor, categoria):
    descricao = descricao.strip()
    pesquisa_produto = produtoDao.validar_produto(descricao, 1)

    if pesquisa_produto == 0: # deu certo(não existe produto assim)
        criacao = produtoDao.create_produto(descricao, valor, categoria)
        if criacao == 0:

            return 0
        else:
            return "Erro ao cadastrar o produto"
    elif pesquisa_produto == 1: # deu erro
        return "Erro ao verificar produtos existentes!"
    
    elif pesquisa_produto == 2: # já existe o produto
        return "Produto já existente!"
    
def search_produto_desc(descricao):
    result = produtoDao.search_produto_desc(descricao)
    if result == 1:
        return 1
    else:
        return result
    
def search_produto_id(id):
    result = produtoDao.search_produto_id(id)
    if result == 1:
        return 1
    else:
        return result
    
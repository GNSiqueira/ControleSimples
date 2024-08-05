from app.daos import categoriaDao
from app.models.categoriaModel import Categoria

def carregar_categorias():
    results = categoriaDao.carregar_categorias()
    if results == 1:
        return 1
    elif results == 2:
        return 2
    else:
        retorno = []
        for result in results:
            p = Categoria(result[0], result[1])
            retorno.append(p)
        return retorno
    
def cadastrar_categoria(categoria):
    categoria = categoria.strip()
    validar = categoriaDao.validar_categoria(categoria)
    if validar == 0:
        cadastro = categoriaDao.create_categoria(categoria)
        return cadastro
    return 2

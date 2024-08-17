from app.daos import inventarioDao

def carregar_inventario():
    return inventarioDao.listar_inventario()

def cadastrar_inventario(quantidade, idproduto):
    return inventarioDao.create_inventario(quantidade, idproduto)
    

def update_qtd_inventario(quantidade, id):
    return inventarioDao.update_qtd_inventario(quantidade, id)
    
def search_inventario_idproduto(id):
    return inventarioDao.search_inventario_idproduto(id)
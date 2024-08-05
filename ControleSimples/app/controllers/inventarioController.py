from app.daos.inventarioDao import *

def carregar_inventario():
    return listar_inventario()

def cadastrar_inventario(quantidade, idproduto):
    result = create_inventario(quantidade, idproduto)
    return result
from app.models.movimentacaoModel import Movimentacao
from app.daos import movimentacaoDao

def create_movimentacao(data, hora, tipo, idfuncionario):
    return movimentacaoDao.create_movimentacao(data, hora, tipo, idfuncionario)
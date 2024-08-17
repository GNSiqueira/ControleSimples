from app.config.conexao import Conexao
from psycopg2 import Error

def create_produto_movimentacao(movimentacao, produto, qtd, valor):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = ("INSERT INTO MovimentoProduto (idMovimentacao, idProduto, qtdProduto, valorProduto)VALUES ({}, {}, {}, {});".format(movimentacao, produto, qtd, valor))
        cursor.execute(query)
        conn.commit()
        return 0
    except (Exception, Error) as error:
        conn.rollback()
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)
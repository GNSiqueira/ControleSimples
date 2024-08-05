from app.config.conexao import Conexao
from psycopg2 import Error

def listar_inventario():
    try:
        conexao = Conexao()
        conn = conexao.conectar()
        try:
            cursor = conn.cursor()
            query = (f"SELECT * FROM inventario")
            cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
            return result
        except (Exception, Error) as e:
            conn.rollback()
            return 1

        finally:
            cursor.close()
            conexao.desconectar(conn)
    except (Exception, Error) as e: 
        return 1
    
def create_inventario(quantidade, idproduto):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = ("insert into inventario (qtdproduto, idproduto) values ({}, {});".format(quantidade, idproduto))    
        cursor.execute(query)
        conn.commit()
        return 0

    except (Exception, Error) as e:
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)
from app.config.conexao import Conexao
from psycopg2 import Error

def read_movimentacao():
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = (f"SELECT * FROM movimentacao")
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

def read_movimentacao(data, hora):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = (f"SELECT * FROM movimentacao where datamovimentacao = '{data}' and horamovimentacao = '{hora}'")
        cursor.execute(query)
        result = cursor.fetchone()
        conn.commit()
        return result
    except (Exception, Error) as e:
        conn.rollback()
        return 1

    finally:
        cursor.close()
        conexao.desconectar(conn)


def create_movimentacao(data, hora, tipo, idfuncionario):
    conexao = Conexao()
    conn = conexao.conectar()
    try: 
        cursor = conn.cursor()
        query = ("insert into movimentacao (datamovimentacao, horamovimentacao, tipomovimentacao, idfuncionario) values ('{}', '{}', {}, {});".format(data, hora, tipo, idfuncionario))
        cursor.execute(query)

        conn.commit()
        return read_movimentacao(data, hora)
    except(Exception, Error) as error:
        conn.rollback()
        print(error)
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)

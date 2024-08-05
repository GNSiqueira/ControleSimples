from psycopg2 import Error
from app.config.conexao import Conexao

def carregar_categorias():
    try:
        conexao = Conexao()
        conn = conexao.conectar()
        try:
            cursor = conn.cursor()
            query = (f"SELECT * FROM categoria order by categoria")
            cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
            if result == []:
                return 2
            else:
                return result
        except (Exception, Error) as e:
            conn.rollback()
            return 1

        finally:
            cursor.close()
            conexao.desconectar(conn)
    except (Exception, Error) as e:
        return 1
    
def validar_categoria(categoria):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = "select count(*) from categoria where categoria = '{}'".format(categoria)
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchone()
        return result[0]
    
    except(Exception, Error) as error:
        conn.rollback()
        return 1
    
    finally:
        cursor.close()
        conexao.desconectar(conn)

def create_categoria(categoria):
    conexao = Conexao()
    conn = conexao.conectar()
    try: 
        cursor = conn.cursor()
        query = "insert into categoria (categoria) values ('{}')".format(categoria)
        cursor.execute(query)
        conn.commit()
        return 0 
    except(Exception, Error) as error:
        conn.rollback()
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)
        
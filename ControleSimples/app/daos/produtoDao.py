from app.config.conexao import Conexao
from psycopg2 import Error

def read_produtos():
    try:
        conexao = Conexao()
        conn = conexao.conectar()
        try:
            cursor = conn.cursor()
            query = (f"SELECT * FROM produto order by descproduto")
            cursor.execute(query)
            result = cursor.fetchall()
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
    
def create_produto(descricao, valor, categoria):
    conexao = Conexao()
    conn = conexao.conectar()

    try:
        cursor = conn.cursor()
        query = "insert into produto (descproduto, valorproduto, idcategoria) values ('{}', {}, {});".format(descricao, valor, categoria)
        cursor.execute(query)
        conn.commit()
        return 0
    
    except (Exception, Error) as e:
        conn.rollback()
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)

def validar_produto(info, tipo):
    conexao = Conexao()
    conn = conexao.conectar()

    try:
        cursor = conn.cursor()
        
        # por descrição
        if tipo == 1:
            query = "select count(*) from produto where descproduto = '{}'".format(info)
            cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
            if result[0][0] == 0:
                return 0
            elif result[0][0] >= 1:
                return 2

        # por id
        if tipo == 2:
            query = "select * from produto where idproduto = {}".format(info)
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

def search_produto_desc(descricao):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = "select * from produto where descproduto = '{}'".format(descricao)
        cursor.execute(query)
        result = cursor.fetchone()
        conn.commit()
        if result == None:
            return 2
        return result

    except (Exception, Error) as e:
        conn.rollback()
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)

def search_produto_id(id):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = "select * from produto where idproduto = %s"
        cursor.execute(query, (id, ))
        conn.commit()
        return cursor.fetchone()
    except(Exception, Error) as error:
        conn.rollback()
        print(error)
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)


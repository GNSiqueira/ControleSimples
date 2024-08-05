from app.config.conexao import Conexao
from psycopg2 import Error

def login_funcionario(login, senha):
    try:
        conexao = Conexao()
        conn = conexao.conectar()
        try:
            cursor = conn.cursor()
            query = (f"SELECT count(idfuncionario) FROM funcionario WHERE loginfuncionario = '{login}' AND senhafuncionario = '{senha}'")
            cursor.execute(query)
            result = cursor.fetchone()

            if result[0] == 1:
                return 0
            else:
                return 1
        except (Exception, Error) as e:
            conn.rollback()
            return 1

        finally:
            cursor.close()
            conexao.desconectar(conn)
    except (Exception, Error) as e:
        return 1
    
def search_funcionario_login_password(login, senha):
    conexao = Conexao()
    conn = conexao.conectar()
    try:
        cursor = conn.cursor()
        query = "select * from funcionario where loginfuncionario = '{}' and senhafuncionario = '{}'".format(login, senha)
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    except(Exception, Error) as error:
        conn.rollback()
        return 1
    finally:
        cursor.close()
        conexao.desconectar(conn)
        

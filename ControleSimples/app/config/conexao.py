from psycopg2 import connect, Error

class Conexao:
    def conectar(self):
        try:
            conn = connect(
                dbname="ControleSimples",
                user="postgres",
                password="123456",
                host="localhost"
            )

            return conn
        
        except (Exception, Error) as e:
            return 1
        
    def desconectar(self, conn):
        try:
            if conn is not None:
                conn.close()
        except (Exception, Error):
            return 1
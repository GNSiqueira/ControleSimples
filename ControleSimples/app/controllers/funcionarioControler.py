from app.daos import funcionarioDao
from app.models.funcionarioModel import Funcionario

def logar_funcionario(login, senha):
    return funcionarioDao.login_funcionario(login, senha)

def search_funcionario_login_senha(login, senha):
    result = funcionarioDao.search_funcionario_login_password(login, senha)
    if result == 1:
        return 1
    else:
        funcionario = Funcionario(result[0], result[1], result[2], result[3], result[4])
        return funcionario

search_funcionario_login_senha('admin', 'admin')
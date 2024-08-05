from app import app
from flask import render_template, request, redirect, jsonify, session, url_for
from app.controllers import funcionarioControler, produtoController, inventarioController, categoriaController
import secrets
app.secret_key = secrets.token_hex(32)

def verificar_login():
    if 'funcionario' in session:
        return 0
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('funcionario', None)
    return redirect(url_for('login'))

@app.route("/", methods=["GET", "POST"])
def login():
    if 'funcionario' in session:
        return redirect(url_for('dashboard'))
    else:
        if request.method == "POST":
            login = request.form.get("login")
            senha = request.form.get("password")
            result = funcionarioControler.logar_funcionario(login, senha)
            if result == 0:
                funcionario = funcionarioControler.search_funcionario_login_senha(login, senha)
                session['funcionario'] = funcionario.idfuncionario
                return redirect(url_for('dashboard'))
            return render_template("login.html", msg = "Senha ou login invalido")    
        return render_template("login.html", msg = 'Teste')
    


@app.route("/dashboard")
def dashboard():
    if verificar_login() == 0:
        return render_template("dashboard.html")
    else: 
        return verificar_login()

@app.route("/estoque")
def estoque():
    if verificar_login() == 0:
        produtos_retorno = produtoController.carregar_produtos()
        inventario_retorno = inventarioController.carregar_inventario()

        if produtos_retorno == 2:
            produtos = []
            msg = "Nenhum produto encontrado"
        elif produtos_retorno == 1:
            produtos = []
            msg = "Erro ao carregar os produtos"
        else:
            produtos = []
            for produto in produtos_retorno:
                inventario_qtd = 0
                for inventario in inventario_retorno:
                    if inventario[2] == produto[0]:
                        inventario_qtd = inventario[1]
                monstro = {'id': produto[0], 'nome': produto[1], 'qtd': inventario_qtd, 'valor': produto[2]}
                produtos.append(monstro)
            msg = ""
        return render_template("estoque.html", produtos=produtos, msg=msg)
    else:
        return verificar_login()

@app.route('/buscar_produtos', methods=['GET'])
def buscar_produtos():
    if verificar_login() == 0:
        produtos_retorno = produtoController.carregar_produtos()
        inventario_retorno = inventarioController.carregar_inventario()
        produtos = []
        for produto in produtos_retorno:
            inventario_qtd = 0
            for inventario in inventario_retorno:
                if inventario[2] == produto[0]:
                    inventario_qtd = inventario[1]
            monstro = {'id': produto[0], 'nome': produto[1], 'qtd': inventario_qtd, 'valor': produto[2]}
            produtos.append(monstro)

        termo_busca = request.args.get('termo', '')
        resultados = [p for p in produtos if termo_busca.lower() in p['nome'].lower()]
        
        return jsonify(resultados)
    else: 
        return verificar_login()

@app.route("/cadastrar/produto", methods=["GET", "POST"])
def cadastrar_produto():
    if verificar_login() == 0:
        categorias = categoriaController.carregar_categorias()
        if categorias == 1:
            msg = "Erro ao carregar as categorias"
            categorias = []
        elif categorias == 2:
            msg = "Nenhuma categoria encontrada"
            categorias = []
        else:
            msg = "sucesso"

        if request.method == "POST":
            categoria = request.form.get('categoria')
            descricao = request.form.get('descricao')
            qtd = int(request.form.get('qtd'))
            valor = request.form.get('valor')
            valor = float(valor.replace(",","."))

            retorno = produtoController.cadastrar_produto(descricao, valor, categoria)
            if retorno == 0:
                idproduto = produtoController.search_produto_desc(descricao)
                result_inventario = inventarioController.cadastrar_inventario(qtd, idproduto[0])
                if result_inventario == 0:
                    msg = "Produto cadastrado com sucesso!"
                else:
                    msg = 'Erro ao cadastrar o inventário'
            else:
                msg = retorno            

        return render_template("cadastro_produto.html", categorias=categorias, msg=msg)
    else:
        return verificar_login()

@app.route('/cadastrar/categoria', methods=['GET', 'POST'])
def cadastrar_categoria():
    if verificar_login() == 0:
        msg = "sucesso"
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            cadastro = categoriaController.cadastrar_categoria(categoria)
            if cadastro == 0:
                msg = "Categoria cadastrado com sucesso!"
            elif cadastro == 2:
                msg = "Categoria já existente!"
            else:
                msg = "Erro ao cadastrar categoria!"
            pass
        return render_template('cadastro-categoria.html', msg = msg)
    else:
        return verificar_login()

@app.route('/produto/entrada', methods=['GET', 'POST'])
def entrada():
    if verificar_login() == 0:
        msg = 'sucesso'
        produtos = []
        produtos_retorno = produtoController.carregar_produtos()
        if produtos_retorno == 2:
            msg = 'Nenhum produto encontrado!'
        elif produtos_retorno == 1:
            msg = 'Erro ao carregar produto!'
        else:
            for produto in produtos_retorno:
                p = {'id': produto[0], 'produto':produto[1]}
                produtos.append(p)
        
        if request.method == 'POST':
            produto = request.form.get('ovalue')
            print(produto)

        return render_template('entrada.html', produtos = produtos, msg = msg)
    else:
        return verificar_login()
    
@app.route('/produto/entrada/remover/<int:id>', methods=['GET'])
def remover_produto_carrinho(id):
    print(id)
    return redirect(url_for('entrada'))

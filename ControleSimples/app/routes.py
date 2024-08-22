from app import app
from flask import render_template, request, redirect, jsonify, session, url_for
from app.controllers import funcionarioControler, produtoController, inventarioController, categoriaController, movimentacaoController, produtoMovimentacaoController
import json
import secrets
import datetime 
app.secret_key = secrets.token_hex(32)

def data_atual():
    data = datetime.datetime.now()
    data_formatada = data.strftime('%d/%m/%Y')
    return data_formatada

def hora_atual():
    data = datetime.datetime.now()
    data_formatada = data.strftime('%H:%M:%S')
    return data_formatada

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
    session['funcionario'] = 1
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
            return render_template("login.html", msg="Senha ou login invalido")
        return render_template("login.html", msg='Teste')

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
            valor = float(request.form.get('valor').replace('.', '').replace(',', '.'))

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
        return render_template('cadastro-categoria.html', msg=msg)
    else:
        return verificar_login()

@app.route('/produto/entrada', methods=['GET', 'POST'])
def entrada():
    if verificar_login() == 0:
        msg = 'sucesso'
        produtos = []
        carrinhos = []

        produtos_retorno = produtoController.carregar_produtos()
        if produtos_retorno == 2:
            msg = 'Nenhum produto encontrado!'
        elif produtos_retorno == 1:
            msg = 'Erro ao carregar produto!'
        else:
            for produto in produtos_retorno:
                p = {'id': produto[0], 'produto': produto[1]}
                produtos.append(p)

        # Ação para adicionar produtos ao carrinho e finalizar compra
        if request.method == 'POST':
            idproduto = request.form.get('ovalue')
            carrinhos_str = request.form.get('carrinhos')
            quantidade = float(request.form.get('qtd'))
            valor = float(request.form.get('valor').replace('.', '').replace(',', '.'))
            pesquisa = produtoController.search_produto_id(idproduto)
            if carrinhos_str:
                carrinhos_str = carrinhos_str.replace("'", '"')

            # Decodifica a string carrinhos_str em uma lista de dicionários
            try:
                novos_carrinhos = json.loads(carrinhos_str) if carrinhos_str else []
            except json.JSONDecodeError as e:
                novos_carrinhos = []

            # Adiciona cada item novo ao carrinho
            for p in novos_carrinhos:
                carrinhos.append(p)
            # Adiciona o novo item atual ao carrinho
            info = {
                "id": int(idproduto),
                "produto": pesquisa[1],
                "quantidade": int(quantidade),
                "valor": '{:.2f}'.format(valor),
                "real": '{:.2f}'.format(round(valor * quantidade, 3))
            }
            carrinhos.append(info)

        return render_template(template_name_or_list='entrada.html', produtos=produtos, msg=msg, carrinhos=carrinhos)
    else:
        return verificar_login()

@app.route('/produto/entrada/remove', methods=['POST'])
def remover_do_carrinho():
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
                p = {'id': produto[0], 'produto': produto[1]}
                produtos.append(p)

        carrinhos_str = request.form.get('carrinhos')
        idproduto = request.form.get('remover')

        if carrinhos_str:
            carrinhos_str = carrinhos_str.replace("'", '"')

        # Decodifica a string carrinhos_str em uma lista de dicionários
        try:
            novos_carrinhos = json.loads(carrinhos_str) if carrinhos_str else []
        except json.JSONDecodeError as e:
            novos_carrinhos = []

        carrinhos = []
        # Adiciona cada item novo ao carrinho
        for p in novos_carrinhos:
            if p['id'] != int(idproduto):
                carrinhos.append(p)

        return render_template(template_name_or_list='entrada.html', produtos=produtos, msg=msg, carrinhos=carrinhos)
    else:
        return verificar_login()

@app.route('/produto/entrada/end', methods=['POST', 'GET'])
def finalizacao_de_carrinho():
    if verificar_login() == 0:
        carrinho = []
        carrinho_str = request.form.get('carrinhos')
        msg = 'Entrada finalizada com sucesso!'
        produtos = []
        produtos_retorno = produtoController.carregar_produtos()
        if produtos_retorno == 2:
            msg = 'Nenhum produto encontrado!'
        elif produtos_retorno == 1:
            msg = 'Erro ao carregar produto!'
        else:
            for produto in produtos_retorno:
                p = {'id': produto[0], 'produto': produto[1]}
                produtos.append(p)
        
        if carrinho_str:
            carrinho_str = carrinho_str.replace("'", '"')

        if carrinho_str != '[]':
            try: 
                carrinho = json.loads(carrinho_str) if carrinho_str else []
            except json.JSONDecodeError as e:
                carrinho = []
            
            #criar a movimentação com as informaçãoes de quem fez, a data hora e etc.
            info_movimentacao = {
                'idfuncionario': session['funcionario'],
                'data': data_atual(),
                'hora': hora_atual(),
                'tipo': 1
            }

            movimentacao = movimentacaoController.create_movimentacao(info_movimentacao['data'], info_movimentacao['hora'], info_movimentacao['tipo'], info_movimentacao['idfuncionario'])

            #registrar todos os itens do carrinho na movimentação
            #adicionar os itens ao inventário
            for item in carrinho:
                produtoMovimentacaoController.create_produto_movimentacao(movimentacao[0], item['id'], item['quantidade'], item['valor'])
                reajuste_qtd = inventarioController.search_inventario_idproduto(item['id'])[1] + item['quantidade']
                inventarioController.update_qtd_inventario(reajuste_qtd, item['id'])

            #remover todos os itens do carrinho
            carrinhos = []
        else: 
            msg = 'Carrinho vazio'
            carrinhos = []
        return render_template(template_name_or_list='entrada.html', produtos=produtos, msg=msg, carrinhos=carrinhos)
    else:
        return verificar_login()
    
@app.route('/produto/saida', methods=['POST', 'GET'])
def saida():
    if verificar_login() == 0:
        produtos = []
        produtos_retorno = produtoController.carregar_produtos()
        if produtos_retorno == 2:
            msg = 'Nenhum produto encontrado!'
        elif produtos_retorno == 1:
            msg = 'Erro ao carregar produto!'
        else:
            for produto in produtos_retorno:
                p = {'id': produto[0], 'produto': produto[1]}
                produtos.append(p)
        carrinho = []
        msg = 'sucesso'
        if request.method == 'POST':
            quantidade = int(request.form.get('qtd'))
            idproduto = request.form.get('ovalue')

            inventario = inventarioController.search_inventario_idproduto(idproduto)
            if inventario[1] < quantidade:
                return render_template('saida.html', produtos = produtos, carrinhos = carrinho, msg = "Quantidade insuficiente!")

            carrinho_str = request.form.get('carrinhos')

            if carrinho_str:
                carrinho_str = carrinho_str.replace("'", '"')
            
            try:
                carrinho = json.loads(carrinho_str) if carrinho_str else []
            except json.JSONDecodeError as e:
                carrinho = [] 

            for c in range(len(carrinho)):
                if int(carrinho[c]["id"]) == int(idproduto):
                    result = carrinho[c]["quantidade"] + quantidade
                    if inventario[1] < result:
                        return render_template('saida.html', produtos = produtos, carrinhos = carrinho, msg = "Quantidade insuficiente!")
                    carrinho[c]["quantidade"] += quantidade
                    return render_template('saida.html', produtos = produtos, carrinhos = carrinho, msg = 'sucesso')


            busca_produto = produtoController.search_produto_id(idproduto)
            
            info = {
                "id": int(idproduto),
                "produto": busca_produto[1],
                "quantidade": int(quantidade),
                "valor": '{:.2f}'.format(busca_produto[2]),
                "real": '{:.2f}'.format(round(busca_produto[2] * quantidade, 3))
            }


            carrinho.append(info)

        return render_template('saida.html', produtos = produtos, carrinhos = carrinho, msg = msg)
    else:
        return verificar_login()
    
@app.route("/produto/saida/remove", methods=['POST'])
def saida_remover():
    if verificar_login() == 0:
        produtos = []
        produtos_retorno = produtoController.carregar_produtos()
        if produtos_retorno == 2:
            msg = 'Nenhum produto encontrado!'
        elif produtos_retorno == 1:
            msg = 'Erro ao carregar produto!'
        else:
            for produto in produtos_retorno:
                p = {'id': produto[0], 'produto': produto[1]}
                produtos.append(p)
        idproduto = request.form.get('remover')
        carrinho = request.form.get('carrinho')
        
        if carrinho:
            carrinho = carrinho.replace("'", '"')
        try:
            carrinho = json.loads(carrinho) if carrinho else []
        except json.JSONDecodeError:
            carrinho = []
        carrinho_para_remover = carrinho
        carrinho = []
        for item in carrinho_para_remover:
            if int(item['id']) != int(idproduto):
                carrinho.append(item)

        return render_template('saida.html', carrinhos = carrinho, msg = 'sucesso', produtos = produtos)

    else:
        return verificar_login()
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
# 4) Crie uma API para gerenciar produtos de um e-commerce, permitindo adicionar, listar,
#atualizar estoque, deletar produtos e gerenciar um carrinho de compras.

FILENAME = 'produtos.json'
FILENAME2 = 'carrinho.json'
##
# nome
#quantidade

#carrinho -> 
# id 
# quantidade
# 
# 
 
#Função para carregar as produtos
def carregar_produtos():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
    #Função para carregar o carrinho
def carregar_carrinho():
    try:
        with open(FILENAME2, 'r') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
#Função para salvar as produtos
def salvar_produtos(produtos):
    with open(FILENAME, 'w') as file:
        json.dump(produtos, file, indent=4)

#Função para salvar os produtos no carrinho
def salvar_produtos_ao_carrinho(produtos):
    with open(FILENAME2, 'w') as file:
        json.dump(produtos, file, indent=4)

#Rota para incluir um produto
@app.route('/produtos', methods=['POST'])
def criar_produtos():
    dados = request.get_json()
    produtos = carregar_produtos()
    novo_produto = {
        "id" : len(produtos) + 1,
        "nome": dados.get("nome"),
        "quantidade": dados.get("quantidade")
    }
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    return jsonify(novo_produto), 201

#Rota para incluir um produto ao carrinho
@app.route('/carrinho/<int:id>', methods=['POST'])
def adicionar_produto_ao_carrinho(id):
    produto = obter_produto(id)
    teste = produto.json['id']
    print(teste)
    produtos = carregar_carrinho()
    novo_produto_no_carrinho = {
        "id" : len(produtos) + 1,
        "id_produtos": produto.json['id'],
        "nome": produto.json['nome'],
        "quantidade": produto.json['quantidade']
    }
    produtos.append(novo_produto_no_carrinho)
    salvar_produtos_ao_carrinho(produtos)
    return jsonify(novo_produto_no_carrinho), 201



#Rota para consultar todas as produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(carregar_produtos())

# Rota para consultar uma produto por ID
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produtos = carregar_produtos()
    produto = next((u for u in produtos if u["id"] == id), None)
    return jsonify(produto) if produto else (jsonify({"erro": "produto não encontrado"}), 404)

# Rota para atualizar uma produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    produtos = carregar_produtos()
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = dados.get("nome", produto["nome"])
            salvar_produtos(produtos)
            return jsonify(produto)
    return jsonify({"erro": "produto não encontrado"}), 404

# Rota para excluir uma produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    produtos = carregar_produtos()
    produtos_filtrados = [u for u in produtos if u["id"] != id]
    if len(produtos) == len(produtos_filtrados):
        return jsonify({"erro": "produto não encontrado"}), 404
    salvar_produtos(produtos_filtrados)
    return jsonify({"mensagem": "produto excluido com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
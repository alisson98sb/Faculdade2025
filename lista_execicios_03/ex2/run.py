from flask import Flask, request, jsonify
import json

app = Flask(__name__)
#2) Crie uma API para cadastro de usuários, permitindo a inclusão, consulta, atualização e exclusão de usuários.
#Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.
FILENAME = 'usuarios.json'

#Função para carregar os usuários
def carregar_usuarios():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
#Função para salvar os usuários
def salvar_usuarios(usuarios):
    with open(FILENAME, 'w') as file:
        json.dump(usuarios, file, indent=4)

#Rota para incluir um usuario
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    usuarios = carregar_usuarios()
    novo_usuario = {
        "id" : len(usuarios) + 1,
        "nome": dados.get("nome"),
        "email": dados.get("email")
    }
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    return jsonify(novo_usuario), 201

#Rota para consultar todos os usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(carregar_usuarios())

# Rota para consultar um usuário por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == id), None)
    return jsonify(usuario) if usuario else (jsonify({"erro": "Usuário não encontrado"}), 404)

# Rota para atualizar um usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_json()
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados.get("nome", usuario["nome"])
            usuario["email"] = dados.get("email", usuario["email"])
            salvar_usuarios(usuarios)
            return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para excluir um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    usuarios = carregar_usuarios()
    usuarios_filtrados = [u for u in usuarios if u["id"] != id]
    if len(usuarios) == len(usuarios_filtrados):
        return jsonify({"erro": "Usuário não encontrado"}), 404
    salvar_usuarios(usuarios_filtrados)
    return jsonify({"mensagem": "Usuário excluído com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
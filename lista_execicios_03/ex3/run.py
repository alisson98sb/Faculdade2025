from flask import Flask, request, jsonify
import json

app = Flask(__name__)
#3) Crie uma API para gerenciar uma lista de tarefas, permitindo adicionar, listar, marcar
#como concluída e excluir tarefas.

FILENAME = 'tarefas.json'

#Função para carregar as tarefas
def carregar_tarefas():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
#Função para salvar as tarefas
def salvar_tarefas(tarefas):
    with open(FILENAME, 'w') as file:
        json.dump(tarefas, file, indent=4)

#Rota para incluir uma tarefa
@app.route('/tarefas', methods=['POST'])
def criar_tarfas():
    dados = request.get_json()
    tarefas = carregar_tarefas()
    nova_tarefa = {
        "id" : len(tarefas) + 1,
        "nome": dados.get("nome")
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return jsonify(nova_tarefa), 201

#Rota para consultar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(carregar_tarefas())

# Rota para consultar uma tarefa por ID
@app.route('/tarefas/<int:id>', methods=['GET'])
def obter_tarefa(id):
    tarefas = carregar_tarefas()
    tarefa = next((u for u in tarefas if u["id"] == id), None)
    return jsonify(tarefa) if tarefa else (jsonify({"erro": "tarefa não encontrada"}), 404)

# Rota para atualizar uma tarefa
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["nome"] = dados.get("nome", tarefa["nome"])
            salvar_tarefas(tarefas)
            return jsonify(tarefa)
    return jsonify({"erro": "tarefa não encontrada"}), 404

# Rota para excluir uma tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    tarefas = carregar_tarefas()
    tarefas_filtrados = [u for u in tarefas if u["id"] != id]
    if len(tarefas) == len(tarefas_filtrados):
        return jsonify({"erro": "tarefa não encontrada"}), 404
    salvar_tarefas(tarefas_filtrados)
    return jsonify({"mensagem": "tarefa excluída com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
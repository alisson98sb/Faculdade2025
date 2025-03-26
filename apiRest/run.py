from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alisson')
def index():
    return 'Bem vindo a api com flask'

@app.route('/api/exemplo', methods=['GET', 'POST'])
def exemplo():
    dados = {'mensagem': 'Resposta de exemplo da sua api com resposta em json'}
    return jsonify(dados), 200, {'Content-type' : 'application/json; charset=utf-8'}

@app.route('/api/parametro', methods=['GET'])
def exemplo_parametro():
    nome = request.args.get('nome', 'Visitante')
    dados = {'mensagem': f'Olá, {nome}!'}
    return jsonify(dados), 200

@app.route('/api/parametroAula', methods=['POST'])
def receber_payload():
    try:
        payload = request.get_json()
        return jsonify({'mensagem': 'Payload recebido com sucesso', "payload" : payload}), 200
    except Exception as e:
        return jsonify({"Erro"}), 500
    
#1) Crie uma API que aceite dois números e realize operações básicas de uma calculadora
#(adição, subtração, multiplicação e divisão)
@app.route('/api/parametro', methods=['POST'])
def ex_1d():
    try:
        payload = request.get_json()
        num1 = payload.get('valor1')
        num2 = payload.get('valor2')
        op = payload.get('operacao')

        if num1 is None or num2 is None or op is None:
            return jsonify({'erro': 'Os campos num1, num2 e operacao são obrigatórios'}), 400
        
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return jsonify({'erro': 'Os valores devem ser numéricos'}), 400
        
        if op == 'adicao':
            resultado = num1 + num2
        elif op == 'subtracao':
            resultado = num1 - num2
        elif op == 'multiplicacao':
            resultado = num1 * num2
        elif op == 'divisao':
            if num2 == 0:
                return jsonify({'erro': 'Divisão por zero não permitida'}), 400
            resultado = num1 / num2
        else:
            return jsonify({'erro': 'Operação inválida. Use adicao, subtracao, multiplicacao ou divisao'}), 400

        return jsonify({'resultado': resultado}), 200
    
    except Exception as e:
        return jsonify({"Erro"}), 500

#2) Crie uma API para cadastro de usuários, permitindo a inclusão, consulta, atualização e exclusão de usuários.
#Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.

if __name__ == '__main__':
    app.run(debug=True)
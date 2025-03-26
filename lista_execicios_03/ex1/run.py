from flask import Flask, request, jsonify

app = Flask(__name__)
    
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

if __name__ == '__main__':
    app.run(debug=True)
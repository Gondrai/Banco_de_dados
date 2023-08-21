headers = {'charset': 'utf-8'}
from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json

    cpf = data['cpf']
    nome = data['nome']
    data_nascimento = data['data_nascimento']

    novoUsuario = Usuario(cpf, nome, data_nascimento)
    users.append(novoUsuario)

    return jsonify({"msg": "Usuário incluído"})

@app.route('/get_user/<int:cpf>', methods=['GET'])
def get_user(cpf):
    for user in users:
        if user.cpf == cpf:
            return jsonify({
                "cpf": user.cpf,
                "nome": user.nome,
                "data_nascimento": user.data_nascimento
                })
    return jsonify({"msg": "Usuário nao encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
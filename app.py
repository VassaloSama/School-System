from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Dados
alunos = {}
turmas = {}
professores = {}

#### ROTA PROFESSORES ####
class Professores:
    def __init__(self, id, nome, idade, materia):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia

        professores[id] = {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia
        }
    
    def serialize(self):
        return professores[self.id]
    
# POST PROFESSORES
@app.route('/professores', methods=['POST'])
def post_professor():
    dados = request.json
    id = dados.get("id")
    
    if id in professores:
        return jsonify({"erro": "Professor com esse ID já existe!"}), 400
    
    novo_professor = Professores(id, dados["nome"], dados["idade"], dados["materia"])
    
    return jsonify(novo_professor.serialize()), 201

# GET ALL PROFESSORES
@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(list(professores.values())), 200

# GET BY ID PROFESSORES
@app.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    if id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    return jsonify(professores[id]), 200

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)


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

# PUT PROFESSORES
@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    if id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    dados = request.json
    professores[id].update(
        {
            "nome": dados["nome"],
            "idade": dados["idade"],
            "materia": dados["materia"]
        }
    )

# DELETE PROFESSORES
@app.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    if id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    del professores[id]
    return jsonify({"mensagem": "Professor deletado com sucesso!"}), 200

#### ROTA TURMAS ####
class Turmas:
    def __init__(self, id, descricao, professor_id, ativo):
        if professor_id not in professores:
            raise ValueError("Professor não encontrado!")

        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

        turmas[id] = {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }
    
    def serialize(self):
        return turmas[self.id]
    
# POST TURMAS
@app.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    id = dados.get("id")
    
    if id in turmas:
        return jsonify({"erro": "Turma com esse ID já existe!"}), 400
    
    professor_id = dados.get("professor_id")
    if professor_id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404

    nova_turma = Turmas(id, dados["descricao"], professor_id, dados["ativo"])
    
    return jsonify(nova_turma.serialize()), 201

# GET ALL TURMAS
@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(list(turmas.values())), 200
 
# GET BY ID TURMAS
@app.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    if id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    
    return jsonify(turmas[id]), 200


# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)


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
    
    # Atualiza apenas os campos que foram enviados na requisição
    if "nome" in dados:
        professores[id]["nome"] = dados["nome"]
    if "idade" in dados:
        professores[id]["idade"] = dados["idade"]
    if "materia" in dados:
        professores[id]["materia"] = dados["materia"]

    return jsonify(professores[id]), 200

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

# PUT TURMAS
@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    if id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    
    dados = request.json
    professor_id = dados.get("professor_id", turmas[id]["professor_id"])

    if professor_id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404

    turmas[id].update({
        "descricao": dados.get("descricao", turmas[id]["descricao"]),
        "professor_id": professor_id,
        "ativo": dados.get("ativo", turmas[id]["ativo"])
    })
    
    return jsonify(turmas[id]), 200

# DELETE TURMAS
@app.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    if id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    
    del turmas[id]
    return jsonify({"mensagem": "Turma deletada com sucesso!"}), 200



#### ROTA ALUNOS ####
class Aluno:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        if turma_id not in turmas:
            raise ValueError("Turma não encontrada!")

        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = float(nota_primeiro_semestre)
        self.nota_segundo_semestre = float(nota_segundo_semestre)
        self.media_final = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

        alunos[id] = {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.media_final
        }
    
    def serialize(self):
        return alunos[self.id]

# POST ALUNOS
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json
    id = dados.get("id")
    
    if id in alunos:
        return jsonify({"erro": "Aluno com esse ID já existe!"}), 400

    turma_id = dados.get("turma_id")
    if turma_id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404

    try:
        datetime.strptime(dados["data_nascimento"], "%Y-%m-%d")
    except ValueError:
        return jsonify({"erro": "Formato da data de nascimento inválido! Use YYYY-MM-DD"}), 400

    novo_aluno = Aluno(
        id, 
        dados["nome"], 
        dados["idade"], 
        turma_id, 
        dados["data_nascimento"], 
        dados["nota_primeiro_semestre"], 
        dados["nota_segundo_semestre"]
    )

    return jsonify(novo_aluno.serialize()), 201

# GET ALL ALUNOS
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(list(alunos.values())), 200

# GET BY ID ALUNOS
@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    if id not in alunos:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    
    return jsonify(alunos[id]), 200

# PUT ALUNOS
@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    if id not in alunos:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    
    dados = request.json
    turma_id = dados.get("turma_id", alunos[id]["turma_id"])

    if turma_id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404

    try:
        if "data_nascimento" in dados:
            datetime.strptime(dados["data_nascimento"], "%Y-%m-%d")
    except ValueError:
        return jsonify({"erro": "Formato da data de nascimento inválido! Use YYYY-MM-DD"}), 400

    alunos[id].update({
        "nome": dados.get("nome", alunos[id]["nome"]),
        "idade": dados.get("idade", alunos[id]["idade"]),
        "turma_id": turma_id,
        "data_nascimento": dados.get("data_nascimento", alunos[id]["data_nascimento"]),
        "nota_primeiro_semestre": float(dados.get("nota_primeiro_semestre", alunos[id]["nota_primeiro_semestre"])),
        "nota_segundo_semestre": float(dados.get("nota_segundo_semestre", alunos[id]["nota_segundo_semestre"]))
    })

    # Recalcular a média final
    alunos[id]["media_final"] = (alunos[id]["nota_primeiro_semestre"] + alunos[id]["nota_segundo_semestre"]) / 2
    
    return jsonify(alunos[id]), 200

# DELETE ALUNOS
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    if id not in alunos:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    
    del alunos[id]
    return jsonify({"mensagem": "Aluno deletado com sucesso!"}), 200



# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
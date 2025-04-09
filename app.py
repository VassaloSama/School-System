from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Dados
alunos = {}
turmas = {}
professores = {}

#### ROTA RESETAR DADOS ####
@app.route('/resetar', methods=['POST'])
def resetar_dados():
    global alunos, turmas, professores
    alunos = {}
    turmas = {}
    professores = {}
    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200
    

    


# POST ALUNOS
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json
    for campo in ["id", "nome", "idade", "data_nascimento", "nota_primeiro_semestre" , "nota_segundo_semestre"]:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório!"}), 400
        
    id = dados.get("id")
    
    if id in alunos:
        return jsonify({"erro": "Aluno com esse ID já existe!"}), 400

    turma_id = dados.get("turma_id")
    if turma_id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404

    try:
        data_formatada = datetime.strptime(dados["data_nascimento"], "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        return jsonify({"erro": "Formato da data de nascimento inválido! Use DD-MM-YYYY"}), 400

    novo_aluno = Aluno(
        id, 
        dados["nome"], 
        dados["idade"],
        turma_id, 
        data_formatada, 
        dados["nota_primeiro_semestre"], 
        dados["nota_segundo_semestre"]
    )

    return jsonify({"mensagem": "Aluno criado com sucesso!"}), 201

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
    dados = request.json

    if not any(campo in dados for campo in ["nome", "idade", "turma_id", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre"]):
        return jsonify({"erro": "Dados Inválidos!"}), 400
    
    if id not in alunos:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    
    dados = request.json
    turma_id = dados.get("turma_id", alunos[id]["turma_id"])

    if turma_id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404

    try:
        if "data_nascimento" in dados:
            dados["data_nascimento"] = datetime.strptime(dados["data_nascimento"], "%d-%m-%Y").strftime("%Y-%m-%d")
    except ValueError:
        return jsonify({"erro": "Formato da data de nascimento inválido! Use DD-MM-YYYY"}), 400

    # Atualiza apenas os campos que foram enviados na requisição
    if "nome" in dados:
        alunos[id]["nome"] = dados["nome"]
    if "idade" in dados:
        alunos[id]["idade"] = dados["idade"]
    if "turma_id" in dados:
        alunos[id]["turma_id"] = dados["turma_id"]
    if "data_nascimento" in dados:
        alunos[id]["data_nascimento"] = dados["data_nascimento"]
    if "nota_primeiro_semestre" in dados:
        alunos[id]["nota_primeiro_semestre"] = dados["nota_primeiro_semestre"]
    if "nota_segundo_semestre" in dados:
        alunos[id]["nota_segundo_semestre"] = dados["nota_segundo_semestre"]

    # Recalcular a média final
    alunos[id]["media_final"] = (alunos[id]["nota_primeiro_semestre"] + alunos[id]["nota_segundo_semestre"]) / 2
    
    return jsonify({"message": "Aluno alterado com sucesso!"}), 200
    
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
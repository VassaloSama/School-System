from flask import request, jsonify, Blueprint
from models.turmas import Turmas
from app import turmas, professores

turmasApp = Blueprint('turma',__name__)

# GET ALL TURMAS
@turmasApp.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(list(turmas.values())), 200
 
# GET BY ID TURMAS
@turmasApp.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    if id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    
    return jsonify(turmas[id]), 200

# PUT TURMAS
@turmasApp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    dados = request.json

    if id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    print("teste")
    
    if not any(campo in dados for campo in ["descricao", "professor_id", "ativo"]):
        return jsonify({"erro": "Dados Inválidos!"}), 400
    
    professor_id = dados.get("professor_id", turmas[id]["professor_id"])

    if professor_id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    print("teste2")

    if "descricao" in dados:
        turmas[id]["descricao"] = dados["descricao"]
    if "professor_id" in dados:
        turmas[id]["professor_id"] = dados["professor_id"]
    if "ativo" in dados:
        turmas[id]["ativo"] = dados["ativo"]

    
    return jsonify({"message": "Turma atualizada com sucesso"}), 200

# DELETE TURMAS
@turmasApp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    if id not in turmas:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    
    del turmas[id]
    return jsonify({"mensagem": "Turma deletada com sucesso!"}), 200

# POST TURMAS
@turmasApp.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    for campo in ["id", "descricao", "professor_id", "ativo"]:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório!"}), 400

    id = dados.get("id")
    
    if id in turmas:
        return jsonify({"erro": "Turma com esse ID já existe!"}), 400
    
    professor_id = dados.get("professor_id")
    if professor_id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404

    nova_turma = Turmas(id, dados["descricao"], professor_id, dados["ativo"])
    
    return jsonify({"message": "Turma criada com sucesso"}), 201

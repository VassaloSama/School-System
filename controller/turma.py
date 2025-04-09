from flask import request, jsonify, Blueprint
from models.turmas import Turmas
from app import turmas

turmasApp = Blueprint('turma', __name__)

# POST TURMAS
@turmasApp.route('/turmas', methods=['POST'])
def post_turma():
    dados = request.json
    try:
        nova_turma = Turmas.criar_turma(dados)
        return jsonify({"message": "Turma criada com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

# GET ALL TURMAS
@turmasApp.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(Turmas.listar_turmas()), 200

# GET BY ID TURMA
@turmasApp.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    turma = Turmas.obter_turma(id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    return jsonify(turma), 200

# PUT TURMA
@turmasApp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    dados = request.json
    try:
        turma_atualizada = Turmas.atualizar_turma(id, dados)
        return jsonify({"message": "Turma atualizada com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

# DELETE TURMA
@turmasApp.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    try:
        Turmas.deletar_turma(id)
        return jsonify({"mensagem": "Turma deletada com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

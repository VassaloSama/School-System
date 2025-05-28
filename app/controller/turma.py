from flask import request, jsonify, Blueprint
from models.turmas import Turmas
from flasgger import swag_from

turmasApp = Blueprint('turma', __name__)

# POST TURMAS
@turmasApp.route('/turmas', methods=['POST'])
@swag_from('../docs/turmas/post.yml')
def post_turma():
    dados = request.json
    try:
        nova_turma = Turmas.criar_turma(dados)
        return jsonify({"message": "Turma criada com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

# GET ALL TURMAS
@turmasApp.route('/turmas', methods=['GET'])
@swag_from('../docs/turmas/get_all.yml')
def listar_turmas():
    return jsonify(Turmas.listar_turmas()), 200

# GET BY ID TURMA
@turmasApp.route('/turmas/<int:id>', methods=['GET'])
@swag_from('../docs/turmas/get_by_id.yml')
def obter_turma(id):
    turma = Turmas.obter_turma(id)
    if not turma:
        return jsonify({"erro": "Turma não encontrada!"}), 404
    return jsonify(turma), 200

# PUT TURMA
@turmasApp.route('/turmas/<int:id>', methods=['PUT'])
@swag_from('../docs/turmas/put.yml')
def atualizar_turma(id):
    dados = request.json
    try:
        turma_atualizada = Turmas.atualizar_turma(id, dados)
        return jsonify({"message": "Turma atualizada com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

# DELETE TURMA
@turmasApp.route('/turmas/<int:id>', methods=['DELETE'])
@swag_from('../docs/turmas/delete.yml')
def deletar_turma(id):
    try:
        Turmas.deletar_turma(id)
        return jsonify({"mensagem": "Turma deletada com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

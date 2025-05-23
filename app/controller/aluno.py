from flask import request, jsonify, Blueprint
from models.alunos import Alunos
from flasgger import swag_from

alunosApp = Blueprint('aluno', __name__)

@alunosApp.route('/alunos', methods=['POST'])
@swag_from('../docs/alunos/post.yml')
def post_aluno():
    dados = request.json
    try:
        novo_aluno = Alunos.criar_aluno(dados)
        return jsonify({"message": "Aluno criado com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

@alunosApp.route('/alunos', methods=['GET'])
@swag_from('../docs/alunos/get_all.yml')
def listar_alunos():
    return jsonify(Alunos.listar_alunos()), 200

@alunosApp.route('/alunos/<int:id>', methods=['GET'])
@swag_from('../docs/alunos/get_by_id.yml')
def obter_aluno(id):
    aluno = Alunos.obter_aluno(id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    return jsonify(aluno), 200

@alunosApp.route('/alunos/<int:id>', methods=['PUT'])
@swag_from('../docs/alunos/put.yml')
def atualizar_aluno(id):
    dados = request.json
    try:
        Alunos.atualizar_aluno(id, dados)
        return jsonify({"message": "Aluno atualizado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

@alunosApp.route('/alunos/<int:id>', methods=['DELETE'])
@swag_from('../docs/alunos/delete.yml')
def deletar_aluno(id):
    try:
        Alunos.deletar_aluno(id)
        return jsonify({"mensagem": "Aluno deletado com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

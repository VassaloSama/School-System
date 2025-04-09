from flask import request, jsonify, Blueprint
from models.alunos import Alunos

alunosApp = Blueprint('aluno', __name__)

# POST ALUNO
@alunosApp.route('/alunos', methods=['POST'])
def post_aluno():
    dados = request.json
    try:
        novo_aluno = Alunos.criar_aluno(dados)
        return jsonify({"message": "Aluno criado com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

# GET ALL ALUNOS
@alunosApp.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(Alunos.listar_alunos()), 200

# GET BY ID ALUNO
@alunosApp.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = Alunos.obter_aluno(id)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    return jsonify(aluno), 200

# PUT ALUNO
@alunosApp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    dados = request.json
    try:
        aluno_atualizado = Alunos.atualizar_aluno(id, dados)
        return jsonify({"message": "Aluno atualizado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

# DELETE ALUNO
@alunosApp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        Alunos.deletar_aluno(id)
        return jsonify({"mensagem": "Aluno deletado com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

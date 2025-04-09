from flask import request, jsonify, Blueprint
from models.professores import Professores

professoresApp = Blueprint('professor',__name__)

# POST PROFESSORES
@professoresApp.route('/professores', methods=['POST'])
def post_professor():
    dados = request.json
    try:
        novo_professor = Professores.criar_professor(dados)
        return jsonify({"message": "Professor criado com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]
    

# GET ALL PROFESSORES
@professoresApp.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(Professores.listar_professores()), 200


# GET BY ID PROFESSORES
@professoresApp.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    professor = Professores.obter_professor(id)
    if not professor:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    return jsonify(professor), 200

# PUT PROFESSORES
@professoresApp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    dados = request.json
    try:
        professor_atualizado = Professores.atualizar_professor(id, dados)
        return jsonify({"message": "Professor atualizado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

# DELETE PROFESSORES
@professoresApp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    try:
        Professores.deletar_professor(id)
        return jsonify({"mensagem": "Professor deletado com sucesso!"}), 200
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]



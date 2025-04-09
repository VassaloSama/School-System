from flask import request, jsonify, Blueprint
from models.professores import Professores
from app import professores

professoresApp = Blueprint('professor',__name__)

# POST PROFESSORES
@professoresApp.route('/professores', methods=['POST'])
def post_professor():
    dados = request.json
    for campo in ["id", "nome", "idade", "materia"]:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório!"}), 400

    id = dados.get("id")
    
    if id in professores:
        return jsonify({"erro": "Professor com esse ID já existe!"}), 400
    
    novo_professor = Professores(id, dados["nome"], dados["idade"], dados["materia"])
    
    return jsonify({"message": "Professor criado com sucesso"}), 201

# GET ALL PROFESSORES
@professoresApp.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(list(professores.values())), 200

# GET BY ID PROFESSORES
@professoresApp.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    if id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    return jsonify(professores[id]), 200

# PUT PROFESSORES
@professoresApp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    dados = request.json

    if not any(campo in dados for campo in ["nome", "idade", "materia"]):
            return jsonify({"erro": "Dados Inválidos!"}), 400

    if id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    
    # Atualiza apenas os campos que foram enviados na requisição
    if "nome" in dados:
        professores[id]["nome"] = dados["nome"]
    if "idade" in dados:
        professores[id]["idade"] = dados["idade"]
    if "materia" in dados:
        professores[id]["materia"] = dados["materia"]

    return jsonify({"message": "Professor atualizado com sucesso"}), 200

# DELETE PROFESSORES
@professoresApp.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    if id not in professores:
        return jsonify({"erro": "Professor não encontrado!"}), 404
    
    del professores[id]
    return jsonify({"mensagem": "Professor deletado com sucesso!"}), 200


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
    

    






# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, jsonify, request
from datetime import datetime

from config import app
from controller.professor import professoresApp
from controller.turma import turmasApp
from controller.aluno import alunosApp

app.register_blueprint(professoresApp)
app.register_blueprint(turmasApp)
app.register_blueprint(alunosApp)

#### ROTA RESETAR DADOS ####
@app.route('/resetar', methods=['POST'])
def resetar_dados():
    from models.professores import professores
    from models.turmas import turmas
    from models.alunos import alunos
    
    alunos.clear()
    turmas.clear()
    professores.clear()

    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200
    
# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
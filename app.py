from flask import Flask, jsonify, request
from datetime import datetime


from config import app, db
from controller.professor import professoresApp
from controller.turma import turmasApp
from controller.aluno import alunosApp

app.register_blueprint(professoresApp)
app.register_blueprint(turmasApp)
app.register_blueprint(alunosApp)

# Criar tabelas no banco
with app.app_context():
    db.create_all()

#### ROTA RESETAR DADOS ####
@app.route('/resetar', methods=['POST'])
def resetar_dados():
    from models.professores import Professor
    from models.turmas import Turma
    from models.alunos import Aluno
    
    Aluno.query.delete()
    Turma.query.delete()
    Professor.query.delete()
    db.session.commit()

    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200
    
# Rodar o servidor
if __name__ == '__main__':
    app.run(host = app.config["HOST"], port = app.config['PORT'], debug = app.config['DEBUG'])
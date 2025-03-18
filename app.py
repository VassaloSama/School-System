from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Dados
alunos = {}
turmas = {}
professores = {}

#### ROTA PROFESSORES ####
class Professores:
    def __init__(self, id, nome, idade, materia):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia

        professores[id] = {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia
        }
    
    def serialize(self):
        return professores[self.id]
    


# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)


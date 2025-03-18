from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Dados
alunos = {}
turmas = {}
professores = {}

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)